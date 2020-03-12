# -*- coding: utf-8 -*-

import csv
from subprocess import call 

if __name__ == "__main__":
        print('Escolha a semana 1, depois a semana 2')
        call(['curl', 'https://spotifycharts.com/regional/br/weekly/latest/download', '>>', 'semana1.csv'])
        call(['curl', 'https://spotifycharts.com/regional/br/weekly/latest/download', '>>', 'semana2.csv'])

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