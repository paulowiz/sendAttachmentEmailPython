import sys
import os
import io 
import time
import datetime
import schedule 
from datetime import datetime
from controller import email as em
from controller import functions as fc
from dotenv import load_dotenv
import pandas as pd

fcp = fc.funcoes() 
df =  pd.DataFrame(columns=['A'])

def listar_pasta(pasta):
    i = 0
    tamanho_arquivo =0
    subpastas = list()
    if os.path.isdir(pasta):
        items = os.listdir(pasta)
        for item in items:
            novo_item = os.path.join(pasta,item)
            if os.path.isdir(novo_item):
                subpastas.append(novo_item)
                continue
            caminho_completo = pasta+'\\'+item
            nome_do_arquivo = item
            data_e_hora_atuais = datetime.now()
            data_arquivo = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
            diretorio = pasta
            tamanho_arquivo = os.path.getsize(caminho_completo)
            print(pasta+'\\'+item)
            enviaArquivos(caminho_completo)
            #os.remove(pasta+str(i))
            log = caminho_completo+';'+data_arquivo+';'+diretorio+';'+str(nome_do_arquivo)+';'+str(tamanho_arquivo)
            fcc = fc.funcoes() 
            fcc.insereDf(df,log)
                    
        
        for subpasta in subpastas:
            listar_pasta(subpasta)
                   
    return df



def executaRotina():
    load_dotenv()
    path = os.getenv("PASTA")
    pastas = os.listdir(path)
    for pasta in pastas:
        if os.path.isdir(pasta):
            listar_pasta(path+pasta)
        else:
            file = path+pasta
            if not file.endswith(".exe") and not file.endswith(".zip"):
                enviaArquivos(file)  
    fcp.geraExcel(df,'logFRE','Logs')

        
        
def  enviaArquivos(arquivo):
    with open('listaEmails.txt', 'r') as f:
        myfile = f.read().splitlines()
    f.close()
    print(myfile)
    for line in myfile:
        mail = em.email()
        mail.enviaEmail(line,arquivo)
        print('email: '+line)
        
       
       
load_dotenv()
if os.getenv("TEMPO") is None:
    print('ATENÇÃO! Variavel TEMPO no .env está nula ou é inválida! foi setada para rodar acada 5 segundos em default')
     
else:
    schedule.every(float(os.getenv("TEMPO"))).minutes.do(executaRotina)

while True:
    schedule.run_pending()
    time.sleep(1)