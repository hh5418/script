import requests
import urllib.request
import ssl
import re
import os
import parsel
import string
from tqdm import tqdm
from urllib.parse import quote
from collections import OrderedDict
from selenium import webdriver
from requests.packages import urllib3
from tkinter import *  # 不这样会出现没有导入干净的问题
ssl._create_default_https_context = ssl._create_unverified_context
headers={
		#'Host': 'www.xbiquge.la',
		#'Referer': 'https://www.xbiquge.la/10/10489/',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36' 
	}

def show_infor(data):
    _name='<span class="s2">.*?<a href=".*?">(.*?)</a>'
    _id='<span class="s2">.*?<a href="(.*?)">.*?</a>'
    aut='<span class="s4">(.*?)</span>'
    global book_name
    book_name=re.compile(_name,re.S).findall(data)
    global book_id
    book_id=re.compile(_id,re.S).findall(data)
    autor=re.compile(aut,re.S).findall(data)
    print('共搜索到{}部相关小说'.format(len(book_name)))
    
    
    #print(a)
    #for i in range(0,len(book_name)):
        #a['name']=book_name[i]
        #a['id']=book_id[i]
    
    for i in range(0,len(book_name)):
        #print(str(i))
        #print(book_name[i])
        #print(book_id[i])
        #print(autor[i+1])
        text.insert(END,'{}'.format('第'+str(int(i+1))+'本:'+book_name[i]))
        text.see(END)
        text.update()
    
    #d = OrderedDict()
    #for i in range(0,len(book_name)):
        #d['{}'.format(book_name[i])]=book_id[i]
    #return d
def show_id():
    #text.insert(END,'{}'.format('请输入要的序号：')
    #text.see(END)
    #text.update()
    theid=int(entry2.get())
    #name=entry.get()
    page=int(entry3.get())
    
    #print('请输入要爬的序号：')
    #for i in range(0,len(the_name)):
    id=book_id[theid]
    name=book_name[theid]
    path='D:\\Python\\fangbian\\'+name
    #print('请输入要爬的页数：')
    #page=int(input())
    #os.path.exists(path)
    if os.path.exists(path)==False:
        #er(id,name,page)
        os.mkdir(path)
    #x=0
    #while x<page:
    for i in range(1,page):#这是小说翻的页数，最后一页不满20先不爬
        url='https://www.bqg.lol'+id+'index_'+str(i)+'.html'
		#print(url)
		#print(url)
					

        urllib3.disable_warnings()
        response=requests.get(url=url,headers=headers,verify=False)

        _name='<li><a href=".*?">(.*?)</a>'
        _id='<li><a href="'+id+'(.*?).html">.*?</a>'
        page_name=re.compile(_name,re.S).findall(response.text)
        page_id=re.compile(_id,re.S).findall(response.text)
				#print(len(page_name))
				#print(len(page_id))
				#print(page_nam5e[-20:])
        name_new=page_name[-20:]
        id_new=page_id[-20:]
				#print(name_new)
				#print(id_new)
        fh=open('D:\\Python\\fangbian\\'+name+'\\{}.txt'.format(name_new[0]+'开始20章'),mode='w',encoding='utf-8')
        y=0
				#for i in id_new:
        for i in tqdm(id_new):
					#x=0
					#text(name_new[i],id_new[i])
            urllib3.disable_warnings()
            the_url='https://www.bqg.lol'+id+i+'.html'
					#print('!!!!!!!!!!!!!'+the_url)
            ssl._create_default_https_context = ssl._create_unverified_context    
            response=requests.get(url=the_url,headers=headers,verify=False)
					#print(response.text)
            selec=parsel.Selector(response.text)
            content_list=selec.css('#content::text').getall()
            content=''.join(content_list)
					#print(content)
						#print(content)

            fh.write(name_new[y])
            fh.write('\n')
            fh.write(content)
            fh.write('\n')
            y+=1
					#break
						#print("okok")
        fh.close
    text.insert(END,'{}'.format('下载完成！！！'))
    text.see(END)
    text.update()

#def er(id,name,page):
    #path='D:\\Python\\fangbian\\'+name
   # os.mkdir(path)
    #x=0
    #while x<page:
       # for i in range(1,page):#这是小说翻的页数，最后一页不满20先不爬
        #    url='https://www.bqg.lol'+id+'index_'+str(i)+'.html'
         #   #url='https://www.bqg.lol'+id+'index_'+str(i)+'.html'
		#print(url)
			    #print(url)
        #    urllib3.disable_warnings()
        	#urllib3.disable_warnings()
        #    response=requests.get(url=url,headers=headers,verify=False)
         #   _name='<li><a href=".*?">(.*?)</a>'
        #    _id='<li><a href="'+id+'(.*?).html">.*?</a>'
      #      page_name=re.compile(_name,re.S).findall(response.text)
        #    page_id=re.compile(_id,re.S).findall(response.text)
				#print(len(page_name))
				#print(len(page_id))
				#print(page_nam5e[-20:])
        #    name_new=page_name[-20:]
        #    id_new=page_id[-20:]
				#print(name_new)
				#print(id_new)
       #     fh=open('D:\\Python\\fangbian\\'+name+'\\{}.txt'.format(name_new[0]+'开始20章'),mode='a',encoding='utf-8')
       #     z=0
				#for i in id_new:
      #      for i in tqdm(id_new):
					#x=0
					#text(name_new[i],id_new[i])
       #         urllib3.disable_warnings()
        #        the_url='https://www.bqg.lol'+id+i+'.html'
					#print('!!!!!!!!!!!!!'+the_url)
         #       ssl._create_default_https_context = ssl._create_unverified_context    
         #       response=requests.get(url=the_url,headers=headers,verify=False)
					#print(response.text)
          #      selec=parsel.Selector(response.text)
         #       content_list=selec.css('#content::text').getall()
          #      content=''.join(content_list)
					#print(content)
						#print(content)

         #       fh.write(name_new[z])
         #       fh.write('\n')
         #       fh.write(content)
         #       fh.write('\n')
          #      z+=1
					#break
						#print("okok")
      #      fh.close
      #  x+=1
      #  text.insert(END,'{}'.format('下载完成！！！'))
       # text.see(END)
       # text.update()
          #x+=1
#def text(name,id):
def start():    
    name=entry.get()
    url='https://www.bqg.lol/ar.php?keyWord='+name
    url2= quote(url, safe=string.printable)
    data=urllib.request.urlopen(url2).read().decode('utf-8','ignore')
    #print(len(data))  
    show_infor(data)

root = Tk()
# 添加界面的标题
root.title('笔趣阁下载器(注意：每20章为一个单位)')
# 设置窗口的大小
root.geometry('860x560')
# 只有以上操作的话，界面一闪而过，所以需要把界面进行维持
# 显示界面
# 添加文本：就是提示信息
label = Label(root, text='下载前需先把有的目录删除，请输入小说名称：',font=('华文行楷', 20))
label.grid(row=0,column=0)

label2= Label(root,text='请输入要看的小说的序号(从0开始)',font=('华文行楷',20))
label2.grid(row=1,column=0)

label3= Label(root,text='与上面的一起填写，请输入要看的页数(>1)：',font=('华文行楷',20))
label3.grid(row=2,column=0)
# 这样之后是没有定位的，显示不出来
# 定位
#label.grid(row=0,column=0)  # 默认为0行0列，即是下面的一行
# 输入框
entry = Entry(root, font=('隶书', 20))
entry.grid(row=0, column=1)  # 定位第一行第二列


#label.grid(row=1,column=0)
entry2 = Entry(root, font=('隶书', 20))
entry2.grid(row=1, column=1)

entry3 = Entry(root, font=('隶书', 20))
entry3.grid(row=2, column=1)
# 列表框
text = Listbox(root, font=('隶书', 20), width=50, heigh=15)
text.grid(row=3, columnspan=2)  # 横跨
# 开始按钮
#查找按钮
startbutton = Button(root, text=('开始下载'), font=('隶书', 17),command=start)
startbutton.grid(row=4, column=0, sticky=W)  # sticky代表的是WENS最东西南北
continuebutton = Button(root, text=('继续下载'), font=('隶书', 17),command=show_id)
continuebutton.grid(row=4, column=0, sticky=E)  # sticky代表的是WENS最东西南北
exitbutton = Button(root, text=('退出程序'), font=('隶书', 17),command=quit)
exitbutton.grid(row=4, column=1, sticky=E)  # sticky代表的是WENS最东西南北


root.mainloop()


#entry2   是序号
#现在要加上返回名字，
#













