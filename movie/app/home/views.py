#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @视图处理模块
'''
from . import  home
from flask import render_template,redirect,url_for,session,flash,request
from app.home.forms import RegistForm,LoginForm,UserForm,PwdForm,CommentForm
from app.models import User,Userlog,Comment,Movie,Moviecol,Preview,Tag
from functools import wraps
from werkzeug.utils import secure_filename
from app import db,app
from app.plugins import IP_addr
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

@home.route("/<int:page>/",methods=["GET"])
@home.route("/",methods=["GET"])
def index(page=None):
    if page is None:
        page = 1
    tags = Tag.query.all()
    page_data = Movie.query
    tid = request.args.get("tid",0)     #标签id
    if int(tid) !=0:
        page_data = page_data.filter_by(tag_id=int(tid)) 
        
    star = request.args.get("star",0)   #星级
    if int(star) !=0:
        page_data = page_data.filter_by(star=int(star)) 
           
    time = request.args.get("time",0)   #上映时间
    if int(time) !=0:
        if int(time) ==1:
            page_data = page_data.order_by(Movie.addtime.desc()) 
        else:
            page_data = page_data.order_by(Movie.addtime.asc()) 
                  
    pm = request.args.get("pm",0)       #播放量
    if int(pm) !=0:
        if int(pm) ==1:
            page_data = page_data.order_by(Movie.playnum.desc()) 
        else:
            page_data = page_data.order_by(Movie.playnum.asc())
            
    cm = request.args.get("cm",0)       #评论量
    if int(cm) !=0:
        if int(cm) ==1:
            page_data = page_data.order_by(Movie.commentnum.desc()) 
        else:
            page_data = page_data.order_by(Movie.commentnum.asc())
    
    
    #page = request.args.get("page",1)
    page_data = page_data.paginate(page=page, per_page=8)        
    p=dict(                 #通过url session传递参数
        tid=tid, 
        star=star,
        time=time,
        pm=pm, 
        cm=cm,
    )
    return render_template("home/index.html",tags=tags,p=p,page_data=page_data)


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
            ip_addr = IP_addr.use_params_requests(request.remote_addr)
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

#用户注册
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
        form.info.data = user.info
    if form.validate_on_submit():
        data = form.data
        user_count = User.query.filter_by(name=data["name"]).count()
        if user_count == 1 and user.name != data["name"]:
            flash(u"用户已存在！",'err')
            return redirect(url_for('home.user'))
        email_count = User.query.filter_by(email=data["email"]).count()
        if email_count == 1 and user.email != data["email"]:
            flash(u"邮箱已存在！",'err')
            return redirect(url_for('home.user'))
        phone_count = User.query.filter_by(phone=data["phone"]).count()
        if phone_count == 1 and user.phone != data["phone"]:
            flash(u"手机号码已存在！",'err')
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

@home.route("/pwd/",methods=["GET","POST"])
@check_login
def pwd():
    form = PwdForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=session["user"]).first()
        from werkzeug.security import generate_password_hash    #导入加密模块
        user.pwd = generate_password_hash(data["new_pwd"])
        db.session.add(user)
        db.session.commit()
        flash(u"密码修改成功,请重新登录", "OK")
        return redirect(url_for('home.logout'))
    return render_template("home/pwd.html",form=form)


#评论
@home.route("/comments/<int:page>",methods=["GET"])
@check_login
def comments(page=None):
    if page is None:
        page = 1
    page_data = Comment.query.join(
        Movie
        ).join(
        User
        ).filter(
            Comment.movie_id == Movie.id,
            User.id == session["user_id"]
    ).order_by(
       Comment.addtime.desc()
    ).paginate(page=page, per_page=10)   #paginate分页 (page页码,per_page条目数)
    return render_template("home/comments.html",page_data=page_data)

#电影收藏添加
@home.route("/moviecol/add/",methods=["GET"])
@check_login
def moviecol_add():
    uid = request.args.get("uid","")
    mid = request.args.get("mid","")
    moviecol=Moviecol.query.filter_by(
        user_id=int(uid),
        movie_id=int(mid)
    ).count()
    if moviecol == 1:
        data = dick(ok=0)
    
    if moviecol == 0:
        moviecol = Moviecol(
            user_id=int(uid),
            movie_id=int(mid)
        )
        db.session.add(moviecol)
        db.session.commit()
        data = dick(ok=1)
    import json
    return json.dumps(data)

#收藏电影
@home.route("/moviecol/<int:page>",methods=["GET"])
@check_login
def moviecol(page=None):
    if page is None:
        page = 1
    page_data = Moviecol.query.join(
        Movie
        ).join(
        User
        ).filter(
            Moviecol.movie_id == Movie.id,
            User.id == session["user_id"]
    ).order_by(
       Moviecol.addtime.desc()
    ).paginate(page=page, per_page=10)   #paginate分页 (page页码,per_page条目数)
    return render_template("home/moviecol.html",page_data=page_data)

@home.route("/loginlog/<int:page>/",methods=["GET"])
@check_login
def loginlog(page=None):
    if page is None:
        page = 1
    page_data = Userlog.query.filter_by( 
        user_id = int(session["user_id"])
    ).order_by(
       Userlog.addtime.desc()
    ).paginate(page=page, per_page=10)   #paginate分页 (page页码,per_page条目数)
    return render_template("home/loginlog.html",page_data=page_data)

#图片轮播
@home.route("/animation/")
def animation():
    data = Preview.query.all()
    return render_template("home/animation.html",data=data)

#搜索
@home.route("/search/<int:page>",methods=["GET"])
def search(page=None):
    if page is None:
        page = 1
    key = request.args.get("key","")
    movie_count = Movie.query.filter(
        Movie.title.ilike('%' +key+ '%')
    ).count()                              #获取搜索的条目数量
    
    page_data = Movie.query.filter(
        Movie.title.ilike('%' +key+ '%')
    ).order_by(
        Movie.addtime.desc()
    ).paginate(page=page,per_page=6)
    return render_template("home/search.html",key=key,page_data=page_data,movie_count=movie_count)

@home.route("/play/<int:id>/<int:page>/",methods=["GET","POST"])
def play(id=None,page=None):
    movie = Movie.query.join(
        Tag
    ).filter(
        Movie.tag_id == Tag.id,
        Movie.id == int(id)
    ).first()                        #播放电影信息
    
    if page is None:
        page = 1
    page_data = Comment.query.join(
        Movie
    ).join(
        User
    ).filter(
        Movie.id == movie.id,
        User.id == Comment.user_id
    ).order_by(
        Comment.addtime.desc()
    ).paginate(page=page,per_page=6)    #分页内容
    
    movie.playnum = movie.playnum + 1   #播放次数添加
    form = CommentForm()
    if form.validate_on_submit():
        data = form.data
        comment = Comment(
            content = data["content"],
            movie_id = movie.id,
            user_id = session["user_id"]
        )
        db.session.add(comment)
        db.session.commit()
        movie.commentnum = movie.commentnum + 1   #评论次数添加
        db.session.add(movie)
        db.session.commit()
        flash(u"评论添加成功！","OK")
        return redirect(url_for('home.play', id=movie.id, page=1))
    db.session.add(movie)
    db.session.commit()
    
    return render_template("home/play.html",movie=movie,page_data=page_data,form=form)



@home.route("/video/<int:id>/<int:page>/", methods=["GET", "POST"])
def video(id=None, page=None):
    movie = Movie.query.join(Tag).filter(
        Tag.id == Movie.tag_id,
        Movie.id == int(id)
    ).first_or_404()

    if page is None:
        page = 1
    page_data = Comment.query.join(
        Movie
    ).join(
        User
    ).filter(
        Movie.id == movie.id,
        User.id == Comment.user_id
    ).order_by(
        Comment.addtime.desc()
    ).paginate(page=page, per_page=10)

    movie.playnum = movie.playnum + 1
    form = CommentForm()
    if "user" in session and form.validate_on_submit():
        data = form.data
        comment = Comment(
            content=data["content"],
            movie_id=movie.id,
            user_id=session["user_id"]
        )
        db.session.add(comment)
        db.session.commit()
        movie.commentnum = movie.commentnum + 1
        db.session.add(movie)
        db.session.commit()
        flash("添加评论成功！", "ok")
        return redirect(url_for('home.video', id=movie.id, page=1))
    db.session.add(movie)
    db.session.commit()
    return render_template("home/video.html", movie=movie, form=form, page_data=page_data)





@home.route("/tm/", methods=["GET", "POST"])
def tm():
    import json
    if request.method == "GET":
        #获取弹幕消息队列
        id = request.args.get('id')
        key = "movie" + str(id)
        if rd.llen(key):
            msgs = rd.lrange(key, 0, 2999)
            res = {
                "code": 1,
                "danmaku": [json.loads(v) for v in msgs]
            }
        else:
            res = {
                "code": 1,
                "danmaku": []
            }
        resp = json.dumps(res)
    if request.method == "POST":
        #添加弹幕
        data = json.loads(request.get_data())
        msg = {
            "__v": 0,
            "author": data["author"],
            "time": data["time"],
            "text": data["text"],
            "color": data["color"],
            "type": data['type'],
            "ip": request.remote_addr,
            "_id": datetime.datetime.now().strftime("%Y%m%d%H%M%S") + uuid.uuid4().hex,
            "player": [
                data["player"]
            ]
        }
        res = {
            "code": 1,
            "data": msg
        }
        resp = json.dumps(res)
        rd.lpush("movie" + str(data["player"]), json.dumps(msg))
    return Response(resp, mimetype='application/json')
