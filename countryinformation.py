import requests
import urllib.request
import string
import re
import queue
import ssl
from selenium import webdriver
from urllib.parse import quote
import time
import parsel
from lxml import etree
from selenium import webdriver
from tkinter import *
ssl._create_default_https_context = ssl._create_unverified_context
def find():
    ssl._create_default_https_context = ssl._create_unverified_context
    headers={
            'Host': 'www.wanfangdata.com.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
        }
    name=entry.get()
    url='https://data.stats.gov.cn/search.htm?s='+name
    url = quote(url, safe=string.printable)
    #response=requests.get(url=url,headers=headers)
    #print(response)
    #data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    #print(data)
    browser=webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
    browser.get(url)
    time.sleep(4)
    #print(browser.current_url)
    data=browser.page_source
    #print(data)
    title='<img src="/images/.*?"></a>(.*?)</td>'
    year='<td class="alignC">全国</td><td class="alignC">(.*?)</td>'
    url_1='<a target="_blank" href="(.*?)">'
    title_name=re.compile(title,re.S).findall(data)
    year_name=re.compile(year,re.S).findall(data)
    final_url=re.compile(url_1,re.S).findall(data)
    #print(title_name)
    #print(year_name)
    for i in range(0,len(title_name)):
        #print(title_name[i]+year_name[i])
        #print('https://data.stats.gov.cn/'+final_url[i])
        #print()
        url='https://data.stats.gov.cn/'+final_url[i]
        text.insert(END,'{}'.format(title_name[i]+year_name[i]))
        text.see(END)
        text.update()
        text.insert(END,'{}'.format(url))
        text.see(END)
        text.update()



    #print(page_text)
    browser.quit()



root = Tk()
# 添加界面的标题
root.title('数据网')
# 设置窗口的大小
root.geometry('900x560')
# 只有以上操作的话，界面一闪而过，所以需要把界面进行维持
# 显示界面
# 添加文本：就是提示信息
label = Label(root, text='请输入关键词：', font=('华文行楷', 20))
# 这样之后是没有定位的，显示不出来
# 定位
label.grid()  # 默认为0行0列，即是下面的一行
# 输入框
entry = Entry(root, font=('隶书', 20))
entry.grid(row=0, column=1)  # 定位第一行第二列
# 列表框
text = Listbox(root, font=('隶书', 20), width=50, heigh=15)
text.grid(row=1, columnspan=20)  # 横跨
# 开始按钮
startbutton = Button(root, text=('开始'), font=('隶书', 17),command=find)
startbutton.grid(row=2, column=0, sticky=W)  # sticky代表的是WENS最东西南北
exitbutton = Button(root, text=('退出程序'), font=('隶书', 17),command=root.quit)
exitbutton.grid(row=2, column=1, sticky=E)  # sticky代表的是WENS最东西南北
root.mainloop()

