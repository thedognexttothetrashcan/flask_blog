import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = 'adsnakdnakjdjahj'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.1000phone.com'
    MAIL_USERNAME = 'xialigang@1000phone.com'
    #授权码或者密码
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    PAGE_NUM = 5 #分页每页显示的数据条数
    #上传文件配置
    UPLOADED_PHOTOS_DEST = os.path.join(BASE_DIR,'static/upload')
    MAX_CONTENT_LENGTH = 1024*1024*64

#开发环境
class   DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/python1809dev_blog'
    DEBUG = True
    TESTING = False

#测试环境
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/test_blog'
    DEBUG = False
    TESTING = True

#生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/blog'
    DEBUG = False
    TESTING = False
#配置的字典
configDict = {
    'default':DevelopmentConfig,
    'development':DevelopmentConfig,
    'test':TestingConfig,
    'production':ProductionConfig
}


