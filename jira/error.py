#!/usr/bin/env python
#-*-coding:utf-8-*-

from jira import app
from flask import render_template

# app = Flask(__name__)

@app.errorhandler(404)
def page_no_found(e):
	return render_template('404.html'),404