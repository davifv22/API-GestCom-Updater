from api.app import ma
from marshmallow import fields

class RptsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('contas', 'requerimento')
    
    contas = fields.String(required=True)
    requerimento = fields.String(required=True)
