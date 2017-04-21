#!/usr/bin/env python
#coding:utf-8

from .. import db

class Jira():
	"""docstring for Connect_mysql"""
	def __init__(self):
		self.con = db.connection.con
		

	def exec(self,sql):
		cur = self.con.cursor()
		cur.execute(sql)
		self.con.commit()
		res = cur.fetchall()
		cur.close()
		return res


