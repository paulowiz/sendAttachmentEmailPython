﻿## 📚  Descrição 

RoboOCR foi criado com finalidade de ler os arquivos da pasta na rede \\fileserver01\Comprovantes que recebe todos os arquivos scaneados com o aplicativo OCR da SIMPRESS em formato TIF. Os arquivos reconhecidos são os comprovantes referente ao CTE - Conhecimento de Transporte e o RPA - Recibo de pagamento Autônomo.

Foi colocado uma chave única em cada documento que será lido pelo OCR e renomeará o arquivo escaneado com aquela chave:
Chave do CTE para os comprovantes do CTE:

```
  31191286613403002094570000000677971477521214.tif
 ```
Número do RPA, filial, empresa emitente e quantidade de paginas para o RPA:

```
  RPA-008239008-8-2000-2.tif
 ```  
<p>O robô pelas chaves informadas acima localiza a viagem atrelada no documento e salva o arquivo scaneado na tabela DOCTOS_ANEXOS do SIT  no formato PDF. Sendo assim possível a visualização do anexo  pela quitação e CEDOC com mais eficiência e rapidez.</p>

<p>Validações realizadas pelo robô no arquivo scaneado:</p>

- Consulta se existe viagem 
- Consulta se existe comprovante já anexado e faz o update caso exista.
- Verifica o tipo de arquivo anexado( espera-se o formato .TIF que é o padrão da impressora)
- Verifica chave do arquivo se está correta
- Pela chave identifica-se a empresa do documento direcionando automaticamente o banco que deve ser feita a ação (Transportes ,Logística ou Recintos) 

## 🚀 Tecnologias Usadas 

Python

## 📌 Estrutura do Projeto 
    |-- controller
         |--cte.py
         |--email.py
         |--functions.py
         |--rpa.py
    |-- database
         |--conexao.py
    |--  .env
    |-- __init__.py
    |-- requiriments.txt
    |-- README.md
## 📢 Como executar

Requisitos:

Python 3.7.5<br>

Instalar todas as depedências do python usando o arquivo requiriments.txt que está no projeto:  

```bash 
pip install  -r requiriments.txt
 ```  
 Executar o _main_.py no cmd com o comando:

```bash 
python _main_.py
 ```  
Assim irá startar o robô

## 🔓 Licença 
MIT © [Paulo Mota](https://www.linkedin.com/in/paulo-mota-955218a2/)
