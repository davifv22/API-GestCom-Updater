from api.app import ma
from marshmallow import fields


class ExecutaveisSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('contas', 'proggestcom', 'requerimento', 'divida_ativa', 'atend_publico', 'pro', 'gestcom')
    
    contas = fields.Boolean(required=True)
    proggestcom = fields.Boolean(required=True)
    requerimento = fields.Boolean(required=True)
    divida_ativa = fields.Boolean(required=True)
    atend_publico = fields.Boolean(required=True)
    pro = fields.Boolean(required=True)
    gestcom = fields.Boolean(required=True)