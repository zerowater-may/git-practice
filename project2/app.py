import os
from flask import Flask
from flask_jwt import JWT ## JQUERY 토큰 
from flask import render_template
from api_v1 import api as api_v1
from models import db , Fcuser


app = Flask(__name__)
app.register_blueprint(api_v1 , url_prefix='/api/v1') ## api 등록하기 


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/')
def hello():
    return render_template('home.html')


basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True ## 트렌젝션 하나의 요청을 할때마다 커밋 됨 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False ## 수정사항에 대한 트랜젝션을 하겠다. ( 최신버전에선 러닝 메세지 나오니 설정해주기 )
app.config['SECRET_KEY'] = 'qkwejweijweiojfwejp1ff22f2332efwjo'

# csrf = CSRFProtect()
# csrf.init_app(app)

db.init_app(app) ## 앱 초기화
db.app = app
db.create_all()

## JWT 토큰 ## 
def authenticate(username, password):
    user = Fcuser.query.filter(Fcuser.userid==username).first()
    if user.password == password:
        return user


'''토큰을 유저정보로 변환하는 함수'''
def identity(payload):
    userid = payload['identity']
    return Fcuser.query.filter(Fcuser.id==userid).first()

## 토큰을 JQUERY 쿠키에 담음 
jwt = JWT(app, authenticate , identity) ## 인증하는 함수 



## AJAX , JQUERY 비동기 

if __name__ == '__main__':
     app.run(host='127.0.0.1', port=5000, debug=True)