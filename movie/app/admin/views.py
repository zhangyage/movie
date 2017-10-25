#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @视图处理模块
'''
from . import  admin
from flask import render_template,url_for,redirect,flash,session,request
from app.admin.forms import LoginForm,TagForm
from app.models import Admin,Tag
from functools import wraps
from app import db

#装饰器 验证是否登录
def check_login(f):
    @wraps(f)
    def decorated_functions(*args,**kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login", next=request.url))
        return f(*args,**kwargs)
    return decorated_functions


@admin.route("/")
@check_login
def index():
    return render_template("admin/index.html")

#退出
@admin.route("/logout/")
@check_login
def logout():
    session.pop("admin",None)   #删除登录信息使我们的登录回到最初状态
    print session
    return redirect( url_for("admin.login"))

#登录
@admin.route("/login/",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        #print data
        admin = Admin.query.filter_by(name=data["account"]).first()
        if not admin.check_pwd(data["pwd"]):
            flash("密码错误！")   #消息闪现
            return redirect(url_for("admin.login"))
        session["admin"] = data["account"]   #保存登录信息
        print session
        return redirect(request.args.get("next") or url_for("admin.index"))
    return render_template("admin/login.html",form=form)

#修改密码
@admin.route("/pwd/")
@check_login
def pwd():
    return render_template("admin/pwd.html")

#添加标签
@admin.route("/tag/add/",methods=["GET","POST"])
@check_login
def tag_add():
    form = TagForm()
    if form.validate_on_submit():
        data = form.data
        tag = Tag.query.filter_by(name=data["name"]).count() #不可以有重复标签
        if tag == 1:
            flash("标签已存在！",'err')
            return redirect(url_for('admin.tag_add'))
        tag = Tag(
            name=data["name"]
        )
        db.session.add(tag)   #添加数据
        db.session.commit()   #提交数据
        flash("添加标签成功！", "OK")
        redirect(url_for('admin.tag_add'))
    return render_template("admin/tag_add.html",form=form)

#标签列表
@admin.route("/tag/list/<int:page>/",methods=["GET"])
@check_login
def tag_list(page=None):
    if page is None:
        page = 1
    page_data = Tag.query.order_by(
        Tag.addtime.desc()
    ).paginate(page=page, per_page=1)   #paginate分页 (page页码,per_page条目数)
    print page_data
    return render_template("admin/tag_list.html",page_data=page_data)


@admin.route("/movie/add/")
@check_login
def movie_add():
    return render_template("admin/movie_add.html")

@admin.route("/movie/list/")
@check_login
def movie_list():
    return render_template("admin/movie_list.html")

@admin.route("/preview/add/")
@check_login
def preview_add():
    return render_template("admin/preview_add.html")

@admin.route("/preview/list/")
@check_login
def preview_list():
    return render_template("admin/preview_list.html")

@admin.route("/user/list/")
@check_login
def user_list():
    return render_template("admin/user_list.html")

@admin.route("/user/view/")
@check_login
def user_view():
    return render_template("admin/user_view.html")

@admin.route("/comment/list/")
@check_login
def comment_list():
    return render_template("admin/comment_list.html")

@admin.route("/moviecol/list/")
@check_login
def moviecol_list():
    return render_template("admin/moviecol_list.html")

@admin.route("/oplog/list/")
@check_login
def oplog_list():
    return render_template("admin/oplog_list.html")

@admin.route("/adminloginlog/list/")
@check_login
def adminloginlog_list():
    return render_template("admin/adminloginlog_list.html")

@admin.route("/moviecol/list/")
@check_login
def userloginlog_list():
    return render_template("admin/userloginlog_list.html")

@admin.route("/auth/add/")
@check_login
def auth_add():
    return render_template("admin/auth_add.html")

@admin.route("/auth/list/")
@check_login
def auth_list():
    return render_template("admin/auth_list.html")

@admin.route("/role/add/")
@check_login
def role_add():
    return render_template("admin/role_add.html")

@admin.route("/role/list/")
@check_login
def role_list():
    return render_template("admin/role_list.html")

@admin.route("/admin/add/")
@check_login
def admin_add():
    return render_template("admin/admin_add.html")

@admin.route("/admin/list/")
@check_login
def admin_list():
    return render_template("admin/admin_list.html")



