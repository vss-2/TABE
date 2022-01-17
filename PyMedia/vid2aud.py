from subprocess import call

class colors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

def cortador_ID(idk):
        if(idk.startswith('youtube.com/watch?v=')):
                idk = idk[20:31]
        elif(idk.startswith('youtu.be/')):
                idk = idk[9:20]
        return idk

def identificador(url):
        # Cada elif remove da string o começo
        if(url.startswith('http://www.')):
                url = url[11:]
                return cortador_ID(url)
        elif(url.startswith('https://www.')):
                url = url[12:]
                return cortador_ID(url)
        elif(url.startswith('www.')):
                url = url[4:]
                return cortador_ID(url)
        elif(url.startswith('youtube.com/watch?v=')):
                # Provavelmente já tá no formato youtube.com/ID
                return url[20:31]
        else:
                print('ID não identificado, encerrando!')
                return exit()


if __name__ == "__main__":
        print('Se qualquer coisa der errado, verifique se há: ffmpeg E youtube-dl, ambos atualizados!')
        link = input('Insira o link:\n')
        link_arg = identificador(link)
        if(link_arg == ''):
                print('Link vazio')
                exit()
        else:
                print(colors.WARNING + 'Iniciando download de: ' + colors.ENDC)
                call(['youtube-dl', '-e', link_arg])
                call(['youtube-dl', '-x', '--audio-format', str("m4a"), '-o', str("%(title)s.%(ext)s"), link_arg])
        exit()
