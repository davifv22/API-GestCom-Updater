from api.app import ma
from ..models import versao_model
from marshmallow import fields


class VersaoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = versao_model.Versao
        load_instance = True
        fields = ('tipo_sistema', 'versao', 'release', 'dt_upload', 'link_download')

    tipo_sistema = fields.String(required=True)
    versao = fields.String(required=True)
    release = fields.String(required=False)
    dt_upload = fields.String(required=False)
    link_download = fields.String(required=False)