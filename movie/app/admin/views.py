#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @视图处理模块
'''
from . import  admin
from flask import render_template,url_for,redirect

@admin.route("/")
def index():
    return "<h1 style='color:red'>this is admin</h1>"

@admin.route("/logout/")
def logout():
    return redirect( url_for("admin.login"))

@admin.route("/login/")
def login():
    return render_template("admin/login.html")