#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymsql://zhangyage:Zhang123@47.94.188.237/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = 'beada18cc5f146aea3902bec7a1b4a08'  #csrf跨站请求伪造
app.debug = True
db = SQLAlchemy(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint,url_prefix="/admin")


#404页面捕获使用
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')