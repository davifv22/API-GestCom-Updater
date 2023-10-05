from api.app import ma
from ..models import clientes_model
from marshmallow import fields

class ClientesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = clientes_model.Clientes
        load_instance = True
        fields = ('id', 'autarquia', 'nome_orgao_resp', 'cidade', 'uf', 'ident_empresa', 'situacao', 'tipo_sistema_id', '_links')
    
    autarquia = fields.String(required=True)
    nome_orgao_resp = fields.String(required=True)
    cidade = fields.String(required=True)
    uf = fields.String(required=True)
    ident_empresa = fields.String(required=True)
    situacao = fields.Integer(required=False)
    tipo_sistema_id = fields.String(required=True)
    
    _links = ma.Hyperlinks({
        'get': ma.URLFor('clientedetail', values=dict(id='<id>')),
        'put': ma.URLFor('clientedetail', values=dict(id='<id>')),
        'delete': ma.URLFor('clientedetail', values=dict(id='<id>'))
    })