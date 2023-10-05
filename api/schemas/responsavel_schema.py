# Mudar responsavel para parametros (mgfcontas=true,rpt=true,...)
from api.app import ma
from ..models import responsavel_model
from marshmallow import fields

class ResponsavelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = responsavel_model.Responsavel
        load_instance = True
        fields = ('id', 'nome', 'email', '_links')

    nome = fields.String(required=True)
    email = fields.String(required=True)
    
    _links = ma.Hyperlinks({
        'get': ma.URLFor('responsaveldetail', values=dict(id='<id>')),
        'put': ma.URLFor('responsaveldetail', values=dict(id='<id>')),
        'delete': ma.URLFor('responsaveldetail', values=dict(id='<id>'))
    })