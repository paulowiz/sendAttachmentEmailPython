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

def executaRotina():
    load_dotenv()
    pasta = os.getenv("PASTA")
    if not len(os.listdir(pasta)) == 0:
        for i in os.listdir(pasta):
            if not i.endswith(".crdownload"):
                print(pasta+str(i))
                #try:
                data_e_hora_atuais = datetime.now()
                print(data_e_hora_atuais.strftime('%d/%m/%Y %H:%M'))
                enviaArquivos(pasta+str(i))
                os.remove(pasta+str(i))
                #except:
                #    print('Erro ao processar o arquivo!')
                #    os.remove(pasta+str(i))
        print('Rotina executada com sucesso!')

def  enviaArquivos(arquivo):
    with open('listaEmails.txt', 'r') as f:
        myfile = f.read().splitlines()
    f.close()
    print(myfile)
            
        #func = fc.funcoes()
        #try:
         #   file = func.convertToBinaryData(arquivo)
        #except:
         #   return print("Erro ao ler o arquivo.")
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