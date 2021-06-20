CHINA logistic time series regression（logistic时间序列回归）
方法：每十天进行一次logistic回归，当作该时间段的最后一天的增长率（β），最终绘制出β和β的95％的置信区间曲线（红线，蓝线+浅蓝线）
数据：中国全国疫情数据.xlsx
程序：CHINA_logistic_time_series_regression.py
（要改变时间序列的长短，仅需改变全局变量“sample”即可，本程序中值设定为10）
运行结果：CHINA logistic time series regression.png（黑线代表x=0）

CHINA SIR time series regression（SIR时间序列回归）
方法：每十天进行一次SIR回归，当作是该时间段的最后一天的增长率（β），最终绘制出β的曲线，最终绘制出β和β的95％的置信区间曲线（红线，蓝线+浅蓝线）
数据：中国全国疫情数据.xlsx
程序：CHINA_SIR_time_series_regression.py
（要改变时间序列的长短，仅需改变全局变量“sample”即可，本程序中值设定为10）
运行结果：CHINA SIR time series regression.png（黑线代表x=0）

CHINA logistic section data regression（logistic截面数据回归）
方法：根据每一天，中国各省的疫情数据进行logistic回归，计算出每一天的增长率（β），最终绘制出β和β的95％的置信区间曲线（红线，蓝线+浅蓝线）
数据：中国34个省级行政区人口数.xlsx，中国疫情截面数据.xlsx
程序：CHINA_logistic_section_data_regression.py
（本程序从1.29日开始进行回归，由于前几天的数据过大，为了能更直观地反映总体β的变化，本程序提供了剔除部分数据的功能，修改“sample”值，即可删除开头指定天数的数据，这里设定为36）
运行结果：CHINA all logistic section data regression.png，CHINA part logistic section data regression.png（sample = 0，sample = 36；黑线代表x=0）

CHINA SIR section data regression（SIR截面数据回归）
方法：根据每一天，中国各省的疫情数据进行SIR回归，计算出每一天的增长率（β），最终绘制出β和β的95％的置信区间曲线（红线，蓝线+浅蓝线）
数据：中国34个省级行政区人口数.xlsx，中国疫情截面数据.xlsx
程序：CHINA_SIR_section_data_regression.py
（本程序从1.29日开始进行回归，由于前几天的β值过大，为了能更直观地反映总体β的变化，本程序提供了剔除部分数据的功能，修改“sample”值，即可删除开头指定天数的数据，这里设定为36）
运行结果：CHINA all SIR section data regression.png，CHINA part SIR section data regression.png（sample = 0，sample = 36；黑线代表x=0）

CHINA changing point inspection logistic&section data（logistic截面数据变点检测）
方法：根据每一天，中国各省的疫情数据进行logistic回归，对假设τ=0进行显著性检验，数据分别间隔1天，7天，14天取得，最终绘制出τ和τ的95％的置信区间曲线（红线，蓝线+浅蓝线）
数据：中国34个省级行政区人口数.xlsx，中国疫情截面数据.xlsx
程序：CHINA_Changing_point_inspection_logistic&section_data.py
（要改变回归的时间间隔，仅改动“time_interval”变量即可，此处通过改动数值为1，7，14绘制出题中需要的曲线）
运行结果：CHINA_Changing_point_inspection_logistic&section_data(1).png，CHINA_Changing_point_inspection_logistic&section_data(7).png，CHINA_Changing_point_inspection_logistic&section_data(14).png

USA logistic time series regression（logistic时间序列回归）
方法：每十天进行一次logistic回归，当作该时间段的最后一天的增长率（β），最终绘制出β和β的95％的置信区间曲线（红线，蓝线+浅蓝线）
数据：美国各州确诊病例（累计值）.xlsx
程序：US_logistic_time_series_regression.py
（要改变时间序列的长短，仅需改变全局变量“sample”即可，本程序中值设定为10；要剔除部分数据，修改“delete”值即可删除开头指定天数，这里设定为32）
运行结果：USA all logistic time series regression.png，USA part logistic time series regression.png（由于开头有几个数据不好，故剔除前32个数据点又画了一张，黑线代表x=0）

USA SIR time series regression（SIR时间序列回归）
方法：每十天进行一次SIR回归，当作是该时间段的最后一天的增长率（β），最终绘制出β的曲线，最终绘制出β和β的95％的置信区间曲线（红线，蓝线+浅蓝线）
数据：美国各州确诊病例（累计值）.xlsx，美国各州死亡病例（累计值）.xlsx，美国各州治愈病例（累计值）.xlsx
程序：US_SIR_time_series_regression.py
（要改变时间序列的长短，仅需改变全局变量“sample”即可，本程序中值设定为10；要剔除部分数据，修改“delete”值即可删除开头指定天数，这里设定为56）
运行结果：USA all SIR time series regression.png，USA part SIR time series regression.png（由于开头有几个数据不好，故剔除前56个数据点又画了一张，黑线代表x=0）

USA logistic section data regression（logistic截面数据回归）
方法：根据每一天，美国各州的疫情数据进行logistic回归，计算出每一天的增长率（β），最终绘制出β和β的95％的置信区间曲线（红线，蓝线+浅蓝线）
数据：美国各州确诊病例（累计值）.xlsx，美国各州人口数.xlsx
程序：US_logistic_section_data_regression.py
运行结果：USA logistic section data regression.png（黑线代表x=0）

USA SIR section data regression（SIR截面数据回归）
方法：根据每一天，美国各州的疫情数据进行SIR回归，计算出每一天的增长率（β），最终绘制出β和β的95％的置信区间曲线（红线，蓝线+浅蓝线）
数据：美国各州确诊病例（累计值）.xlsx，美国各州死亡病例（累计值）.xlsx，美国各州治愈病例（累计值）.xlsx，美国各州人口数.xlsx
程序：US_SIR_section_data_regression.py
运行结果：USA SIR section data regression.png（黑线代表x=0）

USA changing point inspection logistic&section data（logistic截面数据变点检测）
方法：根据每一天，美国各州的疫情数据进行logistic回归，对假设τ=0进行显著性检验，数据分别间隔1天，7天，14天取得，最终绘制出τ和τ的95％的置信区间曲线（红线，蓝线+浅蓝线）
数据：美国各州确诊病例（累计值）.xlsx，美国各州人口数.xlsx
程序：US_Changing_point_inspection_logistic&section_data.py
（要改变回归的时间间隔，仅改动“time_interval”变量即可，此处通过改动数值为1，7，14绘制出题中需要的曲线）
运行结果：USA_Changing_point_inspection_logistic&section_data(1).png，USA_Changing_point_inspection_logistic&section_data(7).png，USA_Changing_point_inspection_logistic&section_data(14).png
