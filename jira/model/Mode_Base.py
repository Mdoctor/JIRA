#!/usr/bin/env python
# coding:utf-8

import pymysql


class Connect_mysql():
    """docstring for Connect_mysql"""

    def __init__(self, app=None):
        # self.connection = None
        self.host = None
        self.user = None
        self.password = None
        self.db = None
        self.port = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.host = app.config["MYSQL_DATABASE_HOST"]
        self.user = app.config["MYSQL_DATABASE_USERNAME"]
        self.password = app.config["MYSQL_DATABASE_PASSWORD"]
        self.db = app.config["MYSQL_DATABASE_BASE"]
        self.port = app.config["MYSQL_DATABASE_PORT"]
        # self.connection = Connection(host,user,password,db,port)


class Connection():
    """docsting for connect mysql """

    def __init__(self, host=None, user=None, password=None, db=None, port=3306):
        try:
            self.con = pymysql.connect(host=host,user=user, password=password, charset='utf8mb4', db=db, port=port,\
            connect_timeout=30, cursorclass=pymysql.cursors.DictCursor)
        except Exception as e:
            raise GetConfigError(e)


class GetConfigError(Exception):
    """docstring for GetConfigError"""

    def __init__(self, error):
        self.error = error

    def __repr__(self):
        return "Eroor:%s" % self.error
