from flask_restful import Resource
from api.app import api
from flask import request, make_response, jsonify, render_template, Blueprint, redirect
from flask_login import login_required
from ..schemas import clientes_schema
from ..entidades import clientes
from ..services import clientes_service, versao_service
from ..models import clientes_model
from ..decorator import admin_required, api_key_required # Implementar após os testes para access token

bp = Blueprint('clientes', __name__)

class ClientesList(Resource):
    @login_required
    def get(self):
        clientes = clientes_service.get_clientes()
        response = make_response(render_template("cPanel/clientes.html", clientes=clientes))
        response.mimetype = "text/html"
        return response
    

    @login_required
    def post(self):
        cs = clientes_schema.ClientesSchema()
        v = cs.validate(request.form)
        if v:
            return make_response(jsonify(v), 400) # Mensagem de erro
        else:
            autarquia = request.form['autarquia']
            autarquia = 'SAEG Guaratinguetá'
            nome_orgao_resp = request.form['nome_orgao_resp']
            cidade = request.form['cidade']
            uf = request.form['uf']
            ident_empresa = request.form['ident_empresa']
            situacao = request.form['situacao']
            tipo_sistema_id = request.form['tipo_sistema_id']
            cliente_tipo_sistema_id = versao_service.get_versao_tipo_sistema(tipo_sistema_id)
            if cliente_tipo_sistema_id is None:
                return make_response(jsonify("Tipo de sistema não foi encontrado!"), 404)
            novo_cliente = clientes.Clientes(autarquia=autarquia,
                                             nome_orgao_resp=nome_orgao_resp,
                                             cidade=cidade,
                                             uf=uf,
                                             ident_empresa=ident_empresa,
                                             situacao=situacao,
                                             tipo_sistema_id=tipo_sistema_id)
            x = clientes_service.set_cliente(novo_cliente)
            return self.get()


class ClienteDetail(Resource):
    @api_key_required
    def get(self, id):
        cliente_bd = clientes_service.get_cliente(id)
        if cliente_bd is None:
            return make_response(jsonify("Cliente não foi encontrado!"), 404)
        cs = clientes_schema.ClientesSchema()
        return make_response(cs.jsonify(cliente_bd), 200)

    @api_key_required
    def put(self, id):
        cliente_bd = clientes_service.get_cliente(id)
        if cliente_bd is None:
            return make_response(jsonify("Cliente não foi encontrado!"), 404)
        cs = clientes_schema.ClientesSchema()
        v = cs.validate(request.json)
        if v:
            return make_response(jsonify(v), 400)
        else:
            autarquia = request.json['autarquia']
            nome_orgao_resp = request.json['nome_orgao_resp']
            cidade = request.json['cidade']
            uf = request.json['uf']
            ident_empresa = request.json['ident_empresa']
            situacao = 0
            tipo_sistema_id = request.json['tipo_sistema_id']
            cliente_tipo_sistema_id = versao_service.get_versao_id(tipo_sistema_id)
            if cliente_tipo_sistema_id is None:
                return make_response(jsonify('Tipo de sistema não cadastrado!'), 404)
            novos_dados = clientes.Clientes(autarquia=autarquia,
                                            nome_orgao_resp=nome_orgao_resp,
                                            cidade=cidade,
                                            uf=uf,
                                            ident_empresa=ident_empresa,
                                            situacao=situacao,
                                            tipo_sistema_id=tipo_sistema_id)
            clientes_service.update_dados_cliente(novos_dados, cliente_bd)
            cliente_atualizado = clientes_service.get_cliente(id)
            return make_response(cs.jsonify(cliente_atualizado), 200)

class Delete(Resource):
    @login_required
    def get(self, id):
        cliente_bd = clientes_service.get_cliente(id)
        if cliente_bd is None:
            return make_response(jsonify("Cliente não foi encontrado!"), 404)
        clientes_service.delete_cliente(cliente_bd)
        return redirect('/clientes')


api.add_resource(ClientesList, '/clientes')
api.add_resource(ClienteDetail, '/cliente/<int:id>')
api.add_resource(Delete, '/cliente/delete/<int:id>')
