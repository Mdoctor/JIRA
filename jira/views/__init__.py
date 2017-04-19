#!/usr/bin/env python
#-*-coding:utf-8-*-

from flask import Blueprint

app = Blueprint("view",__name__)

from . import view,error