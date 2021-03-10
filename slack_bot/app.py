from flask import Flask
from api_v1 import api as api_v1
from flask import request , redirect , render_template , session
from models import db, Fcuser
import os
from forms import RegisterForm,LoginForm
app = Flask(__name__)
app.register_blueprint(api_v1 , url_prefix='/api/v1')


@app.route('/', methods=['GET'])
def home():
    userid = session.get('userid', None)
    return render_template('home.html',userid=userid)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['userid'] = form.data.get('userid')
        return redirect('/')

    return render_template('login.html',form=form)

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('userid',None)
    return redirect('/')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        fcuser = Fcuser()
        fcuser.userid =form.data.get('userid')
        fcuser.password =form.data.get('password')

        # print(fcuser.userid,fcuser.password)
        db.session.add(fcuser)
        db.session.commit()
        # return render_template('login.html',form=form)
        # print('zjtla')

    return render_template('register.html',form=form)

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True ## 트렌젝션 하나의 요청을 할때마다 커밋 됨 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False ## 수정사항에 대한 트랜젝션을 하겠다. ( 최신버전에선 러닝 메세지 나오니 설정해주기 )
app.config['SECRET_KEY'] = 'qkwejweijweiojfwejp1ff22f2332efwjo'

db.init_app(app)
db.app = app
db.create_all()

if __name__ == '__main__':

    app.run(host='127.0.0.1' , port=5000 , debug=True)
