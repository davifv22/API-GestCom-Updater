from api.app import db
# from .responsavel_model import Responsavel

# responsavel_versao = db.Table('resp_versao',
#                               db.Column('responsavel_id', db.Integer, db.ForeignKey('responsavel.id'), primary_key=True, nullable=False),
#                               db.Column('versao_id', db.Integer, db.ForeignKey('versao.tipo_sistema'), primary_key=True, nullable=False))




class Versao(db.Model):
    __tablename__ = 'versao'
    tipo_sistema = db.Column(db.String(10), primary_key=True, nullable=False) # 0 - MGF | 1 - PRO | 2 - RECEBIMENTO
    versao = db.Column(db.String(50), primary_key=True, nullable=False) # 7.0.08
    release = db.Column(db.String(50), primary_key=True, nullable=False) # 2709
    dt_upload = db.Column(db.Date, nullable=False) # 01/01/2023
    link_download = db.Column(db.String(100)) # # URL_API/versao/download/MGFAtualização_7008.rar
    # responsaveis = db.relationship(Responsavel, secondary='resp_versao', back_populates='versoes')