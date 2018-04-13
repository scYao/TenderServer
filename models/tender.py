from utils import db


class Tender(db.Model):
    __tablename__ = 'tender'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    publish_date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    users = db.relationship('User', backref=db.backref('tenders'))

    def __init__(self, title, content, user_id, city_id, publish_date):
        self.title = title
        self.content = content
        self.user_id = user_id
        self.city_id = city_id
        self.publish_date = publish_date
