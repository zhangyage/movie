#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @视图处理模块
'''
from . import  home
from flask import render_template,redirect,url_for

@home.route("/")
def index():
    return render_template("home/index.html")

@home.route("/login/")
def login():
    return render_template("home/login.html")

@home.route("/logout/")
def logout():
    return redirect(url_for("home.login"))

@home.route("/register/")
def register():
    return render_template("home/register.html")

