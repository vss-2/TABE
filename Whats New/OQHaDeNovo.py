# -*- coding: utf-8 -*-

import csv
from tkinter import *
from subprocess import call 

#####################################################################################################
call(['curl', 'http://spotifycharts.com/regional', '>>', 'site.html'])
call(['bash', 'filtro.sh'])

paises = [
"global", "us - United States", "gb - United Kingdom", "ad - Andorra",
"ar - Argentina", "at - Austria", "au - Australia", "be - Belgium", "bg - Bulgaria",
"bo - Bolivia", "br - Brazil", "ca - Canada", "ch - Switzerland", "cl - Chile",
"co - Colombia", "cr - Costa Rica", "cy - Cyprus", "cz - Czech Republic",
"de - Germany", "dk - Denmark", "do - Dominican Republic", "ec - Ecuador",
"ee - Estonia", "es - Spain", "fi - Finland", "fr - France", "gr - Greece",
"gt - Guatemala", "hk - Hong Kong", "hn - Honduras", "hu - Hungary", "id - Indonesia",
"ie - Ireland", "il - Israel", "in - India", "is - Iceland", "it - Italy", "jp - Japan",
"lt - Lithuania", "lu - Luxembourg", "lv - Latvia", "mc - Monaco", "mt - Malta", "mx - Mexico",
"my - Malaysia", "ni - Nicaragua", "nl - Netherlands", "no - Norway", "nz - New Zealand",
"pa - Panama", "pe - Peru", "ph - Philippines", "pl - Poland", "pt - Portugal", "py - Paraguay",
"ro - Romania", "se - Sweden", "sg - Singapore", "sk - Slovakia", "sv - El Salvador", "th - Thailand",
"tr - Turkey", "tw - Taiwan", "uy - Uruguay", "vn - Viet Nam", "za - South Africa"
]

base = Tk()
base.configure(background='#1db954')
base.wm_title('What\'s New')

selectPlace = Label(base, text = 'Selecione lugar', background='#1db954')
selectPlace.grid(row = 0, column = 3)


# Lista que vai ter os países
paisList = Listbox(base, height = 10, width = 35)
paisList.grid(row = 10, column = 0, rowspan = 8, columnspan = 6)
for pais in paises:
        paisList.insert(END, pais)

freq = Listbox(base, height = 2, width = 8)
freq.grid(row = 10, column = 40, rowspan = 8, columnspan = 6)

freq.insert(END, 'Diário')
freq.insert(END, 'Semanal')

semana = Listbox(base, height = 10, width = 35)
semana.grid(row = 10, column = 80, rowspan = 8, columnspan = 6)

base.mainloop()
#####################################################################################################

if __name__ == "__main__":
        hashmap = {'musica': 'aparições'}
        novasmus = []
        with open('semana1.csv') as chartscsv:
                leitor_csv = csv.reader(chartscsv, delimiter=',')
                contador = 0
                for row in csv_reader:
                        if contador == 0:
                                continue
                        else:                         
                                # Retira acentos, cedilhas e tudo que não for ascii-safe
                                titulo1 = bytes(row[1], 'utf-8').decode('ascii','ignore')
                                autor1  = bytes(row[2], 'utf-8').decode('ascii','ignore')
                                musica = titulo1 + ' de ' + autor1
                                hashmap[musica] = 1
        with open('semana2.csv') as chartscsv:
                leitor_csv = csv.reader(chartscsv, delimiter=',')
                contador = 0
                for row in csv_reader:
                        if contador == 0:
                                continue
                        else:
                                titulo1 = bytes(row[1], 'utf-8').decode('ascii','ignore')
                                autor1  = bytes(row[2], 'utf-8').decode('ascii','ignore')
                                musica = titulo1 + ' de ' + autor1
                                hashmap[musica] = hashmap[musica] + 1
                                if(hashmap[musica] > 1):
                                        novasmus.append(musica)
        print(novamus)
