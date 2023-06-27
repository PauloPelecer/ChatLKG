from include import Keys,logo
import time
import openai
import os
import re
# Configuração da autenticação
openai.api_key = Keys.KeyIa()



def Save(msg,filename):
    doc = 'Documentos'
    home = os.path.join(doc, filename)
    if os.path.exists(doc):
        with open(home, 'w') as file:
            file.write(msg[0])
            file.close()
            return "Arquivo Salvo!"
    else:
        print ('Criando Pasta ',doc,' Aguarde Alguns Segundos!')
        os.mkdir(doc)
        with open(home, 'w') as file:
            file.write(msg[0])
            file.close()
            return "Arquivo Salvo!"

    


def Exiting():
    n = 0
    p = str('')
    time.sleep(1)
    while n < 4:
        os.system('clear')
        print (logo.LOGO())
        print ('\nSaindo'+p)
        time.sleep(0.5)
        p += '.'
        n +=1




def Digitar(text):
    print ('\033[0;33mGPT\033[0;31m:\033[0;m ')
    for c in text:
        print (c, end='', flush=True)
        time.sleep(0.05)


def obter_resposta(mensagem):
    
    # Enviando uma solicitação para a API
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=mensagem,
        max_tokens=1024,
        temperature=0.5
    )

    Onemsg = [response.choices[0].message.content, response.usage]
    resposta = Onemsg[0]
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
    return Onemsg
os.system('clear')
print (logo.LOGO())
print ('''
\033[0;32m----------\033[0;33m+\033[0;m
\033[0;34mComandos\033[0;m: \033[0;32m|---------------------\033[0;33m+\033[0;m
 \033[0;33m/\033[0;34mSalvar  \033[0;32m|\033[0;34mPergunte Oque Quiser\033[0;33m!\033[0;32m|
 \033[0;33m/\033[0;34mSair    \033[0;32m|---------------------\033[0;33m+
\033[0;32m----------\033[0;33m+
\033[0;m
''')
while True:
    try:
        global text
        duvida = input(str('\n\033[0;32mUsuario\033[33m:\033[m '))
        if duvida == '/sair' or duvida == '/Sair':
            Exiting()
            break
        elif duvida == '/Salvar' or duvida == '/salvar':
            filename = input(str('\033[0;32mNome do Arquivo\033[0;33m:\033[0;m'))
            msg = Save(text, filename)
            Digitar(msg)
        else:
            quest = [{'role':'system','content':'Voce e um assistente gente boa.'}]
            quest.append({'role':'user','content': str(duvida)})
            text = obter_resposta(quest)

    except KeyboardInterrupt:
        Exiting()
        break

    
    
