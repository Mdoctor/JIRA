#!/usr/bin/env python
#-*-coding:utf-8-*-

from flask import request,render_template,flash,redirect,url_for
from . import app
from ..model.jira import Jira

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
	dsb = Jira()
	res = dsb.exec("select id,pid,issuetype,summary,description,versiontype,field,module,assignee,versions,severity,reproduce,f_date from j_issues_list;")
	return render_template('jira_list.html',res=res)


@app.route('/jirasubmit',methods=["POST"])
def jirasubmit():
	if request.method == "POST":
		summary=request.form.get('summary',"17389")
		jl = request.values
		for k,v in request.values.items():
			print (k,v)
		sql = "INSERT INTO j_issues_list (pid,issuetype,summary,description,versiontype,field,module,assignee,versions,severity,reproduce,f_date) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"\
		%(jl["pid"],jl["issuetype"],jl["summary"],jl["description"],jl["versiontype"],jl["field"],\
		jl["module"],jl["assignee"],jl["versions"],jl["severity"],jl["reproduce"],jl["date"])
		print (sql)
		dsb = Jira()
		res = dsb.exec(sql)
		flash('{}:提单成功'.format(summary))
	return redirect(url_for('view.jira_submit'))
