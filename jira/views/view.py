#!/usr/bin/env python
#-*-coding:utf-8-*-

from flask import request,render_template,flash,redirect,url_for
from . import app
from ..model.Mode_Jira import Jira


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
	ModeJira = Jira()
	res = ModeJira.get_all_list
	return render_template('jira_list.html',res=res)


@app.route('/jirasubmit',methods=["POST"])
def jirasubmit():
	ModeJira = Jira()
	if request.method == "POST":
		summary = request.form.get("summary")
		jl = request.values
		valuses = (jl["pid"],jl["issuetype"],jl["summary"],jl["description"],jl["versiontype"],jl["field"],\
		jl["module"],jl["assignee"],jl["versions"],jl["severity"],jl["reproduce"],jl["date"])
		res = ModeJira.add_jira(valuses)
		flash('{}:提单成功'.format(summary))
	return redirect(url_for('view.jira_submit'))
