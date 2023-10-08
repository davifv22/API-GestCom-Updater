from api.app import db


class VersaoPacotes(db.Model):
    __tablename__ = 'versao_pacotes'
    tipo_sistema = db.Column(db.String(10), primary_key=True, nullable=False)
    versao = db.Column(db.String(50), primary_key=True, nullable=False)
    release = db.Column(db.String(50), primary_key=True, nullable=False)
    dt_upload = db.Column(db.Date, nullable=False)
    nome_maquina = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    gestcomexec = db.Column(db.Boolean, default=False, nullable=False)
    proexec = db.Column(db.Boolean, default=False, nullable=False)
    contasexec = db.Column(db.Boolean, default=False, nullable=False)
    proggestcomexec = db.Column(db.Boolean, default=False, nullable=False)
    requerimentoexec = db.Column(db.Boolean, default=False, nullable=False)
    divida_ativaexec = db.Column(db.Boolean, default=False, nullable=False)
    atend_publicoexec = db.Column(db.Boolean, default=False, nullable=False)
    contasrpt = db.Column(db.String(255), nullable=False)
    requerimentorpt = db.Column(db.String(255), nullable=False)
    nome_arquivo = db.Column(db.String(50), primary_key=True, nullable=False)
    link_download = db.Column(db.String(100), nullable=False)