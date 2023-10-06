from api.app import ma
from marshmallow import fields
from .executaveis_schema import ExecutaveisSchema
from .rpts_schema import RptsSchema


class ArquivosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('executaveis', 'rpts')

    executaveis = fields.List(fields.Nested(ExecutaveisSchema, only=('contas', 'proggestcom', 'requerimento', 'divida_ativa', 'atend_publico', 'pro', 'gestcom')))
    rpts = fields.List(fields.Nested(RptsSchema, only=('contas', 'requerimento')))