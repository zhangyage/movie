#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @视图处理模块
'''
from . import  home
from flask import render_template,redirect,url_for,session,flash,request
from app.home.forms import RegistForm,LoginForm,UserForm
from app.models import User,Userlog
from functools import wraps
from werkzeug.utils import secure_filename
from app import db,app
import uuid
import os
import datetime


#装饰器 验证是否登录
def check_login(f):
    @wraps(f)
    def decorated_functions(*args,**kwargs):
        if "user" not in session:
            return redirect(url_for("home.login", next=request.url))
        return f(*args,**kwargs)
    return decorated_functions


#修改文件名称
def change_filename(filename):
    fileinfo = os.path.splitext(filename) #分割文件名后缀和前缀
    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S")+str(uuid.uuid4().hex)+fileinfo[-1]
    return filename

@home.route("/")
def index():
    return render_template("home/index.html")


#会员注册
@home.route("/login/",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=data["name"]).first()
        if not user.check_pwd(data["pwd"]):
            flash(u"密码错误！","err")   #消息闪现
            return redirect(url_for("home.login"))
        session["user"] = data["name"]   #保存登录信息
        session["user_id"] = user.id       #保存登录用户id,后面验证权限使用
        userlog = Userlog(                 #记录用户登录日志
            user_id=user.id,
            ip=request.remote_addr,
        )
        db.session.add(userlog)
        db.session.commit()
        return redirect(request.args.get("next") or url_for("home.index"))
    return render_template("home/login.html",form=form)

@home.route("/logout/")
def logout():
    session.pop("user",None)   #删除登录信息使我们的登录回到最初状态
    session.pop("user_id",None)
    return redirect(url_for("home.login"))

@home.route("/register/",methods=["GET","POST"])
def register():
    form = RegistForm()
    from werkzeug.security import generate_password_hash
    if form.validate_on_submit():
        data = form.data
        user = User(
            name = data["name"],
            email = data["email"],
            phone = data["phone"],
            pwd=generate_password_hash(data["pwd"]),
            uuid = uuid.uuid4().hex,
            face = uuid.uuid4().hex +'.png'
            )
        db.session.add(user)
        db.session.commit()
        flash(u"用户注册成功","OK")
    return render_template("home/register.html",form=form)

#用户中心
@home.route("/user/",methods=["GET","POST"])
@check_login
def user():
    form = UserForm()
    form.face.validators = []
    user = User.query.get_or_404(session["user_id"])
    if request.method == "GET":
        form.name.data = user.name
        form.email.data = user.email
        form.phone.data = user.phone
    if form.validate_on_submit():
        data = form.data
        user_count = User.query.filter_by(name=data["name"]).count()
        if user_count == 1 and user.name != data["name"]:
            flash(u"用户已存在！",'err')
            return redirect(url_for('home.user'))
        if form.face.data.filename != "":
            file_face = secure_filename(form.face.data.filename)
            user.face = change_filename(file_face)
            form.face.data.save(app.config["UP_DIR"]+ "users/" + user.face)
        
        user.name = data["name"]
        user.info = data["info"]
        user.email = data["email"]
        user.phone = data["phone"]
        db.session.add(user)
        db.session.commit()
        flash(u"用户信息修改成功！",'OK')
        return redirect(url_for('home.user'))
    return render_template("home/user.html",form=form,user=user)

@home.route("/pwd/")
@check_login
def pwd():
    return render_template("home/pwd.html")

@home.route("/comments/")
@check_login
def comments():
    return render_template("home/comments.html")

@home.route("/moviecol/")
@check_login
def moviecol():
    return render_template("home/moviecol.html")

@home.route("/loginlog/")
@check_login
def loginlog():
    return render_template("home/loginlog.html")

@home.route("/animation/")
def animation():
    return render_template("home/animation.html")


@home.route("/search/")
def search():
    return render_template("home/search.html")

@home.route("/play/")
def play():
    return render_template("home/play.html")


