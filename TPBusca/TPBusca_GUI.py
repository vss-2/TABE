#!/usr/bin/python3

import os
from tkinter import *
from tkinter import messagebox
from subprocess import call

def trackerList():
        jaTemTL = os.listdir()
        if('trackerslist' in jaTemTL):
                messagebox.showwarning("Warning",'Já existe um diretório do OpenTrackerList, vou remover e pegar o mais atual no GitHub!')
                call(['rm', '-rf', 'trackerslist'])
        call(['git', 'clone', 'https://github.com/ngosang/trackerslist.git'])
        return

def OpenSubtitles(busca):
        busca = busca[0:len(busca)]
        busca = busca.replace(' ', '+')
        busca = busca.lower()
        busca = 'https://www.opensubtitles.org/pt/search2/sublanguageid-por,pob/moviename-'+busca
        call(['firefox', busca, 'nohup'])
        return

def apenasLink(busca):
        busca = busca[0:len(busca)]
        busca = busca.replace(' ', '+')
        cabeca = 'proxtpb.art/s/?q='
        cauda = '&page=0&orderby=99'
        output = cabeca+busca+cauda
        return output

def abrirFirefox(busca):
        link = apenasLink(busca)
        call(['firefox', link, 'nohup'])
        return

def estouComSorte(busca):
        call(['touch', 'pagina.txt'])
        output = apenasLink(busca)
        call(['curl', '-o', 'pagina.txt', 'https://'+output])
        call(['ls'])
        path   = os.getcwd() + '/pagina.txt'
        leitor = open(path, 'r')
        texto  = leitor.readlines()
        for linha in texto:
                if(linha.endswith('search phrase.</h2>')):
                        # Caso não for encontrado nenhum resultado
                        print('Não foram encontrados resultados, tente novamente')
                        break
                if(linha.startswith('<div class="detName">')):
                        melhorResultado = linha.split("\"")
                        print(melhorResultado[3])
                        call(['rm', 'pagina.txt'])
                        call(['touch', 'pagina.txt'])
                        call(['curl', '-o', 'pagina.txt', 'https://proxtpb.art'+melhorResultado[3]])
                        leitor2 = open(path, 'r')
                        texto2  = leitor2.readlines()
                        for linha2 in texto2:
                                if('magnet:?' in linha2):
                                        magnetlink = linha2.split("\"")
                                        magnetlink[3] = magnetlink[3].replace('amp;','')
                                        print(magnetlink[3])
                                        leitor.close()
                                        leitor2.close()
                                        call(['rm', 'pagina.txt'])
                                        call(['xdg-open', magnetlink[3]])
                                        # Baseado em: xdg-mime default deluge.desktop x-scheme-handler/magnet
                                        # call[('xdg-mime', 'default', 'transmission-gtk.desktop', 'x-scheme-handler/magnet')]
                                        break
                        break
        return

class Checkbar(Frame):
        def __init__(self, parent = None, picks = [], side = LEFT, anchor = W):
                Frame.__init__(self, parent)
                self.vars = []
                for pick in picks:
                        var = IntVar()
                        chk = Checkbutton(self, text = pick, variable = var)
                        chk.pack(side = side, anchor = anchor, expand = YES)
                        self.vars.append(var)
        def state(self):
                return map((lambda var: var.get()), self.vars)

if __name__ == '__main__':
        root = Tk()
        root.wm_title('TPBusca')
        inputBusca = StringVar()
        inputBuscaEntry = Entry(root, textvariable = inputBusca, width = 50)
        labelBusca = Label(root, text = 'Insira a busca: ', bd = 0)
        labelBusca.pack(side = TOP)
        inputBuscaEntry.pack(side = TOP)
        opcoes = Checkbar(root, ['Printar link', 'Abrir no Firefox', 'Estou com sorte (requer Transmission)', 'Baixar OpenTrackerList'])
        labelBusca.pack(side = TOP, fill = X)
        opcoes.pack(side = LEFT)
        print(opcoes.state())
        labelBusca.config(relief = GROOVE, bd = 0)

        def buscar():
                marcados = list(opcoes.state())
                busca_Old = inputBuscaEntry.get()
                if (marcados[0] == 1):
                        busca = apenasLink(busca_Old)
                        inputBuscaEntry.delete(0, len(busca_Old))
                        inputBuscaEntry.insert(0, busca)
                if (marcados[1] == 1):
                        abrirFirefox(busca_Old)
                if (marcados[2] == 1):
                        estouComSorte(busca_Old)
                if (marcados[3] == 1):
                        trackerList()
                return

        def limpar():
                inputBuscaEntry.delete(0, len(inputBuscaEntry.get()))
                return

        def allstates(): 
                # print(list(opcoes.state()))
                return

        Button(root, text='Sair', command=root.quit).pack(side=RIGHT)
        Button(root, text='Buscar', command=buscar).pack(side=RIGHT)
        Button(root, text='Limpar', command=limpar).pack(side=RIGHT)
        # Button(root, text='Printar', command=allstates).pack(side=RIGHT)
        root.mainloop()
