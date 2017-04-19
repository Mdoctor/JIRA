#!/usr/bin/env python
#-*-coding:utf-8-*-

from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,DateTimeField,SelectField,FileField,SubmitField,validators


class JiraFrom(FlaskForm):
	pid = SelectField("项目：", [validators.Required("Please enter")])
	issuetype = StringField("问题类型：",[validators.Required("Please enter")])
	summary = StringField("主题：",[validators.Required("Please enter")])
	description = TextAreaField("描述：",[validators.Required("Please enter")])
	versiontype = SelectField("版本类型：",[validators.Required("Please enter")])
	field = SelectField("领域：",[validators.Required("Please enter")])
	module = SelectField("模块：",[validators.Required("Please enter")])
	assignee = SelectField("处理人：",[validators.Required("Please enter")])
	versions = SelectField("影响版本：",[validators.Required("Please enter")])
	severity = SelectField("严重程度：",[validators.Required("Please enter")])
	reproduce = SelectField("重现概率：",[validators.Required("Please enter")])
	date = DateTimeField("发现时间：",[validators.Required("Please enter")])
	submit = SubmitField("提交")