from subprocess import call

if __name__ == "__main__":
        print('Se qualquer coisa der errado, verifique se há: ffmpeg E youtube-dl, ambos atualizados')
        link = input('Insira o link:\n')
        linkID, link_arg = '', ''
        if(link[link.index('y')+5] == '.'):
                # Link encurtado
                linkID = link[link.index('y')+8]
                link_arg = 'https://youtube.com/watch?v=' + linkID
        elif(len(link) > 43):
                # Provável link padrão de playlist ou com timestamp
                link_arg = link[:43]
        call(['youtube-dl', link_arg, '-x', '--audio-extract', '\"m4a\"', '-o', '\"%(title)s.%(ext)\"'])
        return
