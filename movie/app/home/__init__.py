# -*- coding:utf-8 -*-

from flask import Blueprint
home = Blueprint("home",__name__)
#导入蓝图定义蓝图
import app.home.views