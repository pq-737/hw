# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:25:15 2019

@author: Templar
"""

import pandas as pd
import pandas_datareader as pdr
import datetime
#下載資料起始日與股票代號
start = datetime.datetime(2018,1,1)
end = datetime.date.today()

# 使用 pdr.get_data_yahoo 
# 取代 pdr.DataReader('2330.tw','yahoo',start,end)
df = pdr.get_data_yahoo('2454.tw',start,end)
#p30 = pdr.get_data_yahoo('2454.tw',start,end)
#顯示前五筆
#print(df.head())


df=df.drop(['High','Low','Volume','Open','Adj Close'],axis=1) 

#顯示所有筆數
print(df)
print()
print(df.rolling(window = 30).mean())
print(df.rolling(window = 60).mean())
print(df.rolling(window = 90).mean())