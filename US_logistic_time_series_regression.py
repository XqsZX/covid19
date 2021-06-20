import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

# 定义变量
sample_num = 276
sample = 10
delete = 32
K = 329227746
X = [0] * (sample_num - delete - 1)
Y = [0] * (sample_num - delete - 1)
beta = [0] * (sample_num - sample - delete + 1)
alpha = [0] * (sample_num - sample - delete + 1)
beta_range = [[0] * 2] * (sample_num - sample - delete + 1)
alpha_range = [[0] * 2] * (sample_num - sample - delete + 1)

# 读取文件
df_of_USA = pd.read_excel('D:/study/计量经济学/美国疫情数据/美国各州确诊病例（累计值）.xlsx')
# 提取文件中的确诊病例（累计值）
confirmed_case_USA = np.array(df_of_USA.iloc[delete:sample_num + 1, 58].values)
print(confirmed_case_USA)

# 根据公式计算X和Y的值并写入数组中
for i in range(sample_num - delete - 1):
    Y[i] = (confirmed_case_USA[i + 1] - confirmed_case_USA[i]) / K
    X[i] = ((K - confirmed_case_USA[i]) / K) * confirmed_case_USA[i] / K
print(X)
print(Y)
# i = 0
for i in range(sample_num - sample - delete):
    x = []
    y = []
    for j in range(sample):
        x.append(X[i + j])
        y.append(Y[i + j])
    # print(x)
    # print(y)
    x0 = x
    x = sm.add_constant(x)
    model = sm.OLS(y, x)
    results = model.fit()
    alpha[i], beta[i] = results.params
    [alpha_range[i], beta_range[i]] = results.conf_int()
    print(results.conf_int())
    # 输出结果
    print(results.params)
    print(results.summary())
    # # 绘图
    # y_fitted = results.fittedvalues
    # fig, ax = plt.subplots(figsize=(8, 6))
    # ax.plot(x0, y, 'o', label='data')
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
ax.plot([0] * (sample_num - sample - delete + 1), 'k', label='0')
ax.set_title('USA part logistic time series regression', fontsize=12, color='k')
ax.legend(loc='best')
plt.show()
