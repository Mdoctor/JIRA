#!/usr/bin/env python
#coding:utf-8

import pymysql

class Connect_mysql():
	"""docstring for Connect_mysql"""


	def __init__(self,app=None,host=None,user=None,password=None,db=None,port=None):
		if app is not None:
			host,user,password,db,port = self.init_app(app)
		else:
			return self.init_app(app)
		self.con = pymysql.connect(host=host,\
		user=user,password=password,charset='utf8mb4',db=db, port=port,\
		connect_timeout=30,cursorclass=pymysql.cursors.DictCursor)
		self.cur = self.con.cursor()

	def init_app(self,app):
		host=app.config["MYSQL_DATABASE_HOST"],
		user=app.config["MYSQL_DATABASE_USERNAME"],
		password=app.config["MYSQL_DATABASE_PASSWORD"],
		db=app.config["MYSQL_DATABASE_BASE"],
		port=app.config["MYSQL_DATABASE_PORT"]
		return host,user,password,db,port

	def exec(self,sql):
		self.cur.execute(sql)
		self.con.commit()
		return cur.fetchall()

if __name__ == '__main__':
	ms = Connect_mysql()
