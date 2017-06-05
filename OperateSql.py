#-*- coding:utf-8 -*-


import sqlite3


class ManagerSql(object):

    def __init__(self,databasename):

        self.database = databasename

    def createTable(self,tablename):
        conn = sqlite3.connect(self.database)
        conn.execute(
                "CREATE TABLE IF NOT EXISTS %s(id varchar(20) primary key,username varchar(20) not null,url char(50) not null,datatime varchar(50) not null);"%tablename
        )
        conn.close()

    def createFilterTable(self,tablename):
        conn = sqlite3.connect(self.database)
        conn.execute(
                "CREATE TABLE IF NOT EXISTS %s(filteruser varchar(50) primary key);" % tablename
        )
        conn.close()

    def insertFilterData(self,tablename,*args):
        conn = sqlite3.connect(self.database)
        if args:
            for item in args:
                try:
                    conn.execute(
                            "INSERT INTO %s (filteruser) VALUES (?);" % tablename, (item,)
                    )
                except:
                    continue
            conn.commit()
        conn.close()


    def insertData(self,tablename,*args):
        conn = sqlite3.connect(self.database)
        conn.execute(
            "INSERT INTO %s (id,username,url,datatime) VALUES (?,?,?,?);"%tablename,
                (args[0],args[1],args[2],args[3])
        )
        conn.commit()
        conn.close()

    def deleteData(self,tablename,filteruser):
        conn = sqlite3.connect(self.database)

        conn.execute("DELETE FROM %s WHERE filteruser = '%s'"%(tablename,filteruser))
        conn.commit()
        conn.close()

    def dropTable(self,tablename):
        conn = sqlite3.connect(self.database)

        conn.execute(
            "DROP TABLE IF EXISTS %s;"%tablename
        )
        conn.commit()
        conn.close()

    def getFilterUser(self,tablename):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("SELECT filteruser FROM %s" %tablename)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

if __name__=='__main__':
    ms = ManagerSql('redditdata.db')

    s = ['SupeThief',
        'Catorres',
        'tomsrt8','a']

    ms.createFilterTable('filterusers')
    ms.insertFilterData('filterusers',*s)
    # ms.getFilterUser('filterusers')
    ms.deleteData('filterusers','a')