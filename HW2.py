# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 19:21:31 2019

@author: Templar
"""
maxL = 0
out = ''
str1 = ''
in_str = []
for i in range (0,100):
    new_word = input()    
    if new_word == '':
        max = i
        break
    else:
        in_str.append(new_word)
    if len(new_word) > maxL:
        maxL = len(new_word)

for sum0 in range(0,max):
    more = maxL - len(in_str[sum0])
    if more != 0:
        in_str[sum0] = in_str[sum0] + ' '*more

for re1 in range(0,maxL):    
    for re2 in range(max,0,-1):
        str1 = in_str[re2-1]
        out = out + str1[re1]
    print(out)
    out = ''
    
