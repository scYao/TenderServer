import json

from flask import Flask
from flask import request

import config
from tender.tender_manager import TenderManager
from user.user_manager import UserManager
from utils import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app=app)


@app.route('/')
def hello_world():
    return 'Hello World!'

# 增加用户
@app.route('/add_user/', methods=['GET', 'POST'])
def add_user():
    # return 'success'
    userManager = UserManager()
    data = {}
    data['status'] = 'failed'
    data['data'] = "{'username':'yao','password':'123', 'telephone':'17551018411'}"
    if request.method == 'POST':
        paramsJson = request.form['data']
        result = userManager.add_user(paramsJson)
        if result:
            data['status'] = 'success'
            data['data'] = 'you has add user successfully'
        return json.dumps(data)
    else:
        paramsJson = json.dumps(data)
        result = userManager.add_user(paramsJson)
        if result:
            data['status'] = 'success'
            data['data'] = 'you has add user successfully'
        return json.dumps(data)

#登录
@app.route('/login/', methods=['GET'])
def login():
    userManager = UserManager()
    data = {}
    data['status'] = 'failed'
    data['data'] = {'username': 'yao', 'password': '123'}
    if request.method == 'GET':
        paramsJson = json.dumps(data['data'])
        (stauts, result) = userManager.login(jsonInfo=paramsJson)
        if stauts:
            data['status'] = 'success'
            data['data'] = result
        return json.dumps(data)

#创建招标
@app.route('/create_tender/', methods=['GET', 'POST'])
def create_tender():
    tenderManager = TenderManager()
    data = {}
    data['status'] = 'failed'
    data['data'] = {'title': 'tender', 'content': 'tender content', 'user_id': 1}

    if request.method == 'GET':
        paramsJson = json.dumps(data['data'])
        (status, restult) = tenderManager.create_tender(jsonInfo=paramsJson)
        if status:
            data['status'] = 'success'
            data['data'] = restult
        else:
            data['data'] = restult
        return json.dumps(data)

#获取招标列表
@app.route('/tender_list/', methods=['GET', 'POST'])
def tender_list():
    tenderManager = TenderManager()
    data = {}
    data['status'] = 'failed'
    data['data'] = {'user_id': '1'}

    if request.method == 'GET':
        paramsJson = json.dumps(data['data'])
        (status, result) = tenderManager.query_tender_list_by_user_id(jsonInfo=paramsJson)

        if status:
            data['status'] = 'success'
            data['data'] =result
        else:
            data['data'] = result
        return json.dumps(data)

#修改招标信息
@app.route('/update_tender', methods=['GET', 'POST'])
def update_tender():
    tenderManager = TenderManager()
    data ={}
    data['status'] = 'failed'
    data['data'] = {'id':'1', 'title': 'title change', 'content':'content change'}

    if request.method == 'GET':
        paramJson = json.dumps(data['data'])
        (status, result) = tenderManager.update_tender(jsonInfo=paramJson)

        if status:
            data['status'] = 'success'
            data['data'] = result
        else:
            data['data'] = result
        return json.dumps(data)


if __name__ == '__main__':
    app.run()
