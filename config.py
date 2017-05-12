#!/usr/bin/env python
# coding:utf-8

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    """docstring for TestingConfig"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://asher:Svc_2017~!@localhost/jira"


config = {
    "testing": TestingConfig,
    "default": TestingConfig
}
