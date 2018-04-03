from models.user import *
import json
from utils import db


class UserManager(object):

    def add_user(self, jsonInfo):
        info = json.loads(jsonInfo)
        username = info['username']
        password = info['password']
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return True
