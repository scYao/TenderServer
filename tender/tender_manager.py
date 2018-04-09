import json
from models.tender import Tender
from utils import db
from models.user import User
from tools.error_info import ErrorInfo


class TenderManager():

    def create_tender(self, jsonInfo):
        info = json.loads(jsonInfo)
        title = info['title']
        content = info['content']
        user_id = info['user_id']

        tender = Tender(title=title, content=content, user_id=user_id)

        try:
            db.session.add(tender)
            db.session.commit()
            return (True, None)
        except Exception as e:
            db.session.rollback()
            errorInfo = ErrorInfo['TENDER_02']
            errorInfo['detail'] = str(e)
            return (False, errorInfo)

    def query_tender_list_by_user_id(self, jsonInfo):
        info = json.loads(jsonInfo)
        user_id = info['user_id']

        user = db.session.query(User).filter(User.id == user_id).first()
        print('============', repr(user.tenders[0].title), type(repr(user.tenders)), len(user.tenders))
        if user:

            tender_list = []
            # for i in range(len())
            for item in user.tenders:
                tender_list.append(self.generateDict(tender=item))
            print(tender_list)
            return (True, {'tender_list': tender_list})
        else:
            return (False, None)

    def update_tender(self, jsonInfo):
        info = json.loads(jsonInfo)
        id = info['id']
        title = info['title']
        content = info['content']

        tender = db.session.query(Tender).filter(Tender.id == id).first()

        if tender:
            try:
                tender.title = title
                tender.content = content
                db.session.commit()
                return (True, None)
            except Exception as e:
                db.session.rollback()
                errorInfo = ErrorInfo['TENDER_02']
                errorInfo['detail'] = str(e)
                return (False, errorInfo)

        else:
            return (False, None)


def generateDict(self, tender):
    tender_dict = {}
    tender_dict['title'] = tender.title
    tender_dict['content'] = tender.content
    return tender_dict
