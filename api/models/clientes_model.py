from api.app import db
from ..models import versao_model

class Clientes(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    autarquia = db.Column(db.String(50), nullable=False) # SAAE de Passos
    nome_orgao_resp = db.Column(db.String(100), nullable=False) # Merc. Pague menos
    cidade = db.Column(db.String(50), nullable=False) # Passos
    uf = db.Column(db.String(2), nullable=False) # MG
    ident_empresa = db.Column(db.String(4), nullable=False) # 9999
    situacao = db.Column(db.Integer, nullable=False) # 0 - ATIVO | 1 - SUSPENSO | 2 - CANCELADO
    tipo_sistema_id = db.Column(db.Integer, db.ForeignKey('versao.tipo_sistema', ondelete='CASCADE')) # 0 - MGF | 1 - PRO | 2 - RECEBIMENTOS
    tipo_sistema = db.relationship(versao_model.Versao, backref=db.backref('clientes', lazy='dynamic'))