from flask_restful import Resource
from flask import make_response, render_template, Blueprint
from flask_login import login_required
from api.app import api

bp = Blueprint('dashboard', __name__)

class Dashborad(Resource):
    @login_required
    def get(self):
        response = make_response(render_template("cPanel/dashboard.html"))
        response.mimetype = "text/html"
        return response

api.add_resource(Dashborad, '/')