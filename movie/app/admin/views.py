#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @视图处理模块
'''
from . import  admin

@admin.route("/")
def index():
    return "<h1 style='color:red'>this is admin</h1>"