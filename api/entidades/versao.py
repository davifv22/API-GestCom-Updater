

class Versao():
    def __init__(self, tipo_sistema, versao, release, dt_upload, nome_arquivo, link_download):
        self.__tipo_sistema = tipo_sistema
        self.__versao = versao
        self.__release = release
        self.__dt_upload = dt_upload
        self.__nome_arquivo = nome_arquivo
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