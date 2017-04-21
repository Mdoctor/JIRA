#!/usr/bin/env python
#coding:utf-8

from .. import db

class Jira():
	"""docstring for Connect_mysql"""
	def __init__(self):
		self.cur = db.connection.cur
		self.con = db.connection.con

	def exec(self,sql):
		self.cur.execute(sql)
		self.con.commit()
		return self.cur.fetchall()


