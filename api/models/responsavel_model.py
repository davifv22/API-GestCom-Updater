# Mudar responsavel para parametros (mgfcontas=true,rpt=true,...)
from api.app import db

class Responsavel(db.Model):
    __tablename__ = 'responsavel'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False) # Fulano de Ciclano
    email = db.Column(db.String(50), nullable=False) # user@mail.com
    # versoes = db.relationship("Versao", secondary='resp_versao', back_populates='responsaveis')
