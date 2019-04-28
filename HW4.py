# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:15:38 2019

@author: Templar
"""
in_str = input(['請輸入測試字串，如空白將以 this course is difficult to learn 測試'])
if in_str == '':
    in_str = 'this course is difficult to learn'
list = in_str.split(' ')     #將字串分割成陣列
max = len(list)             #取得陣列長度
if in_str[len(in_str)-1] == ' ':  #假設字串尾巴多一空白字元除錯
    max = max-1
Ans1 = Ans2 = ''
for i in range(0,max):
    str = list[i]
    relen = len(str)
    re_str = str[relen-2:0:-1]              #反轉字串
    str = str[0] + re_str + str[len(str)-1] #字串重組
    #Ans1 += str + ' '                      含空白答案
    Ans2 += str 
#print(Ans1)                                含空白答案
print(Ans2)
    


