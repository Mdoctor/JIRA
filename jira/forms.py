#!/usr/bin/env python
# coding:utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired


class JiraSubmit(FlaskForm):
    requir = "<strong style=\"color:red\">* </strong>"
    pid = SelectField("项目：", validators=[DataRequired(
        "Please enter")], coerce=str, choices=[("ROM", "ROM"), ("POLLUX", "POLLUX")])
    issuetype = StringField(
        requir + "问题类型：", validators=[DataRequired("Please enter")],default="缺陷")
    summary = StringField(
            requir + "主题：", validators=[DataRequired("Please enter")])
    description = TextAreaField(
        requir + "描述：", validators=[DataRequired("Please enter")])
    versiontype = SelectField("版本类型：",coerce=int, validators=[DataRequired(
        "Please enter")], choices=[(1, "test"), (2, "dev")])
    field = SelectField("领域：",coerce=int, validators=[DataRequired(
        "Please enter")], choices=[(1, "test"), (2, "dev")])
    module = SelectField("模块：",coerce=int, validators=[DataRequired(
        "Please enter")], choices=[(1, "test"), (2, "dev")])
    assignee = SelectField("处理人：",coerce=int, validators=[DataRequired(
        "Please enter")], choices=[(1, "test"), (2, "dev")])
    versions = SelectField("影响版本：",coerce=int, validators=[DataRequired(
        "Please enter")], choices=[(1, "test"), (2, "dev")])
    severity = SelectField("严重程度：",coerce=int, validators=[DataRequired(
        "Please enter")], choices=[(1, "test"), (2, "dev")])
    reproduce = SelectField("重现概率：",coerce=int, validators=[DataRequired(
        "Please enter")], choices=[(1, "test"), (2, "dev")])
    date = DateField(requir + "发现时间：", validators=[DataRequired("Please enter")])
