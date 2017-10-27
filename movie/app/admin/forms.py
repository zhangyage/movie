#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @表单处理
'''
from flask_wtf import FlaskForm
from wtforms import TextField,PasswordField,validators,StringField,SubmitField,FileField,TextAreaField,SelectField
from wtforms.validators import DataRequired,ValidationError
from app.models import Admin,Tag
from random import choice

tags = Tag.query.all()   #获取所有的标签

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
        
#标签添加表单
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
    
    submit = SubmitField(label=u"编辑",
                         render_kw={"class":"btn btn-primary",
                              }
                          )
    
    
    
    
#电影管理表单
class MovieForm(FlaskForm):
    '''电影表单'''
    title = StringField(label=u"片名",
                          validators=[DataRequired(u'请输入要添加片名')],  #设置为必填项目
                          description=u"电影片名",
                          render_kw={"class":"form-control", 
                                     "id":"input_title", 
                                     "placeholder":u"请输入片名！",
                              }
                          )
    url = FileField(label=u"文件",
                      validators=[DataRequired(u'请上传文件')],  #设置为必填项目
                      description=u"电影文件",
                      render_kw={"id":"input_url", 
                              }
                      )
    info = TextAreaField(label=u"电影简介",
                      validators=[DataRequired(u'请输入电影简介')],  #设置为必填项目
                      description=u"电影简介",
                      render_kw={"class":"form-control", 
                                 "id":"input_info",
                                 "row":10
                          }
                      )
    logo = FileField(label=u"电影封面",
                  validators=[DataRequired(u'请上传封面')],  #设置为必填项目
                  description=u"电影封面",
                  render_kw={"id":"input_logo",
                          }
                  )
    
    star = SelectField(label=u"星级",
                  validators=[DataRequired(u'请选择星级')],  #设置为必填项目
                  coerce = int,
                  choices = [(1,u"1星"),(2,u"2星"),(3,u"3星"),(4,u"4星"),(5,u"5星")],
                  
                  description=u"星级",
                  render_kw={"class":"form-control", 
                             "id":"input_star",
                          }
                  )
    
    tag_id = SelectField(label=u"标签",
                  validators=[DataRequired(u'请选择标签')],  #设置为必填项目
                  coerce = int,
                  choices = [(v.id,v.name) for v in tags],  #列表生成器生成选择 
                  description=u"标签",
                  render_kw={"class":"form-control", 
                             "id":"input_tag_id"
                          }
                  )
    area = StringField(label=u"地区",
                      validators=[DataRequired(u'请输入地区')],  #设置为必填项目
                      description=u"地区",
                      render_kw={"class":"form-control", 
                                 "id":"input_area", 
                                 "placeholder":u"请输入地区！",
                          }
                      )
    length = StringField(label=u"片长",
                      validators=[DataRequired(u'请输入片长')],  #设置为必填项目
                      description=u"电影片长",
                      render_kw={"class":"form-control", 
                                 "id":"input_length", 
                                 "placeholder":u"请输入片长！",
                          }
                      )
    release_time = StringField(label=u"上映时间",
                      validators=[DataRequired(u'请输入上映时间')],  #设置为必填项目
                      description=u"上映时间",
                      render_kw={"class":"form-control", 
                                 "id":"input_release_time", 
                                 "placeholder":u"请输入上映时间！",
                          }
                      )
    
    submit = SubmitField(label=u"编辑",
                     render_kw={"class":"btn btn-primary",
                          }
                      )
    
        
    
    
    