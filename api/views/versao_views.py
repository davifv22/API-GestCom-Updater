from flask_restful import Resource
from api.app import api
from flask import request, make_response, jsonify, send_file
from flask_jwt_extended import jwt_required
from ..schemas import versao_schema, vdownload_schema
from ..services import versao_service
from ..paginate import paginate
from ..models import versao_model
from ..decorator import admin_required, api_key_required
import os


class VersaoList(Resource):
    # @api_key_required
    def get(self):
        vs = versao_schema.VersaoSchema(many=True)
        versao_bd = versao_service.get_versao()
        return make_response(vs.jsonify(versao_bd), 200)


class VersaoDetail(Resource):
    # @api_key_required
    def get(self, params):
        versao_bd = versao_service.get_versao_tipo_sistema(params)
        if versao_bd is None:
            return make_response(jsonify("Versão não foi encontrado!"), 404)
        vs = versao_schema.VersaoSchema()
        return make_response(vs.jsonify(versao_bd), 200)

    def post(self, params):
        if params == 'download':
            vds = vdownload_schema.VersaoDownloadSchema()
            v = vds.validate(request.json)
            if v:
                return make_response(jsonify(v), 400)
            else:
                tipo_sistema = request.json['tipo_sistema']
                versao = request.json['versao']
                versao_bd = versao_service.get_versao_tipo_sistema(params, tipo_sistema, versao)
                if versao_bd is None:
                    return make_response(jsonify("Versão não foi encontrado!"), 404)
                
                vs = versao_schema.VersaoSchema()
                return make_response(vs.jsonify(versao_bd), 200)

        if params == 'upload':
            pass
        # if params == 'mgf7008':
        #     filename = 'MGFAtualizacao7008_20230921.rar'            
        # elif params == 'mgf6031':
        #     filename = 'MGFAtualizacao6031_20230926.rar'
        # elif params == 2:
        #     filename = 'PROAtualizacao6031_20230927.rar'
        # elif params == 3:
        #     filename = 'PROAtualizacao7008_20230821.rar'
        # elif params == 4:
        #     filename = 'Update_Gestcom-Recebimentos #04-09-2023.rar'
        # else:
        #     return make_response(jsonify("Versão não foi encontrada!"), 404)
        # versao_folder = './arquivos/versoes'
        # file = os.path.join(versao_folder, filename)
        # return #send_file(file, as_attachment=True)


    @admin_required
    def delete(self, id):
        versao_bd = versao_service.get_versao(id)
        if versao_bd is None:
            return make_response(jsonify("Versão não foi encontrada!"), 404)
        versao_service.delete_versao(id)
        return make_response("Versão deletada com sucesso!", 204)


api.add_resource(VersaoList, '/versoes')
api.add_resource(VersaoDetail, '/versao/<params>')