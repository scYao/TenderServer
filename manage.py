from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from TenderServer import app
from models.user import *
from models.tender import Tender
from utils import db
from models.city import City
from models.province import Province

# 使用migrate绑定db和app
migrate = Migrate(app=app, db=db)

# 添加迁移脚本命令到manager
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
