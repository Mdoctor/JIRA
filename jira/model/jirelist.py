# !/usr/bin/env python
# coding:utf-8


from .. import db


class Jiralist(db.Model):
    """docstring for Jiralist"""
    __tablename__ = "j_issues_list"
    id = db.Column(db.INTEGER, primary_key=True)
    pid = db.Column(db.String(50))
    issuetype = db.Column(db.String(50))
    summary = db.Column(db.String(50))
    description = db.Column(db.String(500))
    versiontype = db.Column(db.String(50))
    field = db.Column(db.String(50))
    module = db.Column(db.String(50))
    assignee = db.Column(db.String(50))
    versions = db.Column(db.String(50))
    severity = db.Column(db.String(50))
    reproduce = db.Column(db.String(50))
    f_date = db.Column(db.DateTime)
    delete_flag = db.Column(db.SmallInteger)
    raw_add_time = db.Column(db.DateTime)
    raw_update_time = db.Column(db.DateTime)

    def __init__(self, pid, issuetype, summary, description, versiontype, field, module, assignee, versions, severity, reproduce, f_date):
        self.pid = pid
        self.issuetype = issuetype
        self.summary = summary
        self.description = description
        self.versiontype = versiontype
        self.field = field
        self.module = module
        self.assignee = assignee
        self.versions = versions
        self.severity = severity
        self.reproduce = reproduce
        self.f_date = f_date


    def __repr__(self):
        return "%r" % self.pid
