#!/usr/bin/env python
# coding:utf-8

from urllib import request
from http import cookiejar


class Curl(object):
    """docstring for Urlrequest"""

    def __init__(self):
        self.cj = cookiejar.LWPCookieJar()
        cookie_support = request.HTTPCookieProcessor(self.cj)
        opener = request.build_opener(cookie_support, request.HTTPHandler)
        request.install_opener(opener)
        self.headers = {'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
        "Content-Type": "application/json"}

    def post(self, url, data=None):
        try:
            req = request.Request(url, data, self.headers)
            rsp = request.urlopen(req)
            result = rsp.read().decode('utf-8')
            return result, self.cj
        except Exception as e:
            print('Exception:{e}'.format(e=e))
            return False
