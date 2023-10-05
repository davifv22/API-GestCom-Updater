from ..models import clientes_model
from api.app import db

def set_cliente(cliente):
    clientes_bd = clientes_model.Clientes(autarquia=cliente.autarquia, nome_orgao_resp=cliente.nome_orgao_resp, cidade=cliente.cidade, uf=cliente.uf, ident_empresa=cliente.ident_empresa, situacao=cliente.situacao, tipo_sistema_id=cliente.tipo_sistema_id)
    db.session.add(clientes_bd)
    db.session.commit()
    return clientes_bd

def get_clientes():
    clientes = clientes_model.Clientes.query.all()
    return clientes

def get_cliente(id):
    cliente = clientes_model.Clientes.query.filter_by(id=id).first()
    return cliente

def update_dados_cliente(dados_novos, dados_antigos):
    dados_antigos.autarquia = dados_novos.autarquia
    dados_antigos.nome_orgao_resp = dados_novos.nome_orgao_resp
    dados_antigos.cidade = dados_novos.cidade
    dados_antigos.uf = dados_novos.uf
    dados_antigos.ident_empresa = dados_novos.ident_empresa
    dados_antigos.situacao = dados_novos.situacao
    dados_antigos.tipo_sistema_id = dados_novos.tipo_sistema_id
    db.session.commit()
    
def delete_cliente(id):
    db.session.delete(id)
    db.session.commit()