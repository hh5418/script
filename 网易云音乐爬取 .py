#from tkinter import *  # 不这样会出现没有导入干净的问题
from selenium import webdriver																			#第一步																								#导入事件模块以应对一部分反爬
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from urllib.request import urlretrieve
import time
import re
#from selenium.webdriver.common.keys import Keys
#import get_id
from urllib.parse import quote
import string
import urllib.parse
import base64
#from selenium import webdriver
#from bs4 import BeautifulSoup as bs
import requests
import random
from Crypto.Cipher import AES
from tkinter import *  # 不这样会出现没有导入干净的问题
# import lxml
import json
def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    text = text.encode("utf-8")
    encryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text.decode('utf-8')

def asrsea(p1, p2, p3, p4):
    res = {}
    rand_num = "aq9d7cvBOJ1tzj1o"
    vi = b"0102030405060708"
    h_encText = AES_encrypt(p1, p4, vi)
    h_encText = AES_encrypt(h_encText, rand_num, vi)
    res["encText"] = h_encText
    res["encSecKey"] = "5dec9ded1d7223302cc7db8d7e0428b04139743ab7e3d451ae47837f34e66f9a86f63e45ef20d147c33d88530a6c3c9d9d88e38586b42ee30ce43fbf3283a2b10e3118b76e11d6561d80e33ae38deb96832b1a358665c0579b1576b21f995829d45fc43612eede2ac243c6ebb6c2d16127742f3ac913d3ac7d6026b44cee424e"
    return res

header={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
        #'Postman-Token':'4cbfd1e6-63bf-4136-a041-e2678695b419',
        "origin":'https://music.163.com',
       # 'referer':'https://music.163.com/song?id=1372035522',
        'accept-encoding':'gzip,deflate,br',
        'Accept':'*/*',
        'Host':'music.163.com',
        'content-lenth':'472',
        'Cache-Control':'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'Connection':'keep-alive',
        #'Cookie':'iuqxldmzr_=32; _ntes_nnid=a6f29f40998c88c693bc910331bd6bea,1558011234325; _ntes_nuid=a6f29f40998c88c693bc910331bd6bea; _ga=GA1.2.2120707788.1559308501; WM_TID=pV2C%2BjTrRwBBAAERUVJojniTwk8%2B8Zta; JSESSIONID-WYYY=nvf%2BggodQRfcT%2BTvBRmANqMrsDeQCxRvqwFsxDr3eJvNNWhGYFhfCXKFkfAfOdbHhpCsMzT39mAeJ7ZamBQZbiwwtnSZD%5CPWRqKxD9t6dGKD3bTVjomjgB39DB07RNIWI32bYKa2H4fg1qQgqI%2FR%2B%2Br%2BZXJvgFg1Vh%2FA2XRj9S4p0EMu%3A1560927288799; WM_NI=DthwcEQf5Ew2NbTIZmSNhSnm%2F8VWsg5RxhkYogvs2luEwZ6m5UhdzbHYPIr654ZBWKV4o22%2BEwb9BvdLS%2BFOmOAEUG%2B8xd8az4CX%2FiAL%2BZkz3syA0onCPkhQwCtL4pkUcjg%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed2d650989c9cd1dc4bb6b88eb2c84e979f9aaff773afb6fb83d950bcb19ecce92af0fea7c3b92a88aca898e24f93bafba6f63a8ebe9caad9679192a8b4ed67ede89ab8f26df78eb889ea53adb9ba94b168b79bb9bbb567f78ba885f96a8c87a0aaf13ef7ec96a3d64196eca1d3b12187a9aedac17ea8949dccc545af918fa6d84de9e8b885bb6bbaec8db9ae638394e5bbea72f1adb7a2b365ae9da08ceb5bb59dbcadb77ca98bad8be637e2a3'
        }

def get_music_name():
    #name = entry.get()
    name=entry.get()
    chrome_driver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
    option=webdriver.ChromeOptions()
    option.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=chrome_driver,chrome_options=option)
    #name=quote(name, safe=string.printable)
    #print(name)
    url="https://music.163.com/#/search/m/?s={}".format(name)
    driver.get(url)
    time.sleep(1)
                #由于网页中有iframe框架，进行切换
    driver.switch_to.frame('g_iframe')
                #等待0.5秒
    time.sleep(1)
                #抓取到页面信息
    page_text = driver.execute_script("return document.documentElement.outerHTML")
    #print(page_text)
    get_id='<div class="hd"><a id="song_(.*?)"'
    get_name='<b title="(.*?)">'
    id=re.compile(get_id,re.S).findall(page_text)
    song_name=re.compile(get_name,re.S).findall(page_text)
    driver.quit()
    name=song_name[0]
    song_i=id[0]
    url2 = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="
    param1 = json.dumps({"ids":"[{}]".format(song_i),"level":"standard","encodeType":"aac","csrf_token":""})
    param2="010001"
    param3="00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
    param4="0CoJUm6Qyw8W8jud"
    asrsea_res = asrsea(param1, param2, param3, param4)
    param_data = {"params": asrsea_res["encText"],
                "encSecKey": asrsea_res["encSecKey"]}
    #print(param_data)
    fromdata={
        "params":asrsea_res["encText"]
        ,"encSecKey":asrsea_res["encSecKey"],
    }

    fromdata=urllib.parse.urlencode(fromdata).encode('utf-8')

    req=requests.post(url=url2,data=fromdata,headers=header,)
    res2=json.loads(req.text)
    url=str(res2['data'][0]['url'])
    get_song(url,name)

def get_song(url,name):
    try:
        #print(url)
        text.insert(END,'歌曲：{}  ...正在下载......'.format(name))
        text.see(END)
        text.update()
        urlretrieve(url,filename='E:/迅雷下载/音频/{}.m4a'.format(name))
        text.insert(END,'歌曲：{}  下载成功......'.format(name))
        text.see(END)
        text.update()
                    #urllib.request.urlretrieve(url,'E:\\迅雷下载\\音频\\{}.m4a'.format(name))
                    #存入本地
                    #audio_content = requests.get(url=url,headers=headers).content
                    #with open('E:\迅雷下载\音频\{}.m4a'.format(name),'ab') as f :
                    #    f.write(audio_content.content)
                    #    #f.close()
        #print("爬取成功！！！")

                    #url = 'http://music.163.com/song/media/outer/url?id={}'.format(id)+ '.m4a'
                    #print(url)
    except Exception as err:
        print(err)



root = Tk()
# 添加界面的标题
root.title('网易云音乐下载器')
# 设置窗口的大小
root.geometry('760x560')
# 只有以上操作的话，界面一闪而过，所以需要把界面进行维持
# 显示界面
# 添加文本：就是提示信息
label = Label(root, text='请输入音乐名称：', font=('华文行楷', 20))
# 这样之后是没有定位的，显示不出来
# 定位
label.grid()  # 默认为0行0列，即是下面的一行
# 输入框
entry = Entry(root, font=('隶书', 20))
entry.grid(row=0, column=1)  # 定位第一行第二列
# 列表框
text = Listbox(root, font=('隶书', 20), width=50, heigh=15)
text.grid(row=1, columnspan=2)  # 横跨
# 开始按钮
startbutton = Button(root, text=('开始下载'), font=('隶书', 17),command=get_music_name)
startbutton.grid(row=2, column=0, sticky=W)  # sticky代表的是WENS最东西南北
exitbutton = Button(root, text=('退出程序'), font=('隶书', 17),command=root.quit)
exitbutton.grid(row=2, column=1, sticky=E)  # sticky代表的是WENS最东西南北
root.mainloop()











