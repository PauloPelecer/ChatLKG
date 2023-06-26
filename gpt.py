from include import Keys,logo
import time
import openai
import os
import re
# Configuração da autenticação
openai.api_key = Keys.KeyIa()

def Digitar(text):
    print ('\033[0;33mGPT\033[0;31m:\033[0;m ')
    for c in text:
        print (c, end='', flush=True)
        time.sleep(0.05)


def obter_resposta(mensagem):
    
    # Enviando uma solicitação para a API
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=mensagem,
        max_tokens=700
    )

    resposta = response.choices[0].text.strip()
    resposta = re.sub(r'import ','\033[0;34mimport \033[0;m',resposta)
    resposta = re.sub(r'from ', '\033[0;34mfrom \033[0;m', resposta)
    resposta = re.sub(r'global ', '\033[0;34mglobal \033[0;m', resposta)

    resposta = re.sub(r' try', '\033[0;34m try\033[0;m',resposta)
    resposta = re.sub(r' except', '\033[0;34m except\033[0;m',resposta)
    resposta = re.sub(r' True', '\033[0;32m True\033[0;m',resposta)
    resposta = re.sub(r' as ', '\033[0;34m as \033[0;m',resposta)
    resposta = re.sub(r' False', '\033[0;31m False\033[0;m',resposta)
    resposta = re.sub(r'print', '\033[0;34mprint\033[0;m',resposta)
    resposta = re.sub(r'elif', '\033[0;34melif\033[0;m',resposta)
    resposta = re.sub(r'else', '\033[0;34melse\033[0;m',resposta)
    resposta = re.sub(r'if', '\033[0;34mif\033[0;m',resposta)
    resposta = re.sub(r'for ', '\033[0;34mfor \033[0;m',resposta)
    resposta = re.sub(r' in ', '\033[0;34m in \033[0;m',resposta)
    resposta = re.sub(r'while', '\033[0;34mwhile\033[0;m',resposta)
    resposta = re.sub(r'"', '\033[0;33m"\033[0;m',resposta)
    resposta = re.sub(r"'", "\033[0;33m'\033[0;m",resposta)
    resposta = re.sub(r'\(', '\033[0;34m(\033[0;m',resposta)
    resposta = re.sub(r'\)', '\033[0;34m)\033[0;m',resposta)
    resposta = re.sub(r'#', '\033[0;35m#\033[0;m',resposta)
    Digitar(resposta)
os.system('clear')
print (logo.LOGO())
while True:
    try:
        duvida = input(str('\n\033[0;32mUsuario\033[33m:\033[m '))
        obter_resposta(duvida)
    except KeyboardInterrupt:
        print ('Saindo...')
        time.sleep(0.5)
        break

    
    
