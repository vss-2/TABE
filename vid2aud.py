from subprocess import call

if __name__ == "__main__":
        link = input('Insira o link:\n')
        linkID = ''
        if(link[link.index('y')+5] == '.'):
                # Link encurtado
                linkID = link[link.index('y')+8]
                link_arg = 'https://youtube.com/watch?v=' + linkID
        call(['youtube-dl', link_arg, '-x', '--audio-extract', '\"m4a\"', '-o', '\"%(title)s.%(ext)\"'])
        return
