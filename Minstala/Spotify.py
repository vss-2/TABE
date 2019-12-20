import os
from subprocess import call

# Pega o diretório atual e muda o URL do ok.txt
path = os.getcwd()
path = path+'/versions.txt'
leitor = open(path, 'r+')
texto = leitor.readlines()
for linha in texto:
        continue
inicio = linha.index('href=')
fim    = linha.index('.deb\">')

# print(inicio, fim)
# print(linha[21+6:70+4]) Resultado esperado atingido
leitor.close()

arquivo = linha[inicio+6:fim+4]
download = 'http://packages.linuxmint.com/pool/import/s/spotify-client/' + arquivo

call(['wget',download,'-OSpotify.deb'])

'''
Input para o python vindo do Spotify.sh:
<tr><td class="n"><a href="spotify-client_1.0.27.71.g0a26e3b2-9_amd64.deb">spotify-client_1.0.27.71.g0a26e3b2-9_amd64.deb</a></td><td class="m">2016-Apr-18 08:08:13</td><td class="s">74.3M</td><td class="t">application/vnd.debian.binary-package</td></tr>
<tr><td class="n"><a href="spotify-client_1.0.55.487.g256699aa-16_amd64.deb">spotify-client_1.0.55.487.g256699aa-16_amd64.deb</a></td><td class="m">2017-May-29 11:00:57</td><td class="s">86.8M</td><td class="t">application/vnd.debian.binary-package</td></tr>
<tr><td class="n"><a href="spotify-client_1.0.64.407.g9bd02c2d-26_amd64.deb">spotify-client_1.0.64.407.g9bd02c2d-26_amd64.deb</a></td><td class="m">2017-Oct-27 10:21:46</td><td class="s">89.0M</td><td class="t">application/vnd.debian.binary-package</td></tr>
<tr><td class="n"><a href="spotify-client_1.0.80.480.g51b03ac3-13_amd64.deb">spotify-client_1.0.80.480.g51b03ac3-13_amd64.deb</a></td><td class="m">2018-Jun-17 04:39:19</td><td class="s">93.0M</td><td class="t">application/vnd.debian.binary-package</td></tr>
<tr><td class="n"><a href="spotify-client_1.0.92.390.g2ce5ec7d-18_amd64.deb">spotify-client_1.0.92.390.g2ce5ec7d-18_amd64.deb</a></td><td class="m">2018-Nov-28 08:49:58</td><td class="s">97.6M</td><td class="t">application/vnd.debian.binary-package</td></tr>
<tr><td class="n"><a href="spotify-client_1.1.5.153.gf614956d-16_amd64.deb">spotify-client_1.1.5.153.gf614956d-16_amd64.deb</a></td><td class="m">2019-Jul-10 10:58:01</td><td class="s">108.4M</td><td class="t">application/vnd.debian.binary-package</td></tr>

Output do Python, arquivo baixado Spotify.deb
'''