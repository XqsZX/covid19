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
beta = [0] * (sample_num - sample)
alpha = [0] * (sample_num - sample)
beta_range = [[0] * 2] * (sample_num - sample)
alpha_range = [[0] * 2] * (sample_num - sample)
population = np.array(df_population.iloc[0:, 1].values)

for m in range(sample, sample_num - 1):
    confirmed_case = [0] * province_num
    confirmed_case_next = [0] * province_num
    X = [0] * province_num
    Y = [0] * province_num
    for i in range(province_num):
        confirmed_case[i] = df.iloc[m, n + i * 3]
        confirmed_case_next[i] = df.iloc[m + 1, n + i * 3]
    print(confirmed_case)
    print(confirmed_case_next)
    for j in range(province_num):
        Y[j] = (confirmed_case_next[j] - confirmed_case[j]) / population[j]
        X[j] = ((population[j] - confirmed_case[j]) / population[j]) * confirmed_case[j] / population[j]
    x0 = X
    X = sm.add_constant(X)
    model = sm.OLS(Y, X)
    results = model.fit()
    alpha[m - sample], beta[m - sample] = results.params
    [alpha_range[m - sample], beta_range[m - sample]] = results.conf_int()
    # 输出结果
    print(results.conf_int())
    print(results.params)
    print(results.summary())
    # # 绘图
    # y_fitted = results.fittedvalues
    # fig, ax = plt.subplots(figsize=(8, 6))
    # ax.plot(x0, Y, 'o', label='data')
    # ax.plot(x0, y_fitted, 'r--.', label='OLS')
    # ax.legend(loc='best')
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
ax.plot([0] * (sample_num - sample), 'k', label='0')
ax.set_title('CHINA all logistic section data regression', fontsize=12, color='k')
ax.legend(loc='best')
plt.show()
