#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @表单处理
'''
from flask_wtf import FlaskForm
from wtforms import Form,TextField,PasswordField,validators,StringField,SubmitField



class LoginForm(Form):
    '''管理员登陆表单'''
    account = StringField(label="账号",
                          validators=[u'请输入账号'],
                          description="账号",
                          render_kw={"class":"form-control",
                                     "placeholder":u"请输入账号！",
                                     "required":"required"
                              }
                          )
    pwd = PasswordField(label="密码",
                          validators=[u'请输入密码'],
                          description="密码",
                          render_kw={"class":"form-control",
                                     "placeholder":u"请输入密码！",
                                     "required":"required"
                              }
                          )
    
    submit = SubmitField(label=u"登陆",
                         render_kw={"class":"btn btn-primary btn-block btn-flat",
                              }
                          )
    