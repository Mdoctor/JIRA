#!/usr/bin/env python
#-*-coding:utf-8-*-

from flask import Flask, render_template 
# from flask_sqlalchemy import SQLAlchemy 
from config import config
from .model.base import Connect_mysql


def create_app(config_name):     
	app = Flask(__name__)     
	app.config.from_object(config[config_name])     
	config[config_name].init_app(app)  
	# Connect_mysql(app)
	# 附加路由和自定义的错误页面  
	from .views import app as app_blueprint 
	app.register_blueprint(app_blueprint)
	# from .model import app as model_blueprint 
	# app.register_blueprint(model_blueprint)

	return app
