import requests as rq 
from lxml import etree 
import os 
from selenium.webdriver import Chrome

c = Chrome()

def rqget(root):
    r = rq.get(root)
    r.encoding = r.apparent_encoding 
    #if r.response_code == '200':
    return r.text

def cget(root):
    c.get(root)
    txt = c.page_source
    c.close()
    return txt

root = r'https://bgm.tv/anime/browser/?sort=date'
#print(rqget(root))# So I will discard this method to get page source and utilize selenium to do it 
#I need complete this work(scripts) soon so I don't care the speed of spider .
#print(cget(root))
c.get(root)
page_num = c.find_element_by_class_name('p_edge').text.split('/')[1].split(')')[0].strip()
print(page_num)
