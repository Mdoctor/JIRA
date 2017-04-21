#!/usr/bin/env python
#coding:utf-8

import pymysql


class Connect_mysql():
	"""docstring for Connect_mysql"""
	def __init__(self,app=None):
		self.connection = None
		if app is not None:
			self.init_app(app)
		

	def init_app(self,app):
		host=app.config["MYSQL_DATABASE_HOST"],
		user=app.config["MYSQL_DATABASE_USERNAME"],
		password=app.config["MYSQL_DATABASE_PASSWORD"],
		db=app.config["MYSQL_DATABASE_BASE"],
		port=app.config["MYSQL_DATABASE_PORT"]
		self.connection = Connection(host[0],user[0],password[0],db[0],port)


class Connection():
	def __init__(self,host=None,user=None,password=None,db=None,port=3306):
		try:
			self.con = pymysql.connect(host=host,\
		user=user,password=password,charset='utf8mb4',db=db, port=port,\
		connect_timeout=30,cursorclass=pymysql.cursors.DictCursor)
		except Exception as e:
			raise GetConfigError(e)

class GetConfigError(Exception):
	"""docstring for GetConfigError"""
	def __init__(self,error):
		self.error = error

	def __repr__(self):
		return "Eroor:%s"%self.error



if __name__ == '__main__':
	ms = Connect_mysql()
