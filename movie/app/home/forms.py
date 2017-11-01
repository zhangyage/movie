#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @表单处理
'''
from flask_wtf import FlaskForm
from wtforms import TextField,PasswordField,validators,StringField,SubmitField,FileField,TextAreaField,SelectField,SelectMultipleField
from wtforms.validators import DataRequired,ValidationError,EqualTo,Email,Regexp
from app.models import User

class RegistForm(FlaskForm):
    '''会员注册'''
    name = StringField(label=u"昵称",
                          validators=[DataRequired(u'请输入昵称')],  #设置为必填项目
                          description=u"昵称",
                          render_kw={"class":"form-control input-lg",
                                     "placeholder":u"请输入昵称！",
                                     #"required":"required"     #html提示不能为空
                              }
                          )
    email = StringField(label=u"邮箱",
                      validators=[
                          DataRequired(u'请输入邮箱'),
                          Email(u"邮箱格式不正确！")
                          ],  #设置为必填项目
                      description=u"邮箱",
                      render_kw={"class":"form-control input-lg",
                                 "placeholder":u"请输入邮箱！",
                                 #"required":"required"     #html提示不能为空
                          }
                      )
    phone = StringField(label=u"手机",
                  validators=[
                      DataRequired(u'请输入手机号'),
                      Regexp("1[3458]\\d{9}",message=u"号码格式不正确")
                      ],  #设置为必填项目
                  description=u"手机",
                  render_kw={"class":"form-control input-lg",
                             "placeholder":u"请输入手机号！",
                             #"required":"required"     #html提示不能为空
                      }
                  )
    pwd = PasswordField(label=u"密码",
                          validators=[DataRequired(u'请输入密码')],  
                          description=u"密码",
                          render_kw={"class":"form-control input-lg",
                                     "placeholder":u"请输入密码！",
                                     #"required":"required"
                              }
                          )
    repwd = PasswordField(label=u"确认密码",
                      validators=[
                          DataRequired(u'请再次输入密码'),
                          EqualTo('pwd',message=u"两次密码不一致！")],  
                      description=u"确认密码",
                      render_kw={"class":"form-control input-lg",
                                 "id":"input_re_pwd",
                                 "placeholder":u"请再次输入密码！"
                          }
                      )
    submit = SubmitField(label=u"注册",
                         render_kw={"class":"btn btn-lg btn-success btn-block",
                              }
                          )
    
    def validate_name(self,field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 1:
            raise ValidationError(u"该昵称已经存在")
    def validate_email(self,field):
        email = field.data
        email = User.query.filter_by(email=email).count()
        if email == 1:
            raise ValidationError(u"该邮箱已经存在")
    def validate_phone(self,field):
        phone = field.data
        phone = User.query.filter_by(phone=phone).count()
        if phone == 1:
            raise ValidationError(u"该手机已经存在")
        

#会员登录        
class LoginForm(FlaskForm):
    '''会员登录'''
    name = StringField(label=u"用户名",
                          validators=[DataRequired(u'请输入用户名')],  #设置为必填项目
                          description=u"用户名",
                          render_kw={"class":"form-control input-lg",
                                     "placeholder":u"请输入昵称！",
                                     #"required":"required"     #html提示不能为空
                              }
                          )
    pwd = PasswordField(label=u"密码",
                          validators=[DataRequired(u'请输入密码')],  
                          description=u"密码",
                          render_kw={"class":"form-control input-lg",
                                     "placeholder":u"请输入密码！",
                                     #"required":"required"
                              }
                          )
    submit = SubmitField(label=u"登录",
                         render_kw={"class":"btn btn-lg btn-success btn-block",
                              }
                          )
    def validate_name(self,field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 0:
            raise ValidationError(u"账号不存在")