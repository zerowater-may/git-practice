import os 
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from models import db
from flask_wtf.csrf import CSRFProtect

from forms import *
from flask_sqlalchemy import SQLAlchemy
from models import Fcuser

app = Flask(__name__)


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('userid', None)
    return redirect('/')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        ## 세션 유저아이디를 세션정보에 먹임 로그인을 성공하면 로그인 세션을 저장함##
        session['userid'] = form.data.get('userid')

        return redirect('/')

    return render_template('login.html',form=form)



@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
    
        fcuser = Fcuser()
        fcuser.userid = form.data.get('userid')
        fcuser.username = form.data.get('username')
        fcuser.password = form.data.get('password')

        db.session.add(fcuser)
        db.session.commit()
        print('SUCCESS')

        return redirect('/')
    return render_template('/register.html', form=form)

@app.route('/')
def hello():
    userid = session.get('userid' , None)
    return render_template('hello.html', userid=userid)


basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True ## 트렌젝션 하나의 요청을 할때마다 커밋 됨 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False ## 수정사항에 대한 트랜젝션을 하겠다. ( 최신버전에선 러닝 메세지 나오니 설정해주기 )
app.config['SECRET_KEY'] = 'qkwejweijweiojfwejp1ff22f2332efwjo'

csrf = CSRFProtect()
csrf.init_app(app)

db.init_app(app) ## 앱 초기화
db.app = app
db.create_all()

if __name__ == '__main__':
    app.run(host='127.0.0.1' , port=5000, debug=True)


