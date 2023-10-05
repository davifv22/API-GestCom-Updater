# Mudar responsavel para parametros (mgfcontas=true,rpt=true,...)
from flask_restful import Resource
from api.app import api
from flask import request, make_response, jsonify, render_template
from flask_jwt_extended import jwt_required
from ..schemas import responsavel_schema
from ..entidades import responsavel
from ..services import responsavel_service
from ..models import responsavel_model
from ..paginate import paginate
from ..decorator import admin_required, api_key_required

class ResponsavelList(Resource):
    # @api_key_required
    def get(self):
        rs = responsavel_schema.ResponsavelSchema(many=True)
        return paginate(responsavel_model.Responsavel, rs)

    @api_key_required
    def post(self):
        rs = responsavel_schema.ResponsavelSchema()
        v = rs.validate(request.json)
        if v:
            return make_response(jsonify(v), 400)
        else:
            nome = request.json['nome']
            email = request.json['email']
            novo_responsavel = responsavel.Responsavel(nome=nome, email=email)
            resultado = responsavel_service.set_responsavel(novo_responsavel)
            
            return make_response(rs.jsonify(resultado), 201)


class ResponsavelDetail(Resource):
    # @api_key_required
    def get(self, id):
        responsavel_bd = responsavel_service.get_responsavel_id(id)
        if responsavel_bd is None:
            return make_response(jsonify("Responsável não cadastrado!"), 404)
        rs = responsavel_schema.ResponsavelSchema()
        return make_response(rs.jsonify(responsavel_bd), 200)

    @admin_required
    def put(self, id):
        responsavel_bd = responsavel_service.get_responsavel_id(id)
        if responsavel_bd is None:
            return make_response(jsonify("Responsável não cadastrado!"), 404)
        rs = responsavel_schema.ResponsavelSchema()
        v = rs.validate(request.json)
        if v:
            return make_response(jsonify(v), 400)
        else:
            nome = request.json['nome']
            email = request.json['email']

            novos_dados = responsavel.Responsavel(nome=nome, email=email)
            responsavel_service.update_dados_responsavel(novos_dados, responsavel_bd)
            responsavel_atualizado = responsavel_service.get_responsavel_id(id)
            return make_response(rs.jsonify(responsavel_atualizado), 200)

    @admin_required
    def delete(self, id):
        responsavel_bd = responsavel_service.get_responsavel_id(id)
        if responsavel_bd is None:
            return make_response(jsonify("Responsável não cadastrado!"), 404)
        responsavel_service.delete_responsavel(responsavel_bd)
        return make_response("Responsável deletado com sucesso!", 204)

class Home(Resource):
    def get(self):
        response = make_response(render_template("index.html"))
        response.mimetype = "text/html"
        return response


api.add_resource(Home, '/')
api.add_resource(ResponsavelList, '/responsavel')
api.add_resource(ResponsavelDetail, '/responsavel/<int:id>')