import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

# 定义变量
sample_num = 276
sample = 10
N = 1400050000
X1 = [0] * sample_num
X2 = [0] * sample_num
Y = [0] * sample_num
alpha = [0] * (sample_num - sample + 1)
beta = [0] * (sample_num - sample + 1)
gamma = [0] * (sample_num - sample + 1)
R0 = [0] * (sample_num - sample + 1)
alpha_range = [[0] * 2] * (sample_num - sample + 1)
beta_range = [[0] * 2] * (sample_num - sample + 1)
gamma_range = [[0] * 2] * (sample_num - sample + 1)

# 读取文件
df_of_CHINA = pd.read_excel('D:/study/计量经济学/中国疫情数据/中国全国疫情数据.xlsx')
# 提取文件中的确诊病例（累计值）
Infective_CHINA = np.array(df_of_CHINA.iloc[0:sample_num + 1, 1].values)
Mortality_CHINA = np.array(df_of_CHINA.iloc[0:sample_num + 1, 4].values)
Recovery_CHINA = np.array(df_of_CHINA.iloc[0:sample_num + 1, 5].values)
Removal_CHINA = Mortality_CHINA + Recovery_CHINA
# print(Infective_CHINA)
# print(Mortality_CHINA)
# print(Recovery_CHINA)
# print(Removal_CHINA)

# 根据公式计算X和Y的值并写入数组中
for j in range(sample_num - 1):
    Y[j] = (Infective_CHINA[j + 1] - Infective_CHINA[j]) / N
    X1[j] = ((N - Infective_CHINA[j] - Removal_CHINA[j]) / N) * Infective_CHINA[j] / N
    X2[j] = - Infective_CHINA[j] / N
# print(X1)
# print(X2)
# print(Y)
for i in range(sample_num - sample + 1):
    x1 = []
    x2 = []
    y = []
    for j in range(sample):
        x1.append(X1[i + j])
        x2.append(X2[i + j])
        y.append(Y[i + j])
    # print(x1)
    # print(x2)
    X = np.column_stack((x1, x2))
    X = sm.add_constant(X)
    model = sm.OLS(y, X)
    results = model.fit()
    # 输出结果
    alpha[i], beta[i], gamma[i] = results.params
    R0[i] = beta[i] / gamma[i]
    [alpha_range[i], beta_range[i], gamma_range[i]] = results.conf_int()
    print(results.conf_int())
    print(results.params)
    print(results.summary())
    # # 绘图
    # y_pred = results.predict(X)
    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')  # ax = Axes3D(fig)
    # ax.scatter(x1, x2, y, c='b', marker='o')
    # ax.scatter(x1, x2, y_pred, c='r', marker='+')
    # ax.set_xlabel('X Label')
    # ax.set_ylabel('Y Label')
    # ax.set_zlabel('Z Label')
    # plt.show()

beta_range_pos = [i[0] for i in beta_range]
beta_range_neg = [i[1] for i in beta_range]
# print(beta)
print(beta_range_pos)
print(beta_range_neg)
print(beta_range)
# 绘图
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(beta, 'r--.', label='OLS')
ax.plot(beta_range_pos, '#0BF3F8', label='beta_range_pos')
ax.plot(beta_range_neg, '#0B11F8', label='beta_range_neg')
ax.plot([0] * (sample_num - sample + 1), 'k', label='0')
ax.set_title('CHINA SIR time series regression', fontsize=12, color='k')
ax.legend(loc='best')
plt.show()
