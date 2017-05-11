#!/usr/bin/env python
# coding:utf-8

from .. import db
from .Mode_Base import Connection


class Jira():
    def __init__(self):
        self.con = Connection(host=db.host,user=db.user,password=db.password,db=db.db,port=db.port).con
        self.cur = self.con.cursor()
        
    def exec(self,sql):
        with self.con.cursor() as cur:
            cur.execute(sql)
            result = cur.fetchall()
        self.con.commit()
        self.con.close()
        return result

    def get_all_list(self,page,limit=5):
        sql = "SELECT id,pid,issuetype,summary,description,versiontype,field,module,assignee,versions,severity,reproduce,f_date FROM j_issues_list limit {start},{limit};".format(start=(page-1)*limit,limit=limit)
        return self.exec(sql)

    def add_jira(self,values):
        values = self.escape_string(values)
        sql = "INSERT INTO j_issues_list (pid,issuetype,summary,description,versiontype,field,module,assignee,versions,severity,reproduce,f_date) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"
        sql = sql % values
        return self.exec(sql)

    def escape_string(self,values):
        values = [x.replace("\\","\\\\") for x in values if isinstance(x,str)]
        values = [x.replace('\"','\\"') for x in values if isinstance(x,str)]
        values = [x.replace("'","\\'") for x in values if isinstance(x,str)]
        return tuple(values)

    @property
    def count(self):
        sql = "SELECT COUNT(*) FROM j_issues_list;"
        return self.exec(sql)


