#!/usr/bin/env python
# coding:utf-8

from .. import db
from .Mode_Base import Connection


class Jira():
    def __init__(self):
        self.con = Connection(host=db.host, user=db.user,
                              password=db.password, db=db.db, port=db.port).con
        self.cur = self.con.cursor()

    def exec(self, sql):
        with self.con.cursor() as cur:
            cur.execute(sql)
            result = cur.fetchall()
        self.con.commit()
        self.con.close()
        return result

    @property
    def get_all_list(self):
        sql = "SELECT id,pid,issuetype,summary,description,versiontype,field,module,assignee,versions,severity,reproduce,f_date FROM j_issues_list;"
        return self.exec(sql)

    def add_jira(self, values):
        sql = "INSERT INTO j_issues_list (pid,issuetype,summary,description,versiontype,field,module,assignee,versions,severity,reproduce,f_date) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"
        sql = sql % values
        return self.exec(sql)
