import os
import pyqrcode
import subprocess
from subprocess import call, Popen, PIPE
from tkinter import *
from tkinter import filedialog

URL_padrao   = ''
porta_padrao = '8080'

def descobrirIPlocal():
        # Vejo qual o ip e pego o que vai hostear o arquivo 
        # (aparentemente o último IP é o seu IP local)
        URL_padrao = ''
        with Popen(['ifconfig'], stdout=PIPE, universal_newlines=True) as processo:
                for linha in processo.stdout:
                        if(linha.strip().startswith('inet ')):
                                # A linha que contém o IP começa com 'inet <ip> '
                                # nos meus testes, a última é a do IP local
                                # Removo os espaços e pego o IP
                                strip_linha = linha.strip()
                                posicoes = list()
                                for esp in range(0,len(strip_linha)):
                                        if(strip_linha[esp] == ' '):
                                                posicoes.append(int(esp))
                                URL_padrao = str(strip_linha[posicoes[0]+1:posicoes[1]])
        return URL_padrao

if __name__ == "__main__":
        print('Escolha um arquivo do diretório atual para compartilhar')
        base = Tk()
        arquivo = filedialog.askopenfilename(filetypes = [('All files', '*.*' )] )
        base.destroy()
        
        print('Local e arquivo selecionado: '+str(arquivo))
        
        bool_zip = str(input('Vai querer em formato .zip? (s/n) '))
        bool_url = str(input('Vai querer hostear na URL padrão? (s/n) '))
        
        if(bool_url.strip().lower().startswith('n')):
                URL_padrao   = input('Insira a url desejada no formato IPv4/IPv6: XXX.YYY.ZZZ.WWW: ')
                porta_padrao = input('Insira a porta desejada no formato: KKKK: ')
        
        URL_padrao = descobrirIPlocal()

        url = pyqrcode.create(str(URL_padrao)+':'+str(porta_padrao))
        print(url.terminal(quiet_zone=1))
        
        if (bool_zip.lower().strip().startswith('s')):
                call(['woof', '-i', URL_padrao, '-p', porta_padrao, '-Z', arquivo]) 
        else:
                call(['woof', '-i', URL_padrao, '-p', porta_padrao, arquivo])
        
        exit
