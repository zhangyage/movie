#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @入口脚本文件
'''
from app import  app

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int("80"))