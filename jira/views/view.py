#!/usr/bin/env python
#-*-coding:utf-8-*-

from flask import request,render_template,flash,redirect,url_for
from . import app
from ..model.base import Connect_mysql

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

@app.route('/jira_list')
def jira_list():
	return render_template('jira_list.html')

@app.route('/listdetail')
def listdetail():
	return render_template('listdetail.html')

@app.route('/jirasubmit',methods=["POST"])
def jirasubmit():
	if request.method == "POST":
		summary=request.form.get('summary',"17389")
		flash('{}:提单成功'.format(summary))
	return redirect(url_for('view.jira_submit'))

@app.route("/test")
def test():
	db = Connect_mysql()
	print (db.exec("select * from j_jira_list;"))
	return ('1')