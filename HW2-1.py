# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 23:42:17 2019

@author: Templar
"""

import requests , re
from bs4 import BeautifulSoup
mail_sup = re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
phone_sup = re.compile('037-[0-9]+')

def ans_1 ():
    url = 'https://www.csie.nuu.edu.tw/%E7%B3%BB%E4%B8%8A%E6%88%90%E5%93%A1/'
    html = requests.get(url)
    html.encoding="utf-8"
    sp = BeautifulSoup(html.text,'html.parser')
    
    data1 = sp.select("#Content")                           #截取資料區段
    
    t_phone = data1[0].find_all('p',{'class':'phone'})      #抓取號碼
    t_name = data1[0].find_all('h4')                        #抓取姓名
    t_mail = data1[0].find_all('div',{'class':'links'})     #抓取信箱區段 
    
    for i in range(0,len(t_phone)):                         #修正輸出問題 #為了補字串必須先轉成一般格式
        t_phone[i] = t_phone[i].text
                
    mail_out = [None]*len(t_mail)
    for i in range(0,len(t_mail)):
        m =  mail_sup.findall(str(t_mail[i]))               #抓實際mail
        mail_out[i] = m[0]
         
    """列表長度"""
    long_t_phone = len(t_phone)
    long_t_name  = len(t_name)
    long_t_mail  = len(mail_out)
    """不足補齊"""
    long_max = max(long_t_phone,long_t_name,long_t_mail)
    if long_t_phone < long_max:
        t_phone.append(' 無')
    if long_t_name < long_max:
        t_name.append('無')
    if long_t_mail < long_max:
        mail_out.append('無')
        
    print('資工系')
    for i in range(0,long_max): 
        print("教職員姓名:",end=' ')
        print(t_name[i].text)
        print("聯絡電話:",end='  ')
        print(t_phone[i]) 
        print("聯絡信箱:",end='   ')
        print(mail_out[i])
        
def ans_2 ():
    url = 'https://eo.nuu.edu.tw/p/412-1042-2728.php?Lang=zh-tw'
    html = requests.get(url)
    html.encoding="utf-8"
    sp = BeautifulSoup(html.text,'html.parser')   
    
    data1 = sp.select("#Dyn_2_2")           #截取資料區段
                      
    t_name = data1[0].find_all('font')
    t_phone = phone_sup.findall(str(data1[0]))
    t_mail = mail_sup.findall(str(data1[0]))
    
    x = 0
    name_out = [None]*len(t_mail)
    for i in range(0,len(t_name)):
        if len(t_name[i].text) == 3 and t_name[i].text != "辦公室":
            name_out[x] = t_name[i].text
            x += 1
            
    print('光電系') 
    for i in range(0,len(t_mail)):
          print("教職員姓名:",end=' ')
          print(name_out[i])
          print("聯絡電話:",end='   ')
          print(t_phone[i])
          print("聯絡信箱:",end='   ')
          print(t_mail[i])    
         
def ans_3 ():
    url = 'http://120.105.144.203/UIPWeb/wSite/ct?xItem=127738&ctNode=22248&mp=133'
    html = requests.get(url)
    html.encoding="utf-8"
    sp = BeautifulSoup(html.text,'html.parser')
    
    data1 = sp.find_all('div','cp')           #截取資料區段  
    
    t_name = data1[0].find_all('b')
    t_phone = phone_sup.findall(str(data1[0]))
    t_mail = data1[0].find_all("a",{"class":"content"})
    
    mail_out = []
    for i in range(0,len(t_mail)):
        if len(mail_sup.findall(str(t_mail[i].text))) != 0:
            mail_out.append(mail_sup.findall(str(t_mail[i].text)))
            
    print('電子系')
    for i in range(0,len(mail_out)):
        print('教職員姓名:',end='')
        print(t_name[i].text)
        print('聯絡電話:',end='   ')
        if i == 0:
            print(t_phone[i])
            print('聯絡電話:',end='   '+t_phone[i+1])
            print('')
        else:
            print(t_phone[i+1])  
        print('聯絡信箱:',end='   ')
        m = mail_out[i]
        print(m[0])

            
        
ans = input(['1:資工,2:光電,3:電子'])
if ans == '1':
    ans_1()
elif ans == '2':
    ans_2()
elif ans == '3':
    ans_3()   