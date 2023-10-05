from flask_restful import Resource
from api.app import api
from flask import request, make_response, jsonify, send_file
from flask_jwt_extended import jwt_required
from ..schemas import versao_schema
from ..entidades import versao
from ..services import versao_service
from ..paginate import paginate
from ..models import versao_model
from ..decorator import admin_required, api_key_required
import os


class VersaoList(Resource):
    # @api_key_required
    def get(self):
        vs = versao_schema.VersaoSchema(many=True)
        return paginate(versao_model.Versao, vs)


class VersaoDetail(Resource):
    # @api_key_required
    def get(self, id):
        if id == 0:
            filename = 'MGFAtualizacao7008_20230921.rar'            
        elif id == 1:
            filename = 'MGFAtualizacao6031_20230926.rar'
        elif id == 2:
            filename = 'PROAtualizacao6031_20230927.rar'
        elif id == 3:
            filename = 'PROAtualizacao7008_20230821.rar'
        elif id == 4:
            filename = 'Update_Gestcom-Recebimentos #04-09-2023.rar'
        else:
            return make_response(jsonify("Versão não foi encontrada!"), 404)
        versao_folder = './arquivos/versoes_disp'
        path = os.path.join(versao_folder, filename)
        return send_file(path, as_attachment=True)


    @admin_required
    def delete(self, id):
        versao_bd = versao_service.get_versao(id)
        if versao_bd is None:
            return make_response(jsonify("Versão não foi encontrada!"), 404)
        versao_service.delete_versao(id)
        return make_response("Versão deletada com sucesso!", 204)


api.add_resource(VersaoList, '/versoes_disp')
api.add_resource(VersaoDetail, '/versao/download/id=<int:id>')