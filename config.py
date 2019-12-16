import os

# 根目录下没有文件是调用os库创建
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'dev'

    # 数据库连接配置
    # dialect+driver://username:password@host:port/database?charset=utf8mb4

    # sqlite 配置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    # mysql 链接配置
    # DIALECT = "mysql"
    # DRIVER = "pymysql"
    # USERNAME = "root"
    # PASSWORD = "password"
    # HOST = "127.0.0.1"
    # PORT = "3306"
    # DATABASE = "app"
    # CHARSET = "utf8mb4"

    # SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset={}".format(
    #     DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE,CHARSET)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
