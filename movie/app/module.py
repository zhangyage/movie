#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
     @存放数据模型
     @配置参考：http://www.pythondoc.com/flask-sqlalchemy/
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://zhangyage:Zhang123@47.94.188.237/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

#会员信息
class User(db.Model):
    __tablename__ = "user"   #表名称
    id = db.Column(db.Integer, primary_key=True) #编号
    name = db.Column(db.String(100),unique=True) #名称
    pwd = db.Column(db.String(100))              #密码
    email = db.Column(db.String(100),unique=True)#邮箱
    phone = db.Column(db.String(100),unique=True)#电话
    info = db.Column(db.Text)                    #个性简介               
    face = db.Column(db.String(255),unique=True)   #图像   
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow) #注册时间
    uuid = db.Column(db.String(255),unique=True)   #唯一标志符
    userlogs = db.relationship('Userlog',backref='user') #会员日志外键关系关联
    comments = db.relationship('Comment',backref='user') #评论外键关系关联
    moviecols = db.relationship('Moviecol',backref='user') #电影收藏外键关系关联
    
    def __repr__(self):
        return "<User %r>" % self.name
    
#会员登录日志：
class Userlog(db.Model):
    __tablename__ = "userlog"   #表名称
    id = db.Column(db.Integer, primary_key=True) #编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  #外键关系绑定
    ip = db.Column(db.String(100))    #登录ip
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow) #登录时间
   
    def __repr__(self):
        return "<Userlog %r>" % self.id
    
#标签
class Tag(db.Model):
    __tablename__ = "tag"   #表名称
    id = db.Column(db.Integer, primary_key=True) #编号
    name = db.Column(db.String(100),unique=True) #标题
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow) #添加时间
    movies = db.relationship('Movie',backref='tag') #电影外键关系关联
    
    
    def __repr__(self):
        return "<Tag %r>" % self.name 
    
#电影
class Movie(db.Model):
    __tablename__ = "movie"   #表名称
    id = db.Column(db.Integer, primary_key=True) #编号
    title = db.Column(db.String(255),unique=True) #标题
    url = db.Column(db.String(255),unique=True) #播放地址
    info = db.Column(db.Text) #电影描述
    logo = db.Column(db.String(255),unique=True) #logo
    star = db.Column(db.SmallInteger) #星级
    playnum = db.Column(db.BigInteger) #播放次数
    commentnum = db.Column(db.BigInteger) #评论测试
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))  #外键关系绑定  标签
    area = db.Column(db.String(255)) #上营区域
    release_time = db.Column(db.Date) #上映时间
    length = db.Column(db.String(100)) #播放时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow) #添加时间
    comments = db.relationship('Comment',backref='movie') #评论外键关系关联
    moviecols = db.relationship('Moviecol',backref='movie') #电影收藏外键关系关联
    
    def __repr__(self):
        return "<Movie %r>" % self.title
    
#电影预告
class Preview(db.Model):
    __tablename__ = "preview"   #表名称
    id = db.Column(db.Integer, primary_key=True) #编号
    title = db.Column(db.String(255),unique=True) #标题
    logo = db.Column(db.String(255),unique=True) #logo
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow) #添加时间
    
    def __repr__(self):
        return "<Preview %r>" % self.title
    
#评论
class Comment(db.Model):
    __tablename__ = "comment"   #表名称
    id = db.Column(db.Integer, primary_key=True) #编号
    content = db.Column(db.Text) #评论内容
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  #所属电影
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))    #所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow) #添加时间
    
    def __repr__(self):
        return "<Comment %r>" % self.id
    
#电影收藏
class Moviecol(db.Model):
    __tablename__ = "moviecol"   #表名称
    id = db.Column(db.Integer, primary_key=True) #编号
    content = db.Column(db.Text) #内容
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  #所属电影
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))    #所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow) #添加时间
    
    def __repr__(self):
        return "<Moviecol %r>" % self.id


#权限
class Auth(db.Model):
    __tablename__ = "auth"   #表名称
    id = db.Column(db.Integer, primary_key=True) #编号
    name = db.Column(db.String(255),unique=True) #名称
    url = db.Column(db.String(255),unique=True)  #地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow) #添加时间
    
    def __repr__(self):
        return "<Auth %r>" % self.name   
    
#角色
class Role(db.Model):
    __tablename__ = "role"   #表名称
    id = db.Column(db.Integer, primary_key=True) #编号
    name = db.Column(db.String(255),unique=True) #名称
    auths = db.Column(db.String(600)             #权限列表
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow) #添加时间
     
    def __repr__(self):
        return "<Role %r>" % self.name   