#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @表单处理
'''
from flask_wtf import FlaskForm
from wtforms import TextField,PasswordField,validators,StringField,SubmitField,FileField,TextAreaField,SelectField,SelectMultipleField
from wtforms.validators import DataRequired,ValidationError,EqualTo,Email,Regexp
from flask_wtf.file import file_allowed
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


class UserForm(FlaskForm):
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
    face = FileField(label=u"头像",
                  validators=[DataRequired(u'请上传头像'),file_allowed(['jpg', 'png'], u'Images only!')],  #设置为必填项目
                  description=u"头像",
                  render_kw={"id":"input_face",
                             "class":"form-control",
                             #"name":"face",
                             #"type":"hidden"
                          }
                  )
    info = TextAreaField(label=u"个人简介",
                      validators=[DataRequired(u'请输入个人简介')],  #设置为必填项目
                      description=u"个人简介",
                      render_kw={"class":"form-control", 
                                 "id":"input_info",
                                 "style":"height:100px;",
                                 "row":30
                          }
                      )
    submit = SubmitField(label=u"保存修改",
                         render_kw={"class":" btn btn-success",
                              }
                          )

#修改密码
class PwdForm(FlaskForm):  
    '''密码修改表单'''   
    old_pwd = PasswordField(label=u"旧密码",
                  validators=[DataRequired(u'请输入旧密码')],  #设置为必填项目
                  description=u"旧密码",
                  render_kw={"class":"form-control", 
                             "id":"input_pwd",
                             "placeholder":u"请输入旧密码！",
                          }
                )
    new_pwd = PasswordField(label=u"新密码",
                  validators=[DataRequired(u'请输入新密码')],  #设置为必填项目
                  description=u"新密码",
                  render_kw={"class":"form-control", 
                             "id":"input_newpwd",
                             "placeholder":u"请输入新密码！",
                          }
                )
    submit = SubmitField(label=u"修改",
                 render_kw={"class":"btn btn-primary",
                      }
                  ) 
    def validate_old_pwd(self,field):
        from flask import  session
        pwd = field.data
        name = session["user"]
        user = User.query.filter_by(name=name).first()
        if not user.check_pwd(pwd):
            raise ValidationError(u"旧密码错误！")
        
class CommentForm(FlaskForm):
    '''提交评论'''
    content = TextAreaField(
        label=u"内容", 
        validators=[DataRequired("请输入内容：")],  
        description=u"内容", 
        render_kw={
            "id":"input_content",
            }
        ) 
    
    submit = SubmitField(label=u"提交评论",
                 render_kw={
                     "class":"btn btn-primary glyphicon glyphicon-edit",
                     "id":"btn-sub"
                      }
                  ) 