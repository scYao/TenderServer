from TenderServer import app
from user.user_manager import UserManager
from flask import request
import json

@app.route('/add_user/', methods=['GET', 'POST'])
def add_user():
    userManager = UserManager()
    data = {}
    data['status']= 'failed'
    data['data'] =''
    if request.method == 'POST':
        paramsJson = request.form['data']
        result= userManager.add_user(paramsJson)
        if result:
            data['status'] = 'success'
            data['data'] ='you has add user successfully'
        return json.dumps(data)


@app.route('/login/', methods=['GET'])
def login():
    userManager = UserManager()
    data = {}
    data['status'] = 'failed'
    data['data'] = ''
    if request.method == 'GET':
        paramsJson  = request.form['data']
        (status, result) = userManager.login(paramsJson)

        if status is True:
            pass

