#!/usr/bin/env python
# coding:utf-8

from jira import create_app
import os

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

app.run(host='0.0.0.0', debug=True, threaded=True)
