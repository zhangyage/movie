#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @视图处理模块
'''
from . import  admin
from flask import render_template,url_for,redirect,flash,session,request
from app.admin.forms import LoginForm,TagForm,MovieForm,PreviewForm
from app.models import Admin,Tag,User,Adminlog,Auth,Role,Preview,Oplog,Movie,Moviecol,Comment
from functools import wraps
from app import db,app
from werkzeug.utils import secure_filename
import os
import uuid
import datetime

#装饰器 验证是否登录
def check_login(f):
    @wraps(f)
    def decorated_functions(*args,**kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login", next=request.url))
        return f(*args,**kwargs)
    return decorated_functions


#修改文件名称
def change_filename(filename):
    fileinfo = os.path.splitext(filename) #分割文件名后缀和前缀
    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S")+str(uuid.uuid4().hex)+fileinfo[-1]
    return filename


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
        Tag.addtime.asc()
    ).paginate(page=page, per_page=10)   #paginate分页 (page页码,per_page条目数)
    return render_template("admin/tag_list.html",page_data=page_data)


#删除标签
@admin.route("/tag/del/<int:id>/",methods=["GET"])
@check_login
def tag_del(id=None):
    tag=Tag.query.filter_by(id=id).first_or_404()   #如果没有返回404
    db.session.delete(tag)
    db.session.commit()
    flash("删除标签成功", "OK")
    return redirect(url_for('admin.tag_list',page=1))


#更新标签
@admin.route("/tag/update/<int:id>/",methods=["GET","POST"])
@check_login
def tag_update(id):
    form = TagForm()
    tag = Tag.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        tag_count = Tag.query.filter_by(name=data["name"]).count() #不可以有重复标签
        if tag.name != data["name"] and tag_count == 1:
            flash("标签已经存在！",'err')
            return redirect(url_for('admin.tag_update',id=id))
        tag.name = data["name"]       #修改数据
        db.session.add(tag)   #添加修改数据
        db.session.commit()   #提交数据
        flash("修改标签成功！", "OK")
        redirect(url_for('admin.tag_update',id=id))
    return render_template("admin/tag_update.html",form=form,tag=tag)
    

#添加电影
@admin.route("/movie/add/",methods=["GET","POST"])
@check_login
def movie_add():
    form = MovieForm()
    if form.validate_on_submit():
        data = form.data
        movie_count = Movie.query.filter_by(title=data["title"]).count() #不可以有重复标签
        if movie_count == 1:
            flash("对应的影片已存在！",'err')
            return redirect(url_for('admin.preview_add'))
        file_url = secure_filename(form.url.data.filename)
        file_logo = secure_filename(form.logo.data.filename)
        '''form.logo.data.filename  获取上传文件文件名'''
        if not os.path.exists(app.config["UP_DIR"]):  #判断长传目录是否存在
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"], "rw")
        url = change_filename(file_url)   #修改为安全的名称
        logo = change_filename(file_logo)
        form.url.data.save(app.config["UP_DIR"] + url)  #保存文件
        form.logo.data.save(app.config["UP_DIR"] + logo)
        movie = Movie(
            title = data["title"],
            url = url,
            info = data["info"],
            logo = logo,
            star = int(data["star"]),
            playnum = 0,
            commentnum = 0,
            tag_id = int(data["tag_id"]),
            area = data["area"],
            release_time = data["release_time"],
            length = data["length"]
            )
        db.session.add(movie)
        db.session.commit()
        flash("添加电影成功",'OK')
        return redirect(url_for('admin.movie_add'))
    return render_template("admin/movie_add.html",form=form)


#电影列表
@admin.route("/movie/list/<int:page>",methods=["GET"])
@check_login
def movie_list(page = None):
    if page is None:
        page = 1
    page_data = Movie.query.join(Tag).filter(Tag.id == Movie.tag_id).order_by(
        Movie.addtime.asc()
    ).paginate(page=page, per_page=1)   #paginate分页 (page页码,per_page条目数)
    return render_template("admin/movie_list.html",page_data=page_data)


#删除电影
@admin.route("/movie/del/<int:id>/",methods=["GET"])
@check_login
def movie_del(id=None):
    movie=Movie.query.filter_by(id=id).first_or_404()   #如果没有返回404
    db.session.delete(movie)
    db.session.commit()
    flash("删除标签成功", "OK")
    return redirect(url_for('admin.movie_list',page=1))


#修改电影
@admin.route("/movie/update/<int:id>/",methods=["GET","POST"])
@check_login
def movie_update(id):
    form = MovieForm()
    form.url.validators = []   #不修改这个值，直接设置为空
    form.logo.validators = []
    movie = Movie.query.get_or_404(id)
    if request.method == "GET":
        form.info.data = movie.info
        form.tag_id.data = movie.tag_id
        form.star.data = movie.star
    if form.validate_on_submit():
        data = form.data
        movie_count = Movie.query.filter_by(title=data["title"]).count()
        if movie_count == 1 and movie.title != data["title"]:
            flash("修改失败",'err')
            return redirect(url_for('admin.movie_update',id=id))
        
        if form.url.data.filename != "":   #判断我们是否更改图片了  空就是没有更改
            file_url = secure_filename(form.url.data.filename)
            movie.url = change_filename(file_url)  
            form.url.data.save(app.config["UP_DIR"] + movie.url)  
        if form.logo.data.filename != "":
            file_logo = secure_filename(form.logo.data.filename)
            movie.logo = change_filename(file_logo)
            form.logo.data.save(app.config["UP_DIR"] + movie.logo)
        
        movie.title = data["title"]
        movie.info = data["info"]
        movie.star = data["star"]
        movie.tag_id = data["tag_id"]
        movie.area = data["area"]
        movie.release_time = data["release_time"]
        movie.length = data["length"]
        db.session.add(movie)
        db.session.commit()
        flash("修改电影成功",'OK')
        return redirect(url_for('admin.movie_update',id=id))
    return render_template("admin/movie_update.html",form=form,movie=movie)  #movie=movie传进初始值，方便我们参考修改


#预告添加
@admin.route("/preview/add/",methods=["GET","POST"])
@check_login
def preview_add():
    form = PreviewForm()
    if form.validate_on_submit():
        data = form.data
        preview_count = Preview.query.filter_by(title=data["title"]).count() #不可以有重复标签
        if preview_count == 1:
            flash("对应的预告已存在！",'err')
            return redirect(url_for('admin.preview_add'))
        file_logo = secure_filename(form.logo.data.filename)
        '''form.logo.data.filename  获取上传文件文件名'''
        if not os.path.exists(app.config["UP_DIR"]):  #判断长传目录是否存在
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"], "rw")
        logo = change_filename(file_logo)
        form.logo.data.save(app.config["UP_DIR"] + logo)
        preview = Preview(
            title = data["title"],
            logo = logo
            )
        db.session.add(preview)
        db.session.commit()
        flash("预告电影添加成功",'OK')
        return redirect(url_for('admin.preview_add'))
    return render_template("admin/preview_add.html",form = form)

#预告列表
@admin.route("/preview/list/<int:page>/",methods=["GET"])
@check_login
def preview_list(page=None):
    if page is None:
        page = 1
    page_data = Preview.query.filter_by().order_by(
        Preview.addtime.asc()
    ).paginate(page=page, per_page=10)   #paginate分页 (page页码,per_page条目数)
    return render_template("admin/preview_list.html",page_data=page_data)

#删除预告
@admin.route("/preview/del/<int:id>/",methods=["GET"])
@check_login
def preview_del(id=None):
    preview=Preview.query.filter_by(id=id).first_or_404()   #如果没有返回404
    db.session.delete(preview)
    db.session.commit()
    flash("删除预告成功", "OK")
    return redirect(url_for('admin.preview_list',page=1))


#修改预告电影
@admin.route("/preview/update/<int:id>/",methods=["GET","POST"])
@check_login
def preview_update(id):
    form = PreviewForm()
    form.logo.validators = []   #不修改这个值，直接设置为空
    preview = Preview.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        preview_count = Preview.query.filter_by(title=data["title"]).count()
        if preview_count == 1 and preview.title != data["title"]:
            flash("修改失败！对应的预告片已经存在",'err')
            return redirect(url_for('admin.preview_update',id=id))
        if form.logo.data.filename != "": #判断我们是否更改图片了  空就是没有更改
            file_logo = secure_filename(form.logo.data.filename)
            preview.logo = change_filename(file_logo)
            form.logo.data.save(app.config["UP_DIR"] + preview.logo)
        
        preview.title = data["title"]
        db.session.add(preview)
        db.session.commit()
        flash("预告电影修改成功",'OK')
        return redirect(url_for('admin.preview_update',id=id))
    return render_template("admin/preview_update.html",form=form,preview=preview)  #movie=movie传进初始值，方便我们参考修改


#会员列表
@admin.route("/user/list/<int:page>/",methods=["GET"])
@check_login
def user_list(page=None):
    if page is None:
        page = 1
    page_data = User.query.filter_by().order_by(
        User.addtime.asc()
    ).paginate(page=page, per_page=10)   #paginate分页 (page页码,per_page条目数)
    return render_template("admin/user_list.html",page_data=page_data)


#会员查看
@admin.route("/user/view/<int:id>",methods=["GET"])
@check_login
def user_view(id=None):
    user = User.query.get_or_404(int(id))
    return render_template("admin/user_view.html",user=user)


#删除会员
@admin.route("/user/del/<int:id>/",methods=["GET"])
@check_login
def user_del(id=None):
    user=User.query.filter_by(id=id).first_or_404()   #如果没有返回404
    db.session.delete(user)
    db.session.commit()
    flash("删除预告成功", "OK")
    return redirect(url_for('admin.user_list',page=1))


#评论列表
@admin.route("/comment/list/<int:page>",methods=["GET"])
@check_login
def comment_list(page=None):
    if page is None:
        page = 1
    page_data = Comment.query.join(
            Movie
        ).join(
            User
        ).filter(
           Movie.id == Comment.movie_id,
           User.id == Comment.user_id 
        ).order_by(
        Comment.addtime.asc()
    ).paginate(page=page, per_page=10)   #paginate分页 (page页码,per_page条目数)
    return render_template("admin/comment_list.html",page_data=page_data)


#删除评论
@admin.route("/comment/del/<int:id>/",methods=["GET"])
@check_login
def comment_del(id=None):
    comment=Comment.query.filter_by(id=id).first_or_404()   #如果没有返回404
    db.session.delete(comment)
    db.session.commit()
    flash("评论删除成功", "OK")
    return redirect(url_for('admin.comment_list',page=1))

#电影收藏列表
@admin.route("/moviecol/list/<int:page>",methods=["GET"])
@check_login
def moviecol_list(page=None):
    if page is None:
        page = 1
    page_data = Moviecol.query.join(
            Movie
        ).join(
            User
        ).filter(
           Movie.id == Moviecol.movie_id,
           User.id == Moviecol.user_id 
        ).order_by(
       Moviecol.addtime.asc()
    ).paginate(page=page, per_page=10)   #paginate分页 (page页码,per_page条目数)
    return render_template("admin/moviecol_list.html",page_data=page_data)


#删除电影收藏
@admin.route("/moviecol/del/<int:id>/",methods=["GET"])
@check_login
def moviecol_del(id=None):
    moviecol=Moviecol.query.filter_by(id=id).first_or_404()   #如果没有返回404
    db.session.delete(moviecol)
    db.session.commit()
    flash("收藏电影删除成功", "OK")
    return redirect(url_for('admin.moviecol_list',page=1))

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



