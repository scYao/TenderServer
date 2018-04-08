from utils import db


class Tender(db.Model):
    __tablename__ = 'tender'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    users = db.relationship('User', backref=db.backref('tenders'))
