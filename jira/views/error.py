#!/usr/bin/env python
#-*-coding:utf-8-*-

from flask import render_template
from . import app

@app.app_errorhandler(404)
def page_no_found(e):
	return render_template('404.html'),404

@app.app_errorhandler(500)
def page_no_found(e):
	return render_template('404.html'),500