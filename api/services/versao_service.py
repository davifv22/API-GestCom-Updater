from ..models import versao_model, versao_pacotes_model
from api.app import db, app
import rarfile, os, zipfile, shutil, datetime

def set_versao(versao):
    versao_bd = versao_model.Versao(
        tipo_sistema=versao.tipo_sistema,
        versao=versao.versao,
        release=versao.release,
        dt_upload=versao.dt_upload,
        link_download=versao.link_download)
    db.session.add(versao_bd)
    db.session.commit()
    return versao

def get_versao():
    versao_bd = versao_model.Versao.query.all()
    return versao_bd

def get_pacotes_versao():
    versao_bd = versao_pacotes_model.VersaoPacotes.query.all()
    return versao_bd

def get_versao_tipo_sistema(params):
    if params[-4:] == '.zip':
        vPacote = versao_pacotes_model.VersaoPacotes.query.filter_by(nome_arquivo=params).first()
        if vPacote: return True, vPacote
        else: return False, 'Pacote de versão expirado!'
    
    if params[:3] == 'MGF':
        if params[3:7] == '6031': True
        elif params[3:7] == '7008': True
        else: return False, 'Versão não foi encontrada!'
    elif params[:3] == 'PRO':
        if params[3:7] == '6031': True
        elif params[3:7] == '7008': True
        else: return False, 'Versão não foi encontrada!'
    elif params[:3] == 'REC':
        if params[3:7] == '1001': True
        else: return False, 'Versão não foi encontrada!'
    else:
        return False, 'Tipo de sistema não foi encontrado!'
    if True:
        return True, versao_model.Versao.query.filter_by(tipo_sistema=params).first()

def update_dados_versao(dados_novos, dados_antigos):
    dados_antigos.tipo_sistema = dados_novos.tipo_sistema
    dados_antigos.versao = dados_novos.versao
    dados_antigos.release = dados_novos.release
    dados_antigos.dt_upload = dados_novos.dt_upload
    
def delete_versao(tipo_sistema):
    db.session.delete(tipo_sistema)
    db.session.commit()
    
def set_versao_pacotes(vTipo, params):
    versao_base = versao_model.Versao.query.filter_by(tipo_sistema=vTipo).first()
    if versao_base:
        # Json request
        cidade = params['cidade']
        executaveis = params["arquivos"][0]["executaveis"]
        rpts = params["arquivos"][0]["rpts"]

        dir = app.config.get('DIR_VERSAO') # diretorio versao
        dir_temp = app.config.get('DIR_VERSAO_TEMP') # diretorio versao temp
        versao_arq = versao_base.nome_arquivo # nome versao base        
        pasta_temp = f'{vTipo}_{cidade}_{datetime.datetime.now().strftime("%Y%m%d%H%M")}' # criar nome da pasta
        os.mkdir(f'{dir_temp}/{pasta_temp}') # criar a pasta temp no diretorio
        
        arqs = []
        if vTipo[:3] == 'MGF':
            if executaveis[0]["gestcom"]: arqs.append('MGFGestcom.exe')
            if executaveis[0]["contas"]: arqs.append('MGFConta.exe')
            if executaveis[0]["proggestcom"]: arqs.append('progSuporteGestCom.exe') # pasta do prog
            if executaveis[0]["requerimento"]: arqs.append('MGFRequerimento.exe')
            if executaveis[0]["divida_ativa"]: arqs.append('MGFDividaAtiva.exe')
            if executaveis[0]["atend_publico"]: arqs.append('MGFAtendimentoPub.exe')
        elif vTipo[:3] == 'PRO':
            if executaveis[0]["pro"]: arqs.append('Pro.exe')
            if executaveis[0]["contas"]: arqs.append('ProMFC.exe')
            if executaveis[0]["proggestcom"]: arqs.append('progSuporteGestCom.exe') # pasta do prog
            if executaveis[0]["requerimento"]: arqs.append('ProMREQ.exe')
            if executaveis[0]["divida_ativa"]: arqs.append('ProMDA.exe')
            if executaveis[0]["atend_publico"]: arqs.append('ProMAC.exe')
        elif vTipo[:3] == 'REC': arqs.append('MGFRecebimentos.exe')
        else: return False, 'Tipo de sistema não foi encontrado!'

        if rpts[0]["contas"]: arqs.append('conta.rpt')
        if rpts[0]["requerimento"]: arqs.append('requerimentosdiversos.rpt')


        with rarfile.RarFile(f'{dir}/{versao_arq}', "r") as rar: # Abre e extrai a versão base
            for file in arqs:
                with open(os.path.join(f'{dir_temp}/{pasta_temp}', file), "w") as f: # abre pasta personalizada
                    f.write(file) # extrai arquivos necessarios
                    f.close()

        with zipfile.ZipFile(f'{dir_temp}/{pasta_temp}.zip', 'w', zipfile.ZIP_DEFLATED) as zip:
            for root, dirs, files in os.walk(f'{dir_temp}/{pasta_temp}'):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, f'{dir_temp}/{pasta_temp}')
                    zip.write(file_path, arcname=arcname)

        shutil.rmtree(f'{dir_temp}/{pasta_temp}') # Exclui a pasta temp
        
        # adicionar no banco de dados
        versao_pacote_bd = versao_pacotes_model.VersaoPacotes(
            tipo_sistema = versao_base.tipo_sistema,
            versao = versao_base.versao,
            release = versao_base.release,
            dt_upload = params['data_hora'],
            nome_maquina = params['nome_maquina'],
            cidade = cidade,
            gestcomexec = executaveis[0]["gestcom"],
            proexec = executaveis[0]["pro"],
            contasexec = executaveis[0]["contas"],
            proggestcomexec = executaveis[0]["proggestcom"],
            requerimentoexec = executaveis[0]["requerimento"],
            divida_ativaexec = executaveis[0]["divida_ativa"],
            atend_publicoexec = executaveis[0]["atend_publico"],
            contasrpt = rpts[0]["contas"],
            requerimentorpt = rpts[0]["requerimento"],
            nome_arquivo = f'{pasta_temp}.zip',
            link_download = f'{app.config.get("SERVER_URL")}/versao/download/{pasta_temp}.zip'
            )
        db.session.add(versao_pacote_bd)
        db.session.commit()
        
        return True, versao_pacote_bd