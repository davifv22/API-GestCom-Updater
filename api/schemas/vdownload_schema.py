from api.app import ma
from marshmallow import fields
from .arquivos_schema import ArquivosSchema


class VersaoDownloadSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('tipo_sistema', 'versao', 'data_hora', 'nome_maquina', 'cidade', 'arquivos')

    tipo_sistema = fields.String(required=True)
    versao = fields.String(required=True)
    data_hora = fields.String(required=True)
    nome_maquina = fields.String(required=True)
    cidade = fields.String(required=True)
    arquivos = fields.List(fields.Nested(ArquivosSchema, only=('executaveis', 'rpts')))
