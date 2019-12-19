cd ~
mkdir Spotify
cd Spotify
curl -s http://packages.linuxmint.com/pool/import/s/spotify-client/ | grep _amd64.deb > ok.txt
python3 Spotify.py
ar x Spotify.deb
tar xvzf data.tar.gz
cd usr
cd bin
./spotify

# Criando atalho
~/Desktop/Spotify.desktop

##!/usr/bin/env xdg-open
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec=/snap/bin/skype
Name=Skype
Comment=Skype
Icon=/snap/skype/23/usr/share/icons/hicolor/256x256/apps/skypeforlinux.png

# grep _amd64.deb, pega as linhas que tem _amd64.deb
# wc -l lê a quantidade de linhas
# sed 'Xd' arquivo, deleta as X linhas do arquivo

:'
curl -s http://packages.linuxmint.com/pool/import/s/spotify-client/ | grep _amd64.deb > ok.txt | wc -l ok.txt > lines.txt  | sed '$d' ok.txt
wc -l ok.txt
'