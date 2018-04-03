from flask import Flask
import config
from utils import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app=app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
