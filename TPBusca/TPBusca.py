import os
from subprocess import call

def trackerList():
	trackerList = input('Espera, gostaria de pegar a trackerlist mais recente? -y ou -n: ')
	if(trackerList == '-y'):
		jaTemTL = os.listdir()
		if('trackerslist' in jaTemTL):
			print('Já existe um diretório trackerslist, vou remover e pegar o mais recente!')
			call(['rm', '-rf', 'trackerslist'])
		call(['git', 'clone', 'https://github.com/ngosang/trackerslist.git'])
	else:
		print('OK!')
	return

def OpenSubtitles(busca):
	busca = busca[0:len(busca) - 2]
	busca = busca.replace(' ', '+')
	busca = busca.lower()
	busca = 'https://www.opensubtitles.org/pt/search2/sublanguageid-por,pob/moviename-'+busca
	call(['firefox', busca])
	return

def apenasLink(busca):
	busca = busca[0:len(busca) - 2]
	busca = busca.replace(' ', '+')
	cabeca = 'proxtpb.art/s/?q='
	cauda = '&page=0&orderby=99'
	output = cabeca+busca+cauda
	return output

def abrirFirefox(busca):
	link = apenasLink(busca)
	call(["firefox", link])
	return

def estouComSorte(busca):
	call(["touch", "pagina.txt"])
	output = apenasLink(busca)
	call(["curl", "-o", "pagina.txt", "https://"+output])
	call(["ls"])
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
			call(["rm", "pagina.txt"])
			call(["touch", "pagina.txt"])
			call(["curl", "-o", "pagina.txt", "https://proxtpb.art"+melhorResultado[3]])
			leitor2 = open(path, 'r')
			texto2  = leitor2.readlines()
			for linha2 in texto2:
				if("magnet:?" in linha2):
					magnetlink = linha2.split("\"")
					magnetlink[3] = magnetlink[3].replace('amp;','')
					print(magnetlink[3])
					leitor.close()
					leitor2.close()
					call(["rm", "pagina.txt"])
					call(["xdg-open", magnetlink[3]])
					# Baseado em: xdg-mime default deluge.desktop x-scheme-handler/magnet
					# call[("xdg-mime", "default", "transmission-gtk.desktop", "x-scheme-handler/magnet")]
					break
			break

	return

if __name__ == "__main__":
	print('Digite sua busca e depois: \n-a para abrir (FFox) ou \n-p para printar o link\n-l para abrir busca de legenda (OpenSubtitles) ou\n-s para pegar o magnet do primeiro (estou com sorte): ')
	busca = input()
	parametro = ''

	if(busca.endswith('p')):
		trackerList()
		print(apenasLink(busca))
		exit
	elif(busca.endswith('a')):
		trackerList()
		abrirFirefox(busca)
		exit
	elif(busca.endswith('s')):
		trackerList()
		estouComSorte(busca)
		exit
	elif(busca.endswith('l')):
		trackerList()
		OpenSubtitles(busca)
		exit
	else:
		print('O programa não recebeu parâmetros, encerrando!')
		trackerList()
		exit

# Input:
# Knightfall S02E01 1080p -s
# Output:
# Chamada para o seu aplicativo de torrent com o melhor resultado (se encontrado)
# Funcionamento, vai para página do torrent, que nem o -p faz
# Vê o primeiro torrent da lista, vê o link dele, abre sua página
# Na sua página busca pelo campo "magnet"
# Dá uma systemcall pro xdg-open chamar o programa associado ao torrent passando o magnet
