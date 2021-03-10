from flask import jsonify
from . import api
from flask import request
from models import Fcuser,db
from flask import session

@api.route('/users', methods=['GET','POST'])
def users():
    if request.method == 'POST':
        userid = request.form.get('userid')
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re_password')
        
        print(userid,username,password,re_password)
        if not (userid and username and password and re_password):
            return jsonify({'error':'No arguments'}), 400

        if password != re_password:
            return jsonify({'error':'Wrong password'}), 400

        fcuser = Fcuser()
        fcuser.userid = userid
        fcuser.username = username
        fcuser.password = password
        ## 값이 안들어감 
        db.session.add(fcuser)
        db.session.commit()

        return jsonify(), 201

    users = Fcuser.query.all() ## 디비에 모든 값 
    return jsonify([user.serialize for user in users])

@api.route('/users/<uid>', methods=['GET','PUT','DELETE'])
def user_detail(uid):
    if request.method == 'GET':
        user = Fcuser.query.filter(Fcuser.id==uid).first()
        return jsonify(user.serialize)