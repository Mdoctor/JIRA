#!/usr/bin/env python
# coding:utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField
from wtforms.validators import Required


class JiraSubmit(FlaskForm):
    requir = "<strong style=\"color:red\">* </strong>"
    pid = SelectField("项目：", validators=[Required(
        "Please enter")], choices=[("ROM", "ROM"), ("POLLUX", "POLLUX")])
    issuetype = StringField(
        requir + "问题类型：", validators=[Required("Please enter")],default="缺陷")
    summary = StringField(
        requir + "主题：", validators=[Required("Please enter")],default="【Pollux：ST：Monkey】{{issue}}：{{count}}次")
    description = TextAreaField(
        requir + "描述：", validators=[Required("Please enter")],default="【版本路径】：{{version_path}} &#13;&#10【测试内容】：6小时monkey &#13;&#10【期望结果】：手机运行正常，没有错误类型&#13;&#10【实际结果】：{{issue}}：{{count}}次&#13;&#10【log路径】：{{log_path}}")
    versiontype = SelectField("版本类型：", validators=[Required(
        "Please enter")], choices=[(1, "test"), (2, "dev")])
    field = SelectField("领域：", validators=[Required(
        "Please enter")], choices=[(1, "test"), (2, "dev")])
    module = SelectField("模块：", validators=[Required(
        "Please enter")], choices=[(1, "test"), (2, "dev")])
    assignee = SelectField("处理人：", validators=[Required(
        "Please enter")], choices=[(1, "test"), (2, "dev")])
    versions = SelectField("影响版本：", validators=[Required(
        "Please enter")], choices=[(1, "test"), (2, "dev")])
    severity = SelectField("严重程度：", validators=[Required(
        "Please enter")], choices=[(1, "test"), (2, "dev")])
    reproduce = SelectField("重现概率：", validators=[Required(
        "Please enter")], choices=[(1, "test"), (2, "dev")])
    date = DateField(requir + "发现时间：", validators=[Required("Please enter")])
    def values(self,issue,count,version_path,log_path):
        self.issue=issue
        self.count=count
        self.version_path=version_path
        self.log_path=log_path