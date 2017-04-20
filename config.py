#!/usr/bin/env python
#-*-coding:utf-8-*-

import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'     
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	MYSQL_DATABASE_HOST = 'localhost'
	MYSQL_DATABASE_PORT = 3306
	MYSQL_DATABASE_BASE = 'test_user'
	MYSQL_DATABASE_USERNAME = 'asher'
	MYSQL_DATABASE_PASSWORD = 'Svc_2017~!'

	@staticmethod     
	def init_app(app):         
		pass  

class TestingConfig(Config):
	"""docstring for TestingConfig"""
	TESTING = True
	SQLALCHEMY_DATABASE_URI="mysql+pymysql://asher:Svc_2017~!@localhost/jira"
		

config = {
	"testing":TestingConfig,
	"default":TestingConfig
}