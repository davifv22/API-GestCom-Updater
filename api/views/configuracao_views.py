from flask_restful import Resource
from flask import make_response, render_template, Blueprint
from flask_login import login_required
from api.app import api
from ..services import dashboard_service


bp = Blueprint('config', __name__)

class Config(Resource):
    @login_required
    def get(self):
        response = make_response(render_template("cPanel/configuracao.html"))
        response.mimetype = "text/html"
        return response

api.add_resource(Config, '/config')