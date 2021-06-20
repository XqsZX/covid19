import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

# 定义变量
sample_num = 276
sample = 10
delete = 56
N = 329227746
X1 = [0] * (sample_num - delete)
X2 = [0] * (sample_num - delete)
Y = [0] * (sample_num - delete)
alpha = [0] * (sample_num - sample - delete + 1)
beta = [0] * (sample_num - sample - delete + 1)
gamma = [0] * (sample_num - sample - delete + 1)
R0 = [0] * (sample_num - sample - delete + 1)
alpha_range = [[0] * 2] * (sample_num - sample - delete + 1)
beta_range = [[0] * 2] * (sample_num - sample - delete + 1)
gamma_range = [[0] * 2] * (sample_num - sample - delete + 1)

# 读取文件
df_Infective_USA = pd.read_excel('D:/study/计量经济学/美国疫情数据/美国各州确诊病例（累计值）.xlsx')
df_Mortality_USA = pd.read_excel('D:/study/计量经济学/美国疫情数据/美国各州死亡病例（累计值）.xlsx')
df_Recovery_USA = pd.read_excel('D:/study/计量经济学/美国疫情数据/美国各州治愈病例（累计值）.xlsx')
# 提取文件中的确诊病例（累计值）
Infective_USA = np.array(df_Infective_USA.iloc[delete:sample_num + 1, 58].values)
Mortality_USA = np.array(df_Mortality_USA.iloc[delete:sample_num + 1, 58].values)
Recovery_USA = np.array(df_Recovery_USA.iloc[delete:sample_num + 1, 58].values)
Removal_USA = Mortality_USA + Recovery_USA
# print(Infective_USA)
# print(Mortality_USA)
# print(Recovery_USA)
# print(Removal_USA)

# 根据公式计算X和Y的值并写入数组中
for j in range(sample_num - delete - 1):
    Y[j] = (Infective_USA[j + 1] - Infective_USA[j]) / N
    X1[j] = ((N - Infective_USA[j] - Removal_USA[j]) / N) * Infective_USA[j] / N
    X2[j] = - Infective_USA[j] / N
# print(X1)
# print(X2)
# print(Y)
for i in range(sample_num - sample - delete + 1):
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
print(beta)
print(beta_range_pos)
print(beta_range_neg)
print(beta_range)
# 绘图
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(beta, 'r--.', label='OLS')
ax.plot(beta_range_pos, '#0BF3F8', label='beta_range_pos')
ax.plot(beta_range_neg, '#0B11F8', label='beta_range_neg')
ax.plot([0] * (sample_num - sample - delete + 1), 'k', label='0')
ax.set_title('USA part SIR time series regression', fontsize=12, color='k')
ax.legend(loc='best')
plt.show()
