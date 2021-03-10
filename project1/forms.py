from models import Fcuser
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms.validators import DataRequired,EqualTo

class RegisterForm(FlaskForm):
    '''회원가입'''
    userid = StringField('userid', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired() , EqualTo('repassword')])
    repassword = PasswordField('repassword', validators=[DataRequired()])

class LoginForm(FlaskForm):
    '''로그인'''
    class UserPassword(object):
        '''비밀번호 맞는지 확인 하는 클래스'''
        def __init__(self, message=None):
            self.message = message 
        
        def __call__(self, form ,field):
            userid = form['userid'].data
            password = field.data

            fcuser = Fcuser.query.filter_by(userid=userid).first()
            if fcuser.password != password:
                raise ValueError('Wrong password')

    userid = StringField('userid', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), UserPassword()])

