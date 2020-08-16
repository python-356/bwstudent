import os

SECRET_KEL = os.urandom(24)
DEBUG = True

# 数据库设置
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'sims_db'
USERNAME = 'root'
PASSWORD = 'msphmy'

# dialect+driver://username:password@host:port/database,
DB_URI = 'mysql+pymysql://{root}:{password}@{host}:{port}/{database}?charset=utf8'.format(
    root=USERNAME,
    password=PASSWORD,
    host=HOSTNAME,
    port=PORT,
    database=DATABASE
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = DB_URI
