#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import pandas as pd

root_dir='/home/idriver/avos3_0/bugs/robotaxi/速度分析/5_直道_远处后方车辆加速左侧超车/'
self_car='IDPXJILANTU0000777'
target_car='IDPXJT102010BB0003'

car_name=self_car  # self_car/target_car

# 读取 Excel 文件，假设数据在第一个工作表中
df = pd.read_excel(root_dir + car_name + '_速度分析前_毫米波优化前.xls', sheet_name='Sheet1')

# 对时间戳向下取整
df['time_floor'] = df['time_stamp'].apply(lambda x: int(x))

# 按照 time_floor 分组，求平均速度
df = df.groupby('time_floor', as_index=False)['speed'].mean()

# 重命名列名
df = df.rename(columns={'speed': 'mean_speed'})

# 保存结果到新的 Excel 文件
df.to_excel(root_dir + car_name + '_速度分析后_毫米波优化前.xls', sheet_name='Sheet1')