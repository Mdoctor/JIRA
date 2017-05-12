#!/usr/bin/env python
# coding:utf-8

from flask import request, render_template, \
    flash, redirect, url_for, make_response
from . import app
import threading
import time
from ..api.Jira_Api import Jira_Api
from ..forms import JiraSubmit
from ..model.jirelist import Jiralist
from .. import db


@app.route('/')
def index():
    if not request.cookies.get('username'):
        return render_template('index.html')
    else:
        user = "Asher"
        return render_template('index.html', user=user)


@app.route('/login/', methods=["POST"])
def login():
    username = request.args.get('username')
    pawwsord = request.args.get('password')
    ja = Jira_Api()
    ret, ck = ja.jira_login(username, pawwsord)
    user = "Asher"
    res = make_response(render_template('index.html', user=user))
    res.set_cookie("username", "jfldksafejadslfajd")
    return res


@app.route("/jira_submit/", methods=["GET", "POST"])
def jira_submit():
    form = JiraSubmit()
    if request.method == "POST":
        summary = form.summary.data
        if form.validate_on_submit():
            getdata = lambda x: str(form[x].data)
            jr = Jiralist(getdata("pid"), getdata("issuetype"), getdata("summary"), getdata("description"), getdata("versiontype"), getdata("field"),
                       getdata("module"), getdata("assignee"), getdata("versions"), getdata("severity"), getdata("reproduce"), getdata("date"))
            db.session.add(jr)
            flash('{}:提单成功'.format(summary))
        else:
            print(form.errors)
            flash('{}:提单失败'.format(summary))
        return redirect(url_for('view.jira_submit'))
    else:
        issue = request.args.get('issues', "issues")
        count = request.args.get('count', "count")
        version_path = request.args.get('version_path', "version_path")
        log_path = request.args.get('log_path', "log_path")
        form.summary.data = "【Pollux：ST：Monkey】{issue}：{count}次".format(
            issue=issue, count=count)
        form.description.data = """【版本路径】：{version_path}\n【测试内容】：6小时monkey\n【期望结果】：手机运行正常，没有错误类型\n\
【实际结果】：{issue}：{count}次\n【log路径】：{log_path}""".format(issue=issue, count=count, version_path=version_path, log_path=log_path)
        return render_template('jira_submit.html', form=form)


@app.route("/jira_list/")
def jira_list():
    page = request.args.get('page', 1, type=int)
    pagination = Jiralist.query.order_by(Jiralist.id.asc()).paginate(page, per_page=5,error_out=False)
    posts = pagination.items
    return render_template('jira_list.html',res=posts,pagination=pagination)


def task(func):
    def warp():
        def printt():
            for x in range(3):
                print(x)
                time.sleep(2)
        threading.Thread(target=printt).start()
        return func()
    return warp


@app.route("/asynctask/")
@task
def asynctask():
    return "OK"