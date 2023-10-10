from flask_restful import Resource
from flask import make_response, render_template, Blueprint
from flask_login import login_required
from api.app import api

bp = Blueprint('home', __name__)

class Home(Resource):
    def get(self):
        response = make_response(render_template("home/home.html"))
        response.mimetype = "text/html"
        return response

api.add_resource(Home, '/home')