# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:45:56 2019

@author: Templar
"""

import requests
from bs4 import BeautifulSoup

url = 'http://www.taiwanlottery.com.tw/'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')

data1 = sp.select("#rightdown")
#print(data1)

data2 = data1[0].find('div', {'class':'contents_box01'})
#print(data2)

data3 = data2.find_all('div', {'class':'ball_tx'})
#print(data3)
#
# 威力彩號碼
print("開出獎號：",end="")
for n in range(0,20):
    print(data3[n].text,end="  ") 


     
## 超級獎號
red = data2.find('div', {'class':'ball_red'})        
print("\n超級獎號：{}".format(red.text)) 