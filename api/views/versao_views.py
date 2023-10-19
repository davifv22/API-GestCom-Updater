from flask_restful import Resource
from api.app import api
from flask import request, make_response, jsonify, send_file, render_template, redirect
from flask_login import login_required
from ..schemas import versao_schema, vdownload_schema
from ..services import versao_service
from ..decorator import admin_required, api_key_required
import os


class VersaoList(Resource):
    @login_required
    def get(self):
        pacotes = versao_service.get_pacotes_versao()
        response = make_response(render_template("cPanel/pacotes_versoes.html", pacotes=pacotes))
        response.mimetype = "text/html"
        return response


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
            versao_folder = 'arquivos/versoes/temp'
        else:
            versao_folder = 'arquivos/versoes'
        file = os.path.join(versao_folder, versao_bd[1].nome_arquivo)
        return send_file(file, as_attachment=True)
    
class DeletePacoteVersao(Resource):
    @login_required
    def get(self, tipo_sistema):
        # tipo_sistema_bd = versao_service.get_versao_tipo_sistema(tipo_sistema)
        # if tipo_sistema_bd is None:
        #     return make_response(jsonify("Cliente não foi encontrado!"), 404)
        # versao_service.delete_versao(tipo_sistema_bd)
        return redirect('/versoes')


api.add_resource(VersaoList, '/versoes')
api.add_resource(VersaoDetail, '/versao/<params>')
api.add_resource(VersaoDownload, '/versao/download/<params>')
api.add_resource(DeletePacoteVersao, '/delete/versao/<tipo_sistema>')