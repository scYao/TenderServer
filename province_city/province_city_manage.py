from utils import db
from models.province import Province
from models.city import City


class ProvinceCityManage():

    def get_province_city_list(self):
        province_city_list = []
        try:
            province_list = db.session.query(Province).all()
            print(province_list, type(province_list))
            for item in province_list:
                item_dict = {}
                item_dict = Province.generateDict(province=item)
                # print(item_dict)
                city_list = db.session.query(City).filter(City.province_id == item_dict['province_id']).all()

                city_array=[]
                for city in city_list:
                    city_dict = City.generate_dict(city=city)
                    city_array.append(city_dict)
                item_dict['city_list'] = city_array

                province_city_list.append(item_dict)
            print(province_city_list)
            return (True, province_city_list)

        except Exception as e:

            return (False, str(e))
