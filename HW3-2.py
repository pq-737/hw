# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:38:43 2019

@author: Templar
"""
#import time
import requests
from bs4 import BeautifulSoup

html_url = 'https:'

def get_web_page(url):
    html = requests.get(url)
    return html.text

def get_articles(dom):
    sp = BeautifulSoup(dom, 'html.parser')    
    paging_div = sp.find('div' , 'page')
    next_url = paging_div.find('a','nxt')['href']   #<a>,class=nxt中的herf 圍下一頁支連結    
    articles = []   #用來儲存書本資料
    book_data = sp.find('ul' , 'searchbook')    #當頁全部書籍資料
    books = book_data.find_all('li','item')     #各本書籍資料    
    for i in books:
        price = i.find_all('strong')
        if len(price) == 1:
            price = i.find_all('strong')[0]('b')
        else:
            price = i.find_all('strong')[1]('b')
        if int(price[0].text) > 0:
            title = i.find('a')['title']
            price = price
            articles.append({
                    'title':title,
                    'price':price[0].text
                    })
    return articles,next_url   
    
current_page = get_web_page(html_url + '//search.books.com.tw/search/query/cat/all/key/python/sort/1/page/1/v/0/')
if current_page:
    articles = []   #目前頁面全部書籍
    current_book , next_url = get_articles(current_page)
    page = 0        
    while current_book and page != 3:       #page為抓取頁面上限!!!!別太多!!!!!
        articles += current_book        
        current_page = get_web_page(html_url + next_url)
        
        current_book , next_url = get_articles(current_page)
        page += 1
    current_book = ''
    print('總共有',len(articles),'本與python相關的書')
    key_price = 500
    for i in articles:
        if int(i['price']) < key_price:
            print('書名:',i['title'])
            print('價格:',i['price'])
    

