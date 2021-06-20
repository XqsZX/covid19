import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

# 读取文件
df = pd.read_excel('D:/study/计量经济学/中国疫情数据/中国疫情截面数据.xlsx')
df_population = pd.read_excel('D:/study/计量经济学/中国疫情数据/中国34个省级行政区人口数.xlsx')
# 定义常量
sample_num = 267
sample = 0
province_num = 34
m = 0
n = 1
alpha = [0] * (sample_num - sample)
beta = [0] * (sample_num - sample)
gamma = [0] * (sample_num - sample)
R0 = [0] * (sample_num - sample)
alpha_range = [[0] * 2] * (sample_num - sample)
beta_range = [[0] * 2] * (sample_num - sample)
gamma_range = [[0] * 2] * (sample_num - sample)
population = np.array(df_population.iloc[0:, 1].values)

for m in range(sample, sample_num - 1):
    Infective_case = [0] * province_num
    Infective_case_next = [0] * province_num
    Removal_case = [0] * province_num
    X1 = [0] * province_num
    X2 = [0] * province_num
    Y = [0] * province_num
    for i in range(province_num):
        Infective_case[i] = df.iloc[m, n + i * 3]
        Infective_case_next[i] = df.iloc[m + 1, n + i * 3]
        Removal_case[i] = df.iloc[m, n + i * 3 + 1] + df.iloc[m, n + i * 3 + 2]
    # print(Infective_case)
    # print(Infective_case_next)
    # print(Removal_case)
    for j in range(province_num):
        Y[j] = (Infective_case_next[j] - Infective_case[j]) / population[j]
        X1[j] = ((population[j] - Infective_case[j] - Removal_case[j]) / population[j]) * Infective_case[j] / population[j]
        X2[j] = - Infective_case[j] / population[j]
    X = np.column_stack((X1, X2))
    X = sm.add_constant(X)
    model = sm.OLS(Y, X)
    results = model.fit()
    # 输出结果
    alpha[m - sample], beta[m - sample], gamma[m - sample] = results.params
    [alpha_range[m - sample], beta_range[m - sample], gamma_range[m - sample]] = results.conf_int()
    R0[m - sample] = beta[m - sample] / gamma[m - sample]
    print(results.params)
    print(results.summary())
    # # 绘图
    # y_pred = results.predict(X)
    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')  # ax = Axes3D(fig)
    # ax.scatter(X1, X2, Y, c='b', marker='o')
    # ax.scatter(X1, X2, y_pred, c='r', marker='+')
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
ax.plot([0] * (sample_num - 36), 'k', label='0')
ax.set_title('CHINA part SIR section data regression', fontsize=12, color='k')
ax.legend(loc='best')
plt.show()

