#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import threading
import urllib
import os
from Queue import Queue
import config
import time
import logging
import OperateSql

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='reddit.log',
                    filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
logging.debug('Start Crawl Reddit User Data')

# 任务队列
task_queque = Queue(maxsize=10)

#线程锁
lock = threading.Lock()


class Thread(threading.Thread):
    def __init__(self,target,args):
        threading.Thread.__init__(self)
        self.target = target
        self.args = args

    def run(self):
        self.target(self.args[0],self.args[1])

#获取用户post下载本地
def getparse(userUrl,name,userdata):
    threads = []


    username = name.strip()
    if '/' in username:
        username = username.replace('/','-')
    print username

    userid = userUrl.split('/')[-1]
    userdata = userdata

    userinfo = [
        userid,
        username,
        userUrl,
        userdata
    ]
    global repeat_count, download_num

    ms.createTable('userdata')
    try:
        ms.insertData('userdata', *userinfo)
    except:
        logging.warning('重复用户跳过')
        repeat_count += 1
        return
    response = requests.get(userUrl)
    soup = BeautifulSoup(response.text)
 
    if username:
        print username
        if not os.path.exists("userpost"+os.sep+username):
            os.makedirs("userpost"+os.sep+username)
    else:
        return

    global alreadyCount
    alreadyCount += 1

    for items in soup.find_all(class_="item-container"):
        if items.find_all('video'):
            for v in items.find_all('video'):
                videourl = v.source.get('src')
                filepath = "userpost"+ os.sep + username+ os.sep + videourl.split('/')[-1]
                logging.info(videourl+' '+filepath)
                threads.append(Thread(downloader,(videourl,filepath)))
        else:
            for p in items.find_all('img',width="720"):
                if p.get('src'):
                    imageurl = 'https:' + p.get('src')
                else:
                    imageurl = 'https:' + p.get('data-original')
                if imageurl:
                    filepath = "userpost"+ os.sep + username + os.sep + imageurl.split('/')[-1]
                logging.info(imageurl+" "+filepath)
                threads.append(Thread(downloader,(imageurl,filepath)))


    global post_count
    post_count += len(threads)
    logging.info("统计"+"("+"正在下载:"+str(len(threads))+', '+"已下载总数:"+str(post_count)+", 重复用户数:"+str(repeat_count)+")")
    if threads:
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    else:
        rmfile = "userpost"+os.sep+username
        os.system("rm -rf %s"%rmfile)

#抓取每页列表用户地址,name
def crawl_user_url(url):
    response = requests.get(url,headers=config.HEADERS)
    soup = BeautifulSoup(response.text)

    for item in soup.find_all(class_="title may-blank outbound"):
        #过滤条件
        try:
            filtername = item.next_sibling.parent.next_sibling.a.string
        except:
            filtername = item.parent.next_sibling.next_sibling.a.string

        filteruser =  ms.getFilterUser('filterusers')
        fusers = []
        for fu in filteruser:
            fusers.append(fu[0])

        if filtername.strip() in fusers:
            continue
        url = item.get('data-href-url')
        username = item.string
        userdata = item.get("data-outbound-expiration")
        if '(' in username:
            username = username.split('(')[0]
        if '|' in username:
            username = username.split('|')[0]

        if re.findall(r'eroshare\.com', url):
            users.append((url,username,userdata))

#抓取下一页地址
def crawl_pageUrl(url):
    response = requests.get(url, headers=config.HEADERS)
    soup = BeautifulSoup(response.text)
    try:
        pageurl = soup.find_all(class_="next-button")[0].a.get("href")
    except:
        return
    return pageurl

#文件下载
def downloader(url,path):
    imagedata = urllib.urlopen(url).read()
    with lock:
        f = file(path,"wb")
        f.write(imagedata)
        f.close()

if __name__=="__main__":

    start_url = config.START_URL
    userUrls = []
    count = 1
    end_page = ''
    download_num = 0
    start_time = time.time()
    post_count = 0
    repeat_count = 0
    ms = OperateSql.ManagerSql('redditdata.db')
    alreadyCount = 0

    while True:
        try:
            download_num = int(raw_input('输入下载用户数量:'))
            break
        except:
            logging.warning('请输入数字')
    while True:
        logging.info('开始时间:' + time.ctime(time.time()))

        logging.info('下载页面地址:'+start_url+'\n')
        users = []
        # try:
        crawl_user_url(start_url)
        # except:
        #     pass
        end_page = start_url
        exit = False
        for list in users:
            print alreadyCount,download_num
            if alreadyCount >= download_num:
                exit = True
                break
            logging.info("用户"+str(count)+':'+str(list[0])+', '+str(list[1]) + '\n')
            getparse(list[0],list[1],list[2])
            count += 1
        start_url = crawl_pageUrl(start_url)
        if not start_url:
            break
        if exit:
            break
    logging.warning('结束地址:'+end_page)
    end_time = time.time()
    logging.info('消耗时间:%ds'%int(end_time-start_time))


