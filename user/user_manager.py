import json

from sqlalchemy import or_, and_

from models.user import User
from utils import db
from token_my.token_manager import TokenManager
from tools.error_info import ErrorInfo


class UserManager(object):

    def add_user(self, jsonInfo):

        jsonInfo= json.loads(jsonInfo)
        print(jsonInfo, type(jsonInfo))
        info = jsonInfo['data']
        info = eval(info)
        print(info,type(info))

        username = info['username']
        password = info['password']
        telephone = info['telephone']
        user = User(username=username, password=password, telephone=telephone)
        db.session.add(user)
        db.session.commit()

        return True

    def login(self, jsonInfo):
        # print(jsonInfo,type(jsonInfo))
        info = json.loads(jsonInfo)
        # print(info, type(info))
        username = info['username']
        password = info['password']

        user = db.session.query(User).filter(or_(User.username == username, User.telephone == username)).first()


        if user and user.check_password(raw_password=password):
            tokenManager = TokenManager()
            tokenID = tokenManager.create_token(user_id=user.id)
            return (True, tokenID)
        else:
            errorInfo = ErrorInfo['TENDER_13']
            errorInfo['detail'] = user
            return (False, errorInfo)
