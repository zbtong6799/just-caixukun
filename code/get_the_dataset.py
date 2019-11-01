# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 23:24:21 2019

@author: Lenovo
"""
import FunctionFile as FF

#num_page=0
info = []
url = 'http://www.ciomp.ac.cn/xwdt/zhxw/index.html'
html = FF.openTheWeb(url)
#crawl the message
soup = FF.BeautifulSoup(html,"html.parser")
title=soup.find_all('a',class_="font06") #Find all title
date=soup.find_all('td',class_= "riqi")#Find all date
#make a list of news
output1 = open('data.txt','w',encoding='gbk')
output1.write('date title\n')
FF.crawlerSubPage(info,title,date,output1)
#crawl the rest message
url_rest = 'http://www.ciomp.ac.cn/xwdt/zhxw/index_{list}.html'
for i in range(1,38):
    info_rest=[]
    url_take = url_rest.format(list=i)
    html_rest = FF.openTheWeb(url_take)
    
    soup_rest = FF.BeautifulSoup(html_rest,"html.parser")
    title_rest=soup_rest.find_all('a',class_="font06") #Find all title
    date_rest=soup_rest.find_all('td',class_= "riqi")#Find all date
    
    #check url
    #print(url_take)
    
    FF.crawlerSubPage(info_rest,title_rest,date_rest,output1)
    
output1.close()
print(FF.num_page)