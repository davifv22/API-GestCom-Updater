from api.app import ma
from ..models import versao_model
from marshmallow import fields
from ..schemas import clientes_schema, responsavel_schema

class VersaoSchema(ma.SQLAlchemyAutoSchema):
    # responsaveis = ma.Nested(responsavel_schema.ResponsavelSchema, many=True, only=('nome', 'email'))
    class Meta:
        model = versao_model.Versao
        load_instance = True
        fields = ('tipo_sistema', 'versao', 'release', 'dt_upload', 'link_download')

    tipo_sistema = fields.String(required=True)
    versao = fields.String(required=True)
    release = fields.String(required=False)
    dt_upload = fields.String(required=False)
    link_download = fields.String(required=False)
    # clientes = fields.List(fields.Nested(clientes_schema.ClientesSchema, only=('autarquia', 'nome_orgao_resp', 'cidade', 'uf', 'tipo_sistema_id')))
    # _links = ma.Hyperlinks({
    #     'get': ma.URLFor('versaodetail', values=dict(id='<tipo_sistema>')),
    #     'put': ma.URLFor('versaodetail', values=dict(id='<tipo_sistema>')),
    #     'delete': ma.URLFor('versaodetail', values=dict(id='<tipo_sistema>'))
    # })