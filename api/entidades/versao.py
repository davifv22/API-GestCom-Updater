

class Versao():
    def __init__(self, tipo_sistema, versao, release, dt_upload, link_download, responsaveis):
        self.__tipo_sistema = tipo_sistema
        self.__versao = versao
        self.__release = release
        self.__dt_upload = dt_upload
        self.__link_download = link_download
        self.responsaveis = responsaveis


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
    def link_download(self):
        return self.__link_download

    @link_download.setter
    def link_download(self, link_download):
        self.__link_download = link_download

    @property
    def responsaveis(self):
        return self.__responsaveis

    @responsaveis.setter
    def responsaveis(self, responsaveis):
        self.__responsaveis = responsaveis