#!/usr/bin/env python
# coding:utf-8


# from .. import db

# class Jiralist(db.Model):
#   """docstring for Jiralist"""
#   __tablename__ = "j_issues_list"
#   pid = db.Column(db.Integer,primary_key=True)
#   issuetype = db.Column(db.String(50))
#   summary = db.Column(db.String(50))
#   description = db.Column(db.String(500))
#   versiontype = db.Column(db.String(50))
#   field = db.Column(db.String(50))
#   module = db.Column(db.String(50))
#   assignee = db.Column(db.String(50))
#   versions = db.Column(db.String(50))
#   severity = db.Column(db.String(50))
#   reproduce = db.Column(db.String(50))
#   f_date = db.Column(db.DateTime)
#   delete_flag = db.Column(db.SmallInteger)
#   raw_add_time = db.Column(db.DateTime)
#   raw_update_time = db.Column(db.DateTime)

#   def __init__(self,pid,issuetype,summary,description,versiontype,field,module,assignee,versions,severity,reproduce,f_date,delete_flag=0,raw_add_time=None,raw_update_time=None):
#       self.pid=pid
#       self.issuetype=issuetype
#       self.summary=summary
#       self.description=description
#       self.versiontype=versiontype
#       self.field=field
#       self.module=module
#       self.assignee=assignee
#       self.versions=versions
#       self.severity=severity
#       self.reproduce=reproduce
#       self.f_date=f_date
#       self.delete_flag=delete_flag
#       self.raw_add_time=raw_add_time
#       self.raw_update_time=raw_update_time

#   def __repr__(self):
#       return "<Role %r>"%self.name
