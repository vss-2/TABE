import sys, os
from subprocess import call 
# Poderia usar o sys.argv para pegar os inputs passados do terminal btw

print('Vou te mostrar os arquivos mp3, m4a e wav disponiveis no diretorio atual ('+os.getcwd()+')\n')

itens = os.listdir(os.getcwd())
for item in itens:
    if(item.endswith('m4a') or item.endswith('mp3') or item.endswith('wav')):
        print(item)
print()

arq = input('Qual o arquivo (com sufixo): ')
opcao = input('Quer cortar o inicio, o fim ou ambos? ')

opcao = opcao.lower()

if(opcao == 'inicio'):
    ini = input('Insira o inicio, em segs: ')
    call(['ffmpeg', '-i', arq, '-ss', ini, '-acodec', 'copy', arq[:len(arq)-4]+'_novo'+arq[len(arq)-4:]])
elif(opcao == 'ambos'):
    ini = input('Insira o inicio, em segs: ')
    fim = input('Insira o fim, em segs: ')
    call(['ffmpeg', '-i', arq, '-ss', ini, '-t', fim, '-acodec', 'copy', arq[:len(arq)-4]+'_novo'+arq[len(arq)-4:]])
elif(opcao == 'fim'):
    fim = input('Insira o fim, em segs: ')
    call(['ffmpeg', '-i', arq, '-ss', '0', '-acodec', 'copy', arq[:len(arq)-4]+_novo+arq[len(arq)-4:]])
else:
    print('Voce escreveu errado ou tentou trollar o script, encerrando!')
    exit

print('So pra voce saber: criei um arquivo _novo, fim da execucao!')
exit

# Obs o formato de tempo pode ser:
# (int) em segundos, ex: 189, para 3min e 9seg
# (hh:mm:ss.mss), ex: 00:03:04.423, para 3min, 4seg e 423ms
# -acodec copy nao reencoda o arquivo, apenas corta o audio original
