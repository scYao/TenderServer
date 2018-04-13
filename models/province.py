from utils import db

class Province(db.Model):
    __tablename__ ='province'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    province_name = db.Column(db.String(10), nullable=False)
    city = db.relationship('City', backref='province',lazy='dynamic')

    def __init__(self, province_name):
        self.province_name = province_name

    @staticmethod
    def generateDict(province):
        province_dict ={}
        province_dict['province_id'] = province.id
        province_dict['provinceName'] = province.province_name
        return province_dict