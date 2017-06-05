#-*- coding:utf-8 -*-
#
# '''
#     手机端淘宝广告抓取
# '''
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.by import By
# import requests
#
# mainUrl = "https://www.reddit.com/r/SupeApp/?count=75&after=t3_691aao"
#
# # cap = webdriver.DesiredCapabilities.PHANTOMJS
#
# # cap["phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
#
# # cap["phantomjs.page.settings.resourceTimeout"] = 1000
#
# headers = {
#     "Referer":"https://www.reddit.com/",
#     "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
#     "Cookie":"pc=rz; session_tracker=WoHAh1iOinKPiuhVAR.0.1495079988725.Z0FBQUFBQlpIUncwQ2VpbVoxSVdVLWRfRW04STRNaHE1ZEVQYTMtc21VdDVvUFdjZThTbnRuTzZTalRFSzFiVzdhRUF2ZklXVDFROGVXYVRVUGFpOGphbDktMWJ6YzNEM0dabEZMbkxabnB5b1c4aUVJZVJ5TW1ybUF2MzZNVGhQNUNzTVh4b2FYMHA; _recent_srs=t5_3ghj1; over18=1; edgebucket=RUIXXG4QJlFrnWYkdz; loid=000000000001f14i41.2.1495079797775.Z0FBQUFBQlpIUnQxRGkzMExHVi1QS01JUmNxcjdlOXBGRml1endaTUUydzVkeEZjWmZVWW5mWjBuWG9palRwRk9VTUhWdnRfVGhYcVBBZU9FQ1o4eVQwZUhkcExqOE1aV01HWVkySGw4Q3hISWZldDZyckUxNWVTVXJwY2NiRVEyWmFPa0NPeXo1ckE",
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "Origin":"https://www.reddit.com",
#     "Accept-Encoding":"gzip, deflate"
# }
#
# rs = requests.get(mainUrl,headers=headers)
# print rs.text
#
# # for key, value in enumerate(headers):
# #     webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = value
# #
# #
# # driver = webdriver.PhantomJS()
# #
# # driver.get(mainUrl)
# # try:
# #     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"card")))
# # except:
# #     print "load page failed"
#
# # pagedata = driver.page_source
# # driver.quit()
#
# # soupData = BeautifulSoup(pagedata)
# #
# # print soupData


#
# import logging
# #
# logging.basicConfig(level=logging.DEBUG,
#                 format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                 datefmt='%a, %d %b %Y %H:%M:%S',
#                 filename='reddit.log',
#                 filemode='w')
#
# #################################################################################################
# #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)
# # #################################################################################################
#
# # logging.debug('<This message should go to the log file>')
# logging.info('So should this')
# logging.warning('And this, too')



import os

# os.remove('a')
import re
a = ''' a

                                                        '''


res = re.findall(r'''\['\d.*.'\] = {uid:"\d+"''',a)
for item in res:
    array = re.findall(r'\d+',item)
    print array[0],array[1]


from Tkinter import *


root = Tk()


# 创建两个Label
lb1 = Label(root,text = 'Hello')
lb2 = Label(root,text = 'Grid')

lb1.grid()
lb2.grid()
root.mainloop()















