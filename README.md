
## 💌  Send Email with any kind of attachment from a folder 

![email](https://user-images.githubusercontent.com/18649504/83364148-5e7d6a00-a375-11ea-94d9-0a063b5f8f4f.gif)

## 📚  Description

   Monitoring a folder with this bot and when this folder would have a file, my bot will take this file and send it as email to a list of emails from a txt<br>

## 🚀 Technologies have used 

<img src="https://user-images.githubusercontent.com/18649504/66262823-725cd600-e7be-11e9-9cea-ea14305079db.png" width = "100">
<img src ="https://user-images.githubusercontent.com/18649504/66262944-91f4fe00-e7c0-11e9-979d-2f370d1ebbbc.png" width = "100">

## Structure's Project 📌

    |-- controller
         |--email.py
         |--functions.py
    |-- .env
    |-- database
    |-- _init_.py
    |-- listaEmails.txt
    |-- requirements.txt

## 📢 How to use

Required:

Python 3.7.5 or more<br>
Node 10x<br>
Tips about Linux's Environment:<br>
Before everything you need to rum this command:
```bash 
sudo apt update
```
Install Python 3:
```bash 
sudo apt-get install python3
```
Install pip 3:
```bash 
sudo apt-get install python3-pip
```
Install Node:
```bash 
sudo apt install nodejs
```
Install npm:
```bash 
sudo apt install npm
```
Create specific tables in your database,executing script below:
```bash 
script_bd.sql
```
Install all python's dependencies with script below:  

```bash 
pip install  -r requiriments.txt
pip3 install  -r requiriments.txt(linux)
 ```  
Install lib "pm2" on your node.js with NPM:

```bash 
npm install -g pm2
```
After every installations you can execute the bot,at directory's project with console CMD:  
```bash 
pm2  start  _init_.py
```
if your linux has other versions installed, you need to use:  
```bash 
pm2  start  _init_.py --interpreter python3
```
#TIPS PM2#

List all bots:
```bash 
pm2  list
```
Stop a bot:
```bash 
pm2  stop _init_.py
```
Show bot's log:
```bash 
pm2  logs _init_.py
```
There are many commands on PM2 you can see at all in its documentation https://www.npmjs.com/package/pm2.

## 🔓 Licença 
MIT © [Paulo Mota](https://www.linkedin.com/in/paulo-mota-955218a2/)

