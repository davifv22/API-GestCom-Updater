from flask_restful import Resource
from flask import make_response, render_template, Blueprint
from flask_login import login_required
from api.app import api
from ..services import dashboard_service


bp = Blueprint('dashboard', __name__)

class Dashborad(Resource):
    @login_required
    def get(self):
        chart_clientes = dashboard_service.create_chart_clientes()
        chart_clientes_ = dashboard_service.create_chart_clientes_()
        chart_versao = dashboard_service.create_chart_versao()
        response = make_response(render_template("cPanel/dashboard.html", chart_clientes=chart_clientes, chart_clientes_=chart_clientes_, chart_versao=chart_versao))
        response.mimetype = "text/html"
        return response

api.add_resource(Dashborad, '/')