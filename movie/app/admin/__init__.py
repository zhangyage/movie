# -*- coding:utf-8 -*-

from flask import Blueprint   
admin = Blueprint("admin",__name__)
#导入蓝图定义蓝图
import app.admin.views