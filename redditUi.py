# -*- coding: UTF-8 -*-

from Tkinter import *
import tkFont
import tkMessageBox
import os
from PIL import ImageTk, Image
import OperateSql

class RedditMainWindow(object):

    def __init__(self):
        self.connsql = OperateSql.ManagerSql('redditdata.db')
        self.root = Tk()
        self.root.withdraw()
        self.root.title("Reddit Downloader")
        self.root.resizable(1,1)
        self.setCenter(650,730)
        self.setWindow()


    def setWindow(self):
        self.label_ft = tkFont.Font(family="黑体",size=14,weight=tkFont.BOLD)
        #起始地址
        self.startUrl_label = Label(self.root,text="起始地址:",font=self.label_ft,padx=10,pady=5,width=8)
        self.startUrl_label.grid(row=0,column=0,sticky='e')

        #起始地址输入框
        self.startUrltext = StringVar()
        self.starturl_entry = Entry(self.root,textvariable=self.startUrltext,width=55,)
        self.startUrltext.set("https://www.reddit.com/r/SupeApp/?count=50&after=t3_6abcya")
        self.starturl_entry.grid(row=0,column=1,sticky='w')

        fram = Frame(self.root,width=500,height=600,)
        fram.grid(row=1,column=0,columnspan=2,sticky='w')
        #预下载用户
        self.preDownloadUser_label = Label(fram, text="预下载用户:", font=self.label_ft, padx=10,width=8,height=5,)
        self.preDownloadUser_label.grid(row=0,column=0,sticky='w')

        #用户数量输入框
        self.preDownloaderNum = StringVar()
        self.preDownloadUserNum_entry = Entry(fram,textvariable=self.preDownloaderNum,width=5)
        self.preDownloaderNum.set('')
        self.preDownloadUserNum_entry.grid(row=0,column=1,sticky='w')

        #添加过滤用户名
        self.adduserfilter = Label(fram, text="添加过滤用户:", font=self.label_ft,padx=10,width=10,height=5,)
        self.adduserfilter.grid(row=0,column=2,sticky='w')

        #用户过滤输入框
        self.userfiltertext = StringVar()
        self.userfilterentry = Entry(fram,textvariable=self.userfiltertext,width=10,)
        self.userfiltertext.set('')
        self.userfilterentry.grid(row=0,column=3,sticky=W)

        #添加按钮
        self.addbutton = Button(fram, text="添加", font=self.label_ft, width=5,command=self.addFilter)
        self.addbutton.grid(row=0, column=4)
        #删除按钮
        self.delbutton = Button(fram, text="删除", font=self.label_ft, width=5,borderwidth=2,command=self.deletefilter)
        self.delbutton.grid(row=0, column=5)

        #过滤器
        self.filterlist = Listbox(fram,height=5)
        self.filterlist.bind('<<ListboxSelect>>', self.getListItem)

        listitem = self.connsql.getFilterUser('filterusers')

        for item in listitem:
            self.filterlist.insert(END, item[0])
        self.filterlist.grid(row=0,column=6,sticky='e')


        #下载信息
        self.fm = Frame(self.root,width=300,height=200,relief=RAISED,bd=1)
        self.fm.grid(row=2,column=1,sticky='w')

        #正在下载
        self.info1 = StringVar()
        self.info1Masseage = Message(self.fm,textvariable=self.info1,width=300,relief=RAISED).pack()
        self.info1.set('小茗同学冷泡茶小茗同')

        self.info2 = StringVar()
        self.info2Masseage = Message(self.fm, textvariable=self.info2, width=400, ).pack()
        self.info2.set('小茗同学冷泡茶')

        self.info3 = StringVar()
        self.info3Masseage = Message(self.fm, textvariable=self.info3, width=400, ).pack()
        self.info3.set('小茗同学冷泡茶')

        self.info4 = StringVar()
        self.info4Masseage = Message(self.fm, textvariable=self.info4, width=400,).pack()
        self.info4.set('小茗同学冷泡茶')

        self.info5 = StringVar()
        self.info5Masseage = Message(self.fm, textvariable=self.info5, width=400,)
        self.info5Masseage.pack()
        self.info5.set('小茗同学冷奥利奥奥利啊')

        self.info6 = StringVar()
        self.info6Masseage = Message(self.fm, textvariable=self.info6, width=400,).pack()
        self.info6.set('小茗同学 冷泡茶小茗同学冷泡茶小')

        self.startbutton = Button(self.root, text="开始", font=self.label_ft, width=5, height=5,borderwidth=2)
        self.startbutton.grid(row=2,column=0,sticky='w')
        #日志信息
        self.logtext = Text(self.root,width=92,height=30,font=self.label_ft,relief=RAISED)
        self.logtext.grid(row=3,columnspan=2,sticky='w',padx=2,pady=10)
        self.logtext.insert(END,'小茗同学冷泡茶小茗同学冷泡茶小\n')
        self.root.mainloop()


    def delpopWindow(self,name):
        print name
        info = u'确定删除%s?'%name

        if tkMessageBox.askyesno("删除操作",info, icon="question"):
            return True
        else:
            return False

    def getListItem(self,event):
        w = event.widget
        self.index = int(w.curselection()[0])

    def addFilter(self):
        filtername = self.userfiltertext.get()
        if filtername:
            if filtername not in self.filterlist.get(0,self.filterlist.size()-1):
                self.filterlist.insert(0,filtername)
                self.connsql.insertFilterData('filterusers', filtername)
            else:
                tkMessageBox.showerror('提示','已存在,无法添加!')
        else:
            tkMessageBox.showinfo('提示','内容为空!')

    def deletefilter(self):
        try:
            if self.filterlist.selection_includes(self.index):
                filtername = self.filterlist.get(self.index)
                if self.delpopWindow(filtername):
                    self.filterlist.delete(self.index)
                    print filtername
                    self.connsql.deleteData('filterusers',filtername)
        except:
            return

    def setCenter(self,width,height):

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight() - 100

        self.root.update_idletasks()
        self.root.deiconify()
        self.root.withdraw()
        self.root.geometry('%sx%s+%s+%s' % (
        width + 10, height + 10, (screen_width - width) / 2,
        (screen_height - height) / 2))
        self.root.deiconify()


if __name__=='__main__':
    Rmw = RedditMainWindow()

