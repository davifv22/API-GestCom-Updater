# Mudar responsavel para parametros (mgfcontas=true,rpt=true,...)
from ..models import responsavel_model
from api.app import db

def set_responsavel(responsavel):
    responsavel_bd = responsavel_model.Responsavel(nome=responsavel.nome, email=responsavel.email)
    db.session.add(responsavel_bd)
    db.session.commit()
    return responsavel_bd

def get_responsavel():
    responsavel = responsavel_model.Responsavel.query.all()
    return responsavel

def get_responsavel_id(id):
    responsavel = responsavel_model.Responsavel.query.filter_by(id=id).first()
    return responsavel

def update_dados_responsavel(dados_novos, dados_antigos):
    dados_antigos.nome = dados_novos.nome
    dados_antigos.email = dados_novos.email
    db.session.commit()
    
def delete_responsavel(id):
    db.session.delete(id)
    db.session.commit()