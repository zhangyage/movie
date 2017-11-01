#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @表单处理
'''
from flask_wtf import FlaskForm
from wtforms import TextField,PasswordField,validators,StringField,SubmitField,FileField,TextAreaField,SelectField,SelectMultipleField
from wtforms.validators import DataRequired,ValidationError,EqualTo
from flask_wtf.file import file_allowed
from app.models import Admin,Tag,Auth,Role
from wtforms.fields.core import SelectField

tags = Tag.query.all()   #获取所有的标签
auth_list = Auth.query.all()   #获取所有的权限
role_list = Role.query.all()   #获取所有的角色

#用户登录验证
class LoginForm(FlaskForm):
    '''管理员登陆表单'''
    account = StringField(label=u"账号",
                          validators=[DataRequired(u'请输入账号')],  #设置为必填项目
                          description=u"账号",
                          render_kw={"class":"form-control",
                                     "placeholder":u"请输入账号！",
                                     #"required":"required"     #html提示不能为空
                              }
                          )
    pwd = PasswordField(label=u"密码",
                          validators=[DataRequired(u'请输入密码')],  
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
            raise ValidationError(u"账号不存在")
        
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
                      validators=[DataRequired(u'请上传文件'),file_allowed(['jpg', 'png'], u'Images only!')],  #设置为必填项目
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
    
        
#电影预告列表
class PreviewForm(FlaskForm):  
    '''电影预告表单'''
    title = StringField(label=u"预告标题",
                          validators=[DataRequired(u'请输入预告标题')],  #设置为必填项目
                          description=u"预告标题",
                          render_kw={"class":"form-control", 
                                     "id":"input_title", 
                                     "placeholder":u"请输入预告标题！",
                              }
                          )
    logo = FileField(label=u"预告封面",
                  validators=[DataRequired(u'请上传预告封面'),file_allowed(['jpg', 'png'], u'Images only!')],  #设置为必填项目
                  description=u"预告封面",
                  render_kw={"id":"input_logo",
                          }
                  )
    submit = SubmitField(label=u"编辑",
                 render_kw={"class":"btn btn-primary",
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
        name = session["admin"]
        admin = Admin.query.filter_by(name=name).first()
        if not admin.check_pwd(pwd):
            raise ValidationError(u"旧密码错误！")
            

#权限添加表单
class AuthForm(FlaskForm):
    '''电影添加表单'''
    name = StringField(label=u"权限名称",
                          validators=[DataRequired(u'请输入权限名称')],  #设置为必填项目
                          description=u"权限名称",
                          render_kw={"class":"form-control", 
                                     "id":"input_name", 
                                     "placeholder":u"请输入权限名称！"
                              }
                          )
    url = StringField(label=u"权限地址",
                          validators=[DataRequired(u'请输入权限地址')],  #设置为必填项目
                          description=u"电影标签",
                          render_kw={"class":"form-control", 
                                     "id":"input_url", 
                                     "placeholder":u"请输入权限地址！"
                              }
                          )
    
    submit = SubmitField(label=u"编辑",
                         render_kw={"class":"btn btn-primary",
                              }
                          )           

#角色添加表单
class RoleForm(FlaskForm):
    '''电影添加表单'''
    name = StringField(label=u"角色名称",
                          validators=[DataRequired(u'请输入角色名称')],  #设置为必填项目
                          description=u"角色名称",
                          render_kw={"class":"form-control", 
                                     "placeholder":u"请输入角色名称！"
                              }
                          )
    auths = SelectMultipleField(label=u"权限列表",
                                validators=[DataRequired(u'请选择权限列表')],
                                coerce = int,
                                choices = [(v.id,v.name) for v in auth_list],  #列表生成器生成选择
                                render_kw={"class":"form-control", 
                                     "placeholder":u'请选择权限列表'
                              })
    submit = SubmitField(label=u"编辑",
                     render_kw={"class":"btn btn-primary",
                          }
                      )  
    

#管理员表单
class AdminForm(FlaskForm):
    '''管理员登陆表单'''
    name = StringField(label=u"管理员名称",
                          validators=[DataRequired(u'请输入管理员名称')],  #设置为必填项目
                          description=u"管理员名称",
                          render_kw={"class":"form-control",
                                     "placeholder":u"请输入管理员名称！"
                              }
                          )
    pwd = PasswordField(label=u"密码",
                          validators=[DataRequired(u'请输入密码')],  
                          description=u"密码",
                          render_kw={"class":"form-control",
                                     "id":"input_pwd",
                                     "placeholder":u"请输入密码！"
                              }
                          )
    repwd = PasswordField(label=u"重复密码",
                      validators=[
                          DataRequired(u'请再次输入密码'),
                          EqualTo('pwd',message=u"两次密码不一致！")],  
                      description=u"确认密码",
                      render_kw={"class":"form-control",
                                 "id":"input_re_pwd",
                                 "placeholder":u"请再次输入密码！"
                          }
                      )
    role_id = SelectField(label=u"所属角色",
                      validators=[DataRequired(u'请选择角色')],  
                      description=u"所属角色",
                      coerce = int,
                      choices = [(v.id,v.name) for v in role_list],
                      render_kw={"class":"form-control",
                                 "placeholder":u"请选择角色！"
                          }
        )
    submit = SubmitField(label=u"登陆",
                         render_kw={"class":"btn btn-primary btn-block btn-flat",
                              }
                          )
        
