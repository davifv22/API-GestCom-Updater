# DB LOCAL:
# DEBUG = True
DEBUG = False

if DEBUG:
    USERNAME = 'root'
    PASSWORD = '12345'
    SERVER = 'localhost'
    DB = 'db'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
else:
    USERNAME = 'root'
    PASSWORD = 'GQBIfMhLAZcjX24v04Le'
    SERVER = 'containers-us-west-92.railway.app'
    PORT_ = '5757'
    DB = 'railway'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{SERVER}:{PORT_}/{DB}'

SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'aplicacao_flask'