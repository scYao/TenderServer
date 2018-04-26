from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache



db = SQLAlchemy()

cache_config = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': '127.0.0.1',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': '',
    'CACHE_REDIS_PASSWORD': '',
    'CACHE_REDIS_URL' : 'redis://localhost:6379'
}

cache = Cache(config=cache_config)


# @staticmethod
# def check_is_none(*args, **kwargs):
#     if (not args) and (not kwargs):
#         return True
#
#     if args:
#         for i in args:
#             if not i:
#                 return True
#     elif kwargs:
#         for j

