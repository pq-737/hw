# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:25:15 2019

@author: Templar
"""

import pandas as pd
import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as plt
#下載資料起始日與股票代號
start = datetime.datetime(2018,1,1)
end = datetime.date.today()

# 使用 pdr.get_data_yahoo 
# 取代 pdr.DataReader('2330.tw','yahoo',start,end)
df = pdr.get_data_yahoo('2454.tw',start,end)
#p30 = pdr.get_data_yahoo('2454.tw',start,end)
#顯示前五筆
#print(df.head())



#收盤、30日、60日、90日
df['Close'].plot(figsize=(16, 8))
df['Close'].rolling(window=30).mean().plot(figsize=(16, 8),label='30_day_mean')
df['Close'].rolling(window=60).mean().plot(figsize=(16, 8),label='60_day_mean')
df['Close'].rolling(window=90).mean().plot(figsize=(16, 8),label='90_day_mean')

#線標
plt.legend(loc='uper right',shadow=True,fontsize='x-large')
#標題
plt.title('2454.tw')