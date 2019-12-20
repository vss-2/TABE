
############################ Baixa o Spotify mais recente, instala e roda ##########################
curl -s http://packages.linuxmint.com/pool/import/s/spotify-client/ | grep _amd64.deb > versions.txt
mkdir Spotify
python3 Spotify.py
mv Spotify.deb Spotify
mv versions.txt Spotify
cd Spotify
ar x Spotify.deb
tar xvzf data.tar.gz
$localSpotify=$(pwd)
cd usr
cd bin
mv $(pwd)/spotify $(pwd)/Spotify
./Spotify &


################################# Criando Atalho no Desktop ########################################

# Criando atalho
cd ~/Desktop

echo '
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec=${localSpotify}/usr/bin/Spotify
Name=Spotify
Comment=Spotify
Icon=${!localSpotify}/share/spotify/icons/spotify-linux-512.png
' >> Spotify.desktop
chmod +x Spotify.desktop

# grep _amd64.deb, pega as linhas que tem _amd64.deb
# wc -l lê a quantidade de linhas
# sed 'Xd' arquivo, deleta as X linhas do arquivo

:'
curl -s http://packages.linuxmint.com/pool/import/s/spotify-client/ | grep _amd64.deb > ok.txt | wc -l ok.txt > lines.txt  | sed '$d' ok.txt
wc -l ok.txt
'