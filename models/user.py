from utils import db
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    age = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password=password)

    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result



