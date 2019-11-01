# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:52:42 2019
Note:In this experiment,We are going to use beautiful soup
@author: Botong Zhao
"""

import bs4
import requests
from bs4 import BeautifulSoup
import wordcloud
import re
from urllib.request import urlopen  #it has Chinese,apply decode()
tag=1
num_page=0
#Test:open the webpage
def openTheWeb(url):
    html = urlopen(url).read().decode('utf-8')
    """
    try:
        print(html)
    except:
        print("Error!!!")
    """
    return html

def text_create(name, msg):
    desktop_path = "./message/"  # 新创建的txt文件的存放路径
    full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    
def crawlerSubPage(url_list,title,date,output):
    global num_page
    global tag
    #creat txt file
    for i in range(len(title)):
        if date[i].string == '(2019-08-30)':
            tag = 0
        if tag:
            subWeb='http://www.ciomp.ac.cn/xwdt/zhxw/' + title[i].get('href') #creat the subWeb's link
            subhtml = openTheWeb(subWeb) #get html of subWeb
            subsoup = BeautifulSoup(subhtml, "html.parser") #get the information
            subdata=subsoup.find('div',class_="TRS_Editor")
            
            if (subdata.find('style')!= None ):
                [s.extract() for s in subdata("style")]
            #print(date[i].string)
            text=title[i].string + date[i].string+subdata.get_text()
            txtname=title[i].string + date[i].string
            text_create(txtname,text.replace(u'\xa0',u''))  #creat the txt file
            
        rowtxt1 = '{} {}'.format(date[i].string.strip('[()]'),title[i].string)
        output.write(rowtxt1)
        #print(rowtxt1)
        output.write('\n')       #write the new line
            
        num_page=num_page+1
    

            

