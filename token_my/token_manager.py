# coding=utf8

import hashlib
import datetime
class TokenManager():

    def create_token(self,user_id):
        time_now = datetime.datetime.now()
        tokenID = self.getMD5String(''.join([str(time_now), str(user_id)]))
        return tokenID


    def getMD5String(self,string):
        md5= hashlib.md5()
        md5.update(string.encode('utf8'))
        return md5.hexdigest()
