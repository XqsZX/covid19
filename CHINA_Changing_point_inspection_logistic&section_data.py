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
time_interval = 14
province_num = 34
m = 0
n = 1
alpha = [0] * (sample_num - sample - time_interval - 1)
beta = [0] * (sample_num - sample - time_interval - 1)
tau = [0] * (sample_num - sample - time_interval - 1)
alpha_range = [[0] * 2] * (sample_num - sample - time_interval - 1)
beta_range = [[0] * 2] * (sample_num - sample - time_interval - 1)
tau_range = [[0] * 2] * (sample_num - sample - time_interval - 1)
population = np.array(df_population.iloc[0:, 1].values)

for m in range(sample, sample_num - time_interval - 1):
    confirmed_case0 = [0] * province_num
    confirmed_case0_next = [0] * province_num
    confirmed_case1 = [0] * province_num
    confirmed_case1_next = [0] * province_num
    X1 = [0] * province_num
    X2 = [0] * province_num
    Y1 = [0] * province_num
    Y2 = [0] * province_num
    for i in range(province_num):
        confirmed_case0[i] = df.iloc[m, n + i * 3]
        confirmed_case0_next[i] = df.iloc[m + 1, n + i * 3]
        confirmed_case1[i] = df.iloc[m + time_interval, n + i * 3]
        confirmed_case1_next[i] = df.iloc[m + time_interval + 1, n + i * 3]
    for j in range(province_num):
        Y1[j] = (confirmed_case0_next[j] - confirmed_case0[j]) / population[j]
        Y2[j] = (confirmed_case1_next[j] - confirmed_case1[j]) / population[j]
        X1[j] = ((population[j] - confirmed_case0[j]) / population[j]) * confirmed_case0[j] / population[j]
        X2[j] = ((population[j] - confirmed_case1[j]) / population[j]) * confirmed_case1[j] / population[j]
    X = X1 + X2
    Y = Y1 + Y2
    X0 = [0] * province_num + X2
    X = np.column_stack((X, X0))
    X = sm.add_constant(X)
    model = sm.OLS(Y, X)
    results = model.fit()
    # 输出结果
    alpha[m - sample], beta[m - sample], tau[m - sample] = results.params
    [alpha_range[m - sample], beta_range[m - sample], tau_range[m - sample]] = results.conf_int()
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

tau_range_pos = [i[0] for i in tau_range]
tau_range_neg = [i[1] for i in tau_range]
print(tau)
# print(tau_range_pos)
# print(tau_range_neg)
# print(tau_range)
# 绘图
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(tau, 'r--.', label='OLS')
ax.plot(tau_range_pos, '#0BF3F8', label='tau_range_pos')
ax.plot(tau_range_neg, '#0B11F8', label='tau_range_neg')
ax.plot([0] * (sample_num - sample), 'k', label='0')
ax.set_title('CHINA_Changing_point_inspection_logistic&section_data(14)', fontsize=12, color='k')
ax.legend(loc='best')
plt.show()
