from datetime import datetime,timedelta
import os
import logging
import shutil

lista_dados = []
caminho = '/home/hitallo/valcann/backupsFrom'
lista_arquivos = os.listdir(caminho)
caminho_backup = '/home/hitallo/valcann/backupsTo'
caminho_log_backup = '/home/hitallo/valcann/'
caminho_log_To = '/home/hitallo/valcann/'



for arquivo in lista_arquivos:
    # tamanho dos arquivos
    tamanho = os.stat(f'{caminho}/{arquivo}').st_size
    # data de criacao
    data_criacao = os.path.getctime(f'{caminho}/{arquivo}')
    # data da ultima modificacao
    data = os.path.getmtime(f'{caminho}/{arquivo}')
    # lista completa
    lista_dados.append((data, arquivo, data_criacao, tamanho))

logging.basicConfig(filename=f'{caminho_log_backup}/backupsFrom.log' , level=logging.DEBUG)
logging.basicConfig(filename=f'{caminho_log_To}/backupsTo.log', level=logging.DEBUG)
lista_dados.sort(reverse=True)

logging.debug("verificando datas")
for arquivo in lista_dados:

    tempo_modificado = arquivo[0]
    date_time = datetime.fromtimestamp(tempo_modificado)
    now = date_time.now()
    tempo_exclusao = now - timedelta(3)

    if tempo_exclusao >= date_time:
        # deletando arquivos com mais de 3 dias
        os.remove(f'{caminho}/{arquivo[1]}')
        print(f'Deletado o arquivo:{arquivo[1]}.')
        # logs de acoes
        logging.debug(f'Hoje: {now}, data dos arquivos: {date_time}')
        logging.debug("Deletando arquivos")


    elif tempo_exclusao <= date_time:
        # copiando arquivos para o caminho
        shutil.copy2(f'{caminho}/{arquivo[1]}',caminho_backup)
        # log de acoes
        logging.warning(f'salvando arquivos {arquivo[1]} em {caminho_backup}')

