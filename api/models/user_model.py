from api.app import db
from passlib.hash import pbkdf2_sha256

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user = db.Column(db.String(25), nullable=False)
    nome = db.Column(db.String(50), nullable=False) # Fulano de Ciclano
    email = db.Column(db.String(100), nullable=False) # user@mail.com
    senha = db.Column(db.String(255), nullable=False) # criptografada
    situacao = db.Column(db.Boolean, default=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    api_key = db.Column(db.String(100), nullable=False)

    def encriptar_senha(self):
        self.senha = pbkdf2_sha256.hash(self.senha)
        
    def ver_senha(self, senha):
        return pbkdf2_sha256.verify(senha, self.senha)
