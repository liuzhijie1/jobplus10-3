import os


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hello shiyanlou'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JOB_PER_PAGE = 9
    COMPANY_PER_PAGE = 12
    ADMIN_PER_PAGE = 15
    CSRF_ENABLED = True
    # 上传文件目录
    UPLOADS_DEFAULT_DEST = 'jobplus/static/'
    MAX_CONTENT_LENGTH = 1024 * 1024 * 8


# 本地开发环境
class DevelopConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/jobplus?charset=utf8'


# Test环境
class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Zk6RTBjGNK@sh-cdb-8280ncbs.sql.tencentcdb.com:62304/jobplus?charset=utf8'


# 线上生产环境
class ProdConfig(BaseConfig):
    pass


configs = {
    'dev': DevelopConfig,
    'test': TestConfig,
    'Prod': ProdConfig
}
