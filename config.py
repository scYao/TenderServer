# 数据库配置
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'tender'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS =False