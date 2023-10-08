class VersaoPacotes():
    def __init__(self, tipo_sistema, versao, release, dt_upload, nome_maquina, cidade, gestcomexec, proexec, contasexec, proggestcomexec,
                 requerimentoexec, divida_ativaexec, atend_publicoexec, contasrpt, requerimentorpt, nome_arquivo, link_download):
        self.__tipo_sistema = tipo_sistema
        self.__versao = versao
        self.__release = release
        self.__dt_upload = dt_upload
        self.__nome_maquina = nome_maquina
        self.__cidade = cidade
        self.__gestcomexec = gestcomexec
        self.__proexec = proexec
        self.__contasexec = contasexec
        self.__proggestcomexec = proggestcomexec
        self.__requerimentoexec = requerimentoexec
        self.__divida_ativaexec = divida_ativaexec
        self.__atend_publicoexec = atend_publicoexec
        self.__contasrpt = contasrpt
        self.__requerimentorpt = requerimentorpt
        self.__link_download = link_download

    @property
    def tipo_sistema(self):
        return self.__tipo_sistema

    @tipo_sistema.setter
    def tipo_sistema(self, tipo_sistema):
        self.__tipo_sistema = tipo_sistema

    @property
    def versao(self):
        return self.__versao

    @versao.setter
    def versao(self, versao):
        self.__versao = versao

    @property
    def release(self):
        return self.__release

    @release.setter
    def release(self, release):
        self.__release = release

    @property
    def dt_upload(self):
        return self.__dt_upload

    @dt_upload.setter
    def dt_upload(self, dt_upload):
        self.__dt_upload = dt_upload

    @property
    def nome_maquina(self):
        return self.__nome_maquina

    @nome_maquina.setter
    def nome_maquina(self, nome_maquina):
        self.__nome_maquina = nome_maquina
        
    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def gestcomexec(self):
        return self.__gestcomexec

    @gestcomexec.setter
    def gestcomexec(self, gestcomexec):
        self.__gestcomexec = gestcomexec

    @property
    def proexec(self):
        return self.__proexec

    @proexec.setter
    def proexec(self, proexec):
        self.__proexec = proexec

    @property
    def contasexec(self):
        return self.__contasexec

    @contasexec.setter
    def contasexec(self, contasexec):
        self.__contasexec = contasexec

    @property
    def proggestcomexec(self):
        return self.__proggestcomexec

    @proggestcomexec.setter
    def proggestcomexec(self, proggestcomexec):
        self.__proggestcomexec = proggestcomexec

    @property
    def requerimentoexec(self):
        return self.__requerimentoexec

    @requerimentoexec.setter
    def requerimentoexec(self, requerimentoexec):
        self.__requerimentoexec = requerimentoexec
        
    @property
    def divida_ativaexec(self):
        return self.__divida_ativaexec

    @divida_ativaexec.setter
    def divida_ativaexec(self, divida_ativaexec):
        self.__divida_ativaexec = divida_ativaexec

    @property
    def atend_publicoexec(self):
        return self.__atend_publicoexec

    @atend_publicoexec.setter
    def atend_publicoexec(self, atend_publicoexec):
        self.__atend_publicoexec = atend_publicoexec
    
    @property
    def contasrpt(self):
        return self.__contasrpt
    
    @contasrpt.setter
    def contasrpt(self, contasrpt):
        self.__contasrpt = contasrpt

    @property
    def requerimentorpt(self):
        return self.__requerimentorpt

    @requerimentorpt.setter
    def requerimentorpt(self, requerimentorpt):
        self.__requerimentorpt = requerimentorpt

    @property
    def nome_arquivo(self):
        return self.__nome_arquivo

    @nome_arquivo.setter
    def nome_arquivo(self, nome_arquivo):
        self.__nome_arquivo = nome_arquivo

    @property
    def link_download(self):
        return self.__link_download

    @link_download.setter
    def link_download(self, link_download):
        self.__link_download = link_download