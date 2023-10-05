class Clientes():
    def __init__(self, autarquia, nome_orgao_resp, cidade, uf, ident_empresa, situacao, tipo_sistema_id):
        self.__autarquia = autarquia
        self.nome_orgao_resp = nome_orgao_resp
        self.__cidade = cidade
        self.__uf = uf
        self.__ident_empresa = ident_empresa
        self.__situacao = situacao
        self.__tipo_sistema_id = tipo_sistema_id


    @property
    def autarquia(self):
        return self.__autarquia

    @autarquia.setter
    def autarquia(self, autarquia):
        self.__autarquia = autarquia

    @property
    def nome_orgao_resp(self):
        return self.__nome_orgao_resp

    @nome_orgao_resp.setter
    def nome_orgao_resp(self, nome_orgao_resp):
        self.__nome_orgao_resp = nome_orgao_resp

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def uf(self):
        return self.__uf

    @uf.setter
    def uf(self, uf):
        self.__uf = uf
        
    @property
    def ident_empresa(self):
        return self.__ident_empresa

    @ident_empresa.setter
    def ident_empresa(self, ident_empresa):
        self.__ident_empresa = ident_empresa

    @property
    def situacao(self):
        return self.__situacao

    @situacao.setter
    def situacao(self, situacao):
        self.__situacao = situacao

    @property
    def tipo_sistema_id(self):
        return self.__tipo_sistema_id

    @tipo_sistema_id.setter
    def tipo_sistema_id(self, tipo_sistema_id):
        self.__tipo_sistema_id = tipo_sistema_id