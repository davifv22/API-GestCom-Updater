from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)

login_manager = LoginManager()
login_manager.init_app(app)

from .views import clientes_views, token_views, versao_views, user_views, refresh_token_views, home_views, dashboard_views, login_views, configuracao_views
from .models import clientes_model, versao_model, user_model, versao_pacotes_model

@login_manager.user_loader
def load_user(user):
    return user_model.User.get(user)

app.register_blueprint(home_views.bp)
app.register_blueprint(login_views.bp)
app.register_blueprint(dashboard_views.bp)
app.register_blueprint(clientes_views.bp)
app.register_blueprint(user_views.bp)
app.register_blueprint(configuracao_views.bp)

app.add_url_rule('/home', endpoint='home_views')
login_manager.login_view = 'home'

