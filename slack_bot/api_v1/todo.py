
from flask import jsonify
from flask import request , session
from flask import Blueprint
from models import Todo, db
import requests,json
from . import api
import datetime

def send_slack(msg):
    res = requests.post('https://hooks.slack.com/services/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', json={
        'text':msg
        } , headers={'Content-Type':'application/json'})


@api.route('/todos' , methods=['GET','POST','DELETE'])
def todos():
    userid = session.get('userid',None)
    if not userid:
        ## 로그인이 안되면 401
        return jsonify(),401

    if request.method == 'POST':
        data = request.get_json()

        todo = Todo()
        todo.title = data.get('title')
        todo.fcuser_id = userid

        db.session.add(todo)
        db.session.commit()

        send_slack('TODO가 생성되었습니다.')
         
        return jsonify(),201
    elif request.method == 'GET':
        todos = Todo.query.filter_by(fcuser_id=userid)
        return jsonify([t.serialize for t in todos])

    elif request.method == 'DELETE':
        data = request.get_json() 
        todo_id = data.get('todo_id')

        todo = Todo.query.filter_by(id=todo_id).first()
        db.session.delete(todo)
        db.session.commit()

        return jsonify(), 203
    data = request.get_json()
    return jsonify(data)

# @api.route('/todos' , methods=['GET','POST'])
# def slack_todos():
#     if request.method == 'POST':
#         # 생성하는 코드 추가 
#         send_slack('TODO가 생성되었습니다.') # 사용자 정보, 할일 제목 ,기한
        

#     elif request.method == 'GET':
#         pass
    
#     data = request.get_json()
#     return jsonify(data)



@api.route('/slack/todos' , methods=['POST'])
def slack_todos():
    res = request.form['text'].split(' ')
    cmd, *args = res
    if cmd == 'create':
        todo_name = args[0]

        todo = Todo()
        todo.title = todo_name

        db.session.add(todo)
        db.session.commit()
        ret_msg = 'todo가 생성되었습니다.'
        dt = datetime.datetime.now()
        send_slack(f'[{dt}] {todo_name}') 


    elif cmd == 'list':
        todos = Todo.query.all()
        for idx, todo in enumerate(todos):
            ret_msg += '%d. %s (~ %s)\n' %(idx+1, todo.title, str(todo.tstamp))

    return ret_msg
