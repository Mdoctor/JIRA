#!/usr/bin/env python
# coding:utf-8

from flask import request, render_template, \
    flash, redirect, url_for, make_response
from . import app
from ..model.Mode_Jira import Jira
import threading
import time
from ..api.Jira_Api import Jira_Api
from ..forms import JiraSubmit


@app.route('/')
def index():
    if not request.cookies.get('username'):
        return render_template('index.html')
    else:
        user = "Asher"
        return render_template('index.html', user=user)


@app.route('/login', methods=["POST"])
def login():
    username = request.args.get('username')
    pawwsord = request.args.get('password')
    ja = Jira_Api()
    ret, ck = ja.jira_login(username, pawwsord)
    user = "Asher"
    res = make_response(render_template('index.html', user=user))
    res.set_cookie("username", "jfldksafejadslfajd")
    return res


@app.route('/jira_submit')
def jira_submit():
    issue = request.args.get('issues')
    count = request.args.get('count')
    version_path = request.args.get('version_path')
    log_path = request.args.get('log_path')
    return render_template('jira_submit.html', issue=issue, count=count, version_path=version_path, log_path=log_path)


@app.route('/jira_list')
def jira_list():
    ModeJira = Jira()
    res = ModeJira.get_all_list
    return render_template('jira_list.html', res=res)


@app.route('/jirasubmit', methods=["POST"])
def jirasubmit():
    ModeJira = Jira()
    if request.method == "POST":
        summary = request.form.get("summary")
        jl = request.values
        valuses = (jl["pid"], jl["issuetype"], jl["summary"], jl["description"], jl["versiontype"], jl["field"],
                   jl["module"], jl["assignee"], jl["versions"], jl["severity"], jl["reproduce"], jl["date"])
        res = ModeJira.add_jira(valuses)
        flash('{}:提单成功'.format(summary))
    return redirect(url_for('view.jira_submit'))


def task(func):
    def warp():
        def printt():
            for x in range(3):
                print(x)
                time.sleep(2)
        threading.Thread(target=printt).start()
        return func()
    return warp


@app.route("/asynctask")
@task
def asynctask():
    return "OK"


@app.route("/test/")
def test():
    issue = request.args.get('issues')
    count = request.args.get('count')
    version_path = request.args.get('version_path')
    log_path = request.args.get('log_path')
    form = JiraSubmit()
    form.values(issue,count,version_path,log_path)
    return render_template('test.html', form=form)
