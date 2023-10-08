from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)

from .views import clientes_views, token_views, versao_views, user_views, refresh_token_views
from .models import clientes_model, versao_model, user_model, versao_pacotes_model