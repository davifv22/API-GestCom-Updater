from ..models import versao_model
from api.app import db
from .responsavel_service import get_responsavel_id

def set_versao(versao):
    versao_bd = versao_model.Versao(tipo_sistema=versao.tipo_sistema, versao=versao.versao, release=versao.release, dt_upload=versao.dt_upload, link_download=versao.link_download, responsaveis=versao.responsaveis)
    for i in versao.responsaveis:
        responsavel = get_responsavel_id(i)
        versao_bd.responsaveis.append(responsavel)
    db.session.add(versao_bd)
    db.session.commit()
    return versao

def get_versao():
    versao_bd = versao_model.Versao.query.all()
    return versao_bd

def get_versao_tipo_sistema(tipo_sistema):
    versao_bd = versao_model.Versao.query.filter_by(tipo_sistema=tipo_sistema).first()
    return versao_bd

def update_dados_versao(dados_novos, dados_antigos):
    dados_antigos.tipo_sistema = dados_novos.tipo_sistema
    dados_antigos.versao = dados_novos.versao
    dados_antigos.release = dados_novos.release
    dados_antigos.link_download = dados_novos.link_download
    dados_antigos.dt_upload = dados_novos.dt_upload
    for i in dados_novos.responsaveis:
        responsavel = get_responsavel_id(i)
        dados_antigos.responsaveis.append(responsavel)
    db.session.commit()
    
def delete_versao(tipo_sistema):
    db.session.delete(tipo_sistema)
    db.session.commit()