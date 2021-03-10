from flask import jsonify
from . import api
from flask import request
from models import Fcuser,db
from flask import session
from flask_jwt import jwt_required ## 로그인할때
import platform ,psutil
import socket

@api.route('/users', methods=['GET','POST'])
# @jwt_required() ## 로그인한사람만 보이게 인증하는것 
def users():
    if request.method == 'POST':
        data = request.get_json()
        userid = data.get('userid')
        username = data.get('username')
        password = data.get('password')
        re_password = data.get('re_password')

        ## 하드정보 
        process = platform.processor()
        memory = platform.machine()
        ram = (str(round(psutil.virtual_memory().total / (1024.0 **3))))
        hostname = (socket.gethostname())
        ip = socket.gethostbyname(socket.gethostname())
        # userid = 'thewayat'
        # username = '더웨이엣'
        # password = 'As-5520314'
        # re_password = 'As-5520314'
        # process = 'AMD64 Family 23 Model 8 Stepping 2, AuthenticAMD'
        # memory = 'AMD64'
        # ram = '16'
        # hostname = 'DESKTOP-LO08C13'
        # ip = '192.168.0.39'

        print((username, userid, password, process, memory, ram, hostname, ip))
        if not (userid and username and password and re_password):
            return jsonify({'error':'No arguments'}), 400

        if password != re_password:
            return jsonify({'error':'Wrong password'}), 400

        fcuser = Fcuser()
        fcuser.userid = userid
        fcuser.username = username
        fcuser.password = password

        fcuser.process = process
        fcuser.memory = memory
        fcuser.ram = ram
        fcuser.hostname = hostname
        fcuser.ip = ip

        ## 값이 안들어감 
        db.session.add(fcuser)
        db.session.commit()

        return jsonify(), 201

    users = Fcuser.query.all() ## 디비에 모든 값 
    # jsonify 를 하면 json 으로 변환해줌 flask 에서 
    return jsonify([user.serialize for user in users])


@api.route('/register', methods=['GET','POST'])
# @jwt_required() ## 로그인한사람만 보이게 인증하는것 
def register():
    if request.method == 'POST':
        data = request.get_json()

    #     userid = 'thewayat'
    #     username = '더웨이엣'
    #     password = 'As-5520314'
    #     re_password = 'As-5520314'
    #     process = 'AMD64 Family 23 Model 8 Stepping 2, AuthenticAMD'
    #     memory = 'AMD64'
    #     ram = '16'
    #     hostname = 'DESKTOP-LO08C13'
    #     ip = '192.168.0.39'
    #     serial = 'ABCD'


        fcuser = Fcuser()
        fcuser.userid = data['userid']
        fcuser.username = data['username']
        fcuser.password = data['password']

        fcuser.process = data['process']
        fcuser.memory = data['memory']
        fcuser.ram = data['ram']
        fcuser.hostname = data['hostname']
        fcuser.ip = data['IP']
        fcuser.serial = data['serial']

        ## 값이 안들어감 
        db.session.add(fcuser)
        db.session.commit()

        return '하드인증 , 회원가입 완료'
    return '누구세요 ?'
    # users = Fcuser.query.all() ## 디비에 모든 값 
    # # jsonify 를 하면 json 으로 변환해줌 flask 에서 
    # return jsonify([user.serialize for user in users])


@api.route('/users/<uid>', methods=['GET','PUT','DELETE'])
def user_detail(uid):
    if request.method == 'GET':
        user = Fcuser.query.filter(Fcuser.id==uid).first()
        return jsonify(user.serialize)

    elif request.method == 'DELETE':
        ## DB 에서 지움 
        Fcuser.query.delete(Fcuser.id == uid )
        return jsonify(), 204 ## 이제 이것을 사용할수없다는 코드 
    
    ## PUT 전체 데이터를 , PATCH 는 일부만 보통 함 
    data = request.get_json()

    Fcuser.query.filter(Fcuser.id == uid).update(data)
    user = Fcuser.query.filter(Fcuser.id==uid).first()
    return jsonify(user.serialize)
    
