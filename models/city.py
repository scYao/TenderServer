from utils import db


class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_name = db.Column(db.String(10), nullable=False)
    province_id = db.Column(db.Integer, db.ForeignKey('province.id'))

    def __init__(self, city_name, province_id):
        self.city_name = city_name
        self.province_id = province_id

    @staticmethod
    def generate_dict(city):
        city_dict ={}
        city_dict['city_id'] = city.id
        city_dict['cityName'] = city.city_name
        return city_dict