from flask import Flask
import config
from utils import db
from user.user_manager import UserManager
from flask import request
import json

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app=app)


@app.route('/')
def hello_world():
    return 'Hello World!'


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

@app.route('/login/', methods=['GET'])
def login():
    userManager = UserManager()
    data ={}
    data['status'] = 'failed'
    data['data'] = {'username': 'yao','password':'123'}
    if request.method =='GET':
        paramsJson = json.dumps(data['data'])
        (stauts, result) = userManager.login(jsonInfo=paramsJson)
        if stauts:
            data['status'] = 'success'
            data['data']= result
        return json.dumps(data)



if __name__ == '__main__':
    app.run()
