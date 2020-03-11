import csv
from subprocess import call 

def tratarString(titulo, autor):
        return

if __name__ == "__main__":
        call(['curl', 'https://spotifycharts.com/regional/br/weekly/latest/download', '>>', 'arquivo.csv'])
        with open('arquivo.csv') as chartscsv:
                leitor_csv = csv.reader(chartscsv, delimiter=',')
                contador = 0
                for coluna in csv_reader:
                        if contador == 0:
                                continue
                        else: 
                                titulo = row[1]
                                autor = row[2]
                                tratarString(titulo, autor)
