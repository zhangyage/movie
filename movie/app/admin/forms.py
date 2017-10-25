#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @表单处理
'''
from flask_wtf import FlaskForm
from wtforms import TextField,PasswordField,validators,StringField,SubmitField
from wtforms.validators import DataRequired,ValidationError
from app.models import Admin


#用户登录验证
class LoginForm(FlaskForm):
    '''管理员登陆表单'''
    account = StringField(label=u"账号",
                          validators=[DataRequired('请输入账号')],  #设置为必填项目
                          description=u"账号",
                          render_kw={"class":"form-control",
                                     "placeholder":u"请输入账号！",
                                     #"required":"required"     #html提示不能为空
                              }
                          )
    pwd = PasswordField(label=u"密码",
                          validators=[DataRequired('请输入密码')],  
                          description=u"密码",
                          render_kw={"class":"form-control",
                                     "placeholder":u"请输入密码！",
                                     #"required":"required"
                              }
                          )
    
    submit = SubmitField(label=u"登陆",
                         render_kw={"class":"btn btn-primary btn-block btn-flat",
                              }
                          )
    
    def validate_account(self,field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError("账号不存在")
        
#电影标签添加
class TagForm(FlaskForm):
    '''电影添加表单'''
    name = StringField(label=u"电影标签",
                          validators=[DataRequired(u'请输入要添加的标签')],  #设置为必填项目
                          description=u"电影标签",
                          render_kw={"class":"form-control", 
                                     "id":"input_name", 
                                     "placeholder":u"请输入标签名称！",
                                     #"required":"required"     #html提示不能为空
                              }
                          )
    
    submit = SubmitField(label=u"添加",
                         render_kw={"class":"btn btn-primary",
                              }
                          )
        
    
    
    