#!/usr/bin/env python
#-*-coding:utf-8-*-

from flask import request,render_template,flash,redirect,url_for
from . import app
from ..model.jirelist import Jiralist
from .. import db

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

@app.route('/jirasubmit',methods=["POST"])
def jirasubmit():
	if request.method == "POST":
		summary=request.form.get('summary',"17389")
		alls = Jiralist(request.form.get("pid"),request.form.get("issuetype"),request.form.get("summary"),request.form.get("description"),request.form.get("versiontype"),request.form.get("field"),request.form.get("module"),request.form.get("assignee"),request.form.get("versions"),request.form.get("severity"),request.form.get("reproduce"),request.form.get("date"))
		print (db.session.add(alls))
		flash('{}:提单成功'.format(summary))
	return redirect(url_for('view.jira_submit'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'