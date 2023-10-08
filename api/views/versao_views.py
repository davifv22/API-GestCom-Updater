from flask_restful import Resource
from api.app import api
from flask import request, make_response, jsonify, send_file
from ..schemas import versao_schema, vdownload_schema
from ..services import versao_service
from ..decorator import admin_required, api_key_required
import os


class VersaoList(Resource):
    @api_key_required
    def get(self):
        vs = versao_schema.VersaoSchema(many=True)
        versao_bd = versao_service.get_versao()
        return make_response(vs.jsonify(versao_bd), 200)


class VersaoDetail(Resource):
    @api_key_required
    def get(self, params):
        versao_bd = versao_service.get_versao_tipo_sistema(params)
        if versao_bd[0] is False:
            return make_response(jsonify(versao_bd[1]), 404)
        vs = versao_schema.VersaoSchema()
        return make_response(vs.jsonify(versao_bd[1]), 200)

    @api_key_required
    def post(self, params):
        if params == 'download':
            # Json format APP Updater GestCom
            vds = vdownload_schema.VersaoDownloadSchema()
            v = vds.validate(request.json)
            if v:
                return make_response(jsonify(v), 400)
            else:
                tipo_sistema = request.json['tipo_sistema']
                versao = request.json['versao']
                versao_bd = versao_service.get_versao_tipo_sistema(f'{tipo_sistema}{versao}')
                if versao_bd[0] is False:
                    return make_response(jsonify(versao_bd[1]), 404)
                
                
                versao_pacote = versao_service.set_versao_pacotes(f'{tipo_sistema}{versao}', request.json)
                if versao_pacote[0] is False:
                    return make_response(jsonify(versao_pacote[1]), 404)
                
                vs = versao_schema.VersaoSchema()
                return make_response(vs.jsonify(versao_pacote[1]), 200)

        if params == 'upload':
            pass


class VersaoDownload(Resource):
    def get(self, params):
        versao_bd = versao_service.get_versao_tipo_sistema(params)
        if versao_bd[0] is False:
            return make_response(jsonify(versao_bd[1]), 404)
        
        if params[-4:] == '.zip':
            versao_folder = './arquivos/versoes/temp'
        else:
            versao_folder = './arquivos/versoes'
        file = os.path.join(versao_folder, versao_bd[1].nome_arquivo)
        return send_file(file, as_attachment=True)


api.add_resource(VersaoList, '/versoes')
api.add_resource(VersaoDetail, '/versao/<params>')
api.add_resource(VersaoDownload, '/versao/download/<params>')