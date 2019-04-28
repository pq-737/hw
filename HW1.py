# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 23:44:08 2019

@author: Templar
"""

in_country = []
out_country = []
max = int(input())
for i in range(0,max):
    in_data = input()
    if in_data != '':
       first = in_data.split( )
       in_country.append(first[0])
in_country.sort()                      #排序

for i in range(0,max):
    com = in_country[i]
    if out_country.count(com) == 0:
        out_country.append(com)
for i in range(0,len(out_country)):
    print(out_country[i] + ' ' + str(in_country.count(out_country[i])))
        