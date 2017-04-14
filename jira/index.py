#!/usr/bin/env python
#-*-coding:utf-8-*-

from jira import app
from flask import request,abort,render_template

# app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/jira_submit')
def jira_submit():
	issue = request.args.get('issues')
	count = request.args.get('count')
	version_path = request.args.get('version_path')
	log_path = request.args.get('log_path')
	return render_template('jira_submit.html',issue=issue,count=count,version_path=version_path,log_path=log_path)

@app.route('/jira_list',methods=['GET', 'POST'])
def jira_list():
	return render_template('jira_list.html')