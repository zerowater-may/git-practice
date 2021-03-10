from models import Fcuser
from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField
from wtforms.validators import DataRequired, EqualTo

class RegisterForm(FlaskForm):

    userid = StringField('userid', validators=[DataRequired()])
    password = PasswordField('passowrd', validators=[DataRequired()])
    repassword = PasswordField('repassword', validators=[DataRequired()])

class LoginForm(FlaskForm):  

    class UserPassword(object):
        def __init__(self,message=None):
            self.message = message

        def __call__(self, form ,field):
            userid = form['userid'].data
            password = field.data

            fcuser = Fcuser.query.filter_by(userid=userid).first()
            print(fcuser,'<<<<<<<')
            if fcuser.password != password:
                raise ValueError('Wrong Password')

    userid = StringField('userid', validators=[DataRequired()])
    password = PasswordField('passowrd', validators=[DataRequired()])
    