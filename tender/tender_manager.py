import json
from models.tender import Tender
from utils import db
from models.user import User
from models.city import City
from tools.error_info import ErrorInfo


class TenderManager():

    def create_tender(self, jsonInfo):
        info = json.loads(jsonInfo)
        title = info['title']
        content = info['content']
        user_id = info['user_id']
        city_id = info['city_id']

        tender = Tender(title=title, content=content, user_id=user_id, city_id=city_id)

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
            for item in user.tenders:
                tender_list.append(self.generate_tender_dict(tender=item))
            print(tender_list)
            return (True, {'tender_list': tender_list})
        else:
            return (False, None)

    def get_tender_list(self, jsonInfo):
        info = json.loads(jsonInfo)
        startIndex = info['startIndex']
        pageCount = info['pageCount']
        startDate = info['startDate']
        endDate = info['endDate']

        try:

            query = db.session.query(Tender, City).outerjoin(City, Tender.city_id == City.id)

            if startDate != '-1':
                query = db.session.query(Tender, City).filter(Tender.publish_date > startDate).outerjoin(City, Tender.city_id == City.id)

            if endDate != '-1':
                query =db.session.query(Tender, City).filter(Tender.publish_date < endDate).outerjoin(City, Tender.city_id == City.id)

            restult = query.offset(startIndex).limit(pageCount).all()
            print(restult, type(restult))
            tender_list = []
            for item in restult:
                item_dict = self.generate_tender_city_dict(item=item)
                tender_list.append(item_dict)
            return (True, tender_list)

        except Exception as e:
            db.session.rollback()
            errorInfo = ErrorInfo['TENDER_04']
            errorInfo['detail'] = str(e)
            return (False, errorInfo)

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

    def delete_tender(self, jsonInfo):
        info = json.loads(jsonInfo)
        id = info['id']

        tender = db.session.query(Tender).filter(Tender.id == id).first()

        if tender:
            try:
                db.session.delete(tender)
                db.session.commit()
                return (True, None)
            except Exception as e:
                db.session.rollback()
                errorInfo = ErrorInfo['TENDER_03']
                errorInfo['detail'] = str(e)
                return (False, errorInfo)
        else:
            return (False, None)

    def generate_tender_dict(self, tender):
        tender_dict = {}
        tender_dict['title'] = tender.title
        tender_dict['content'] = tender.content
        return tender_dict

    def generate_tender_city_dict(self, item):
        tender = item[0]
        city = item[1]
        print(tender, type(tender))
        tender_dict = self.generate_tender_dict(tender=tender)
        city_dict = self.generate_city_dict(city=city)
        tender_city = dict(tender_dict, **city_dict)
        return tender_city

    def generate_city_dict(self, city):
        city_dict = {}
        city_dict['city_name'] = city.city_name
        return city_dict
