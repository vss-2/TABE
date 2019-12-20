
############################ Baixa o Spotify mais recente, instala e roda ##########################
curl -s http://packages.linuxmint.com/pool/import/s/spotify-client/ | grep _amd64.deb > versions.txt
mkdir Spotify
python3 Spotify.py
mv Spotify.deb Spotify
mv versions.txt Spotify
cd Spotify
localSpotify=$(pwd)
ar x Spotify.deb
tar xvzf data.tar.gz
cd usr
cd bin
mv $(pwd)/spotify $(pwd)/Spotify
./Spotify &


################################# Criando Atalho no Desktop ########################################

# Criando atalho

echo ${localSpotify}
echo "[Desktop Entry]" >> Spotify.desktop
echo "Version=1.0" >> Spotify.desktop
echo "Type=Application" >> Spotify.desktop
echo "Terminal=false" >> Spotify.desktop
execPlace="Exec=${localSpotify}/usr/bin/Spotify"
echo ${execPlace} >> Spotify.desktop
echo "Name=Spotify" >> Spotify.desktop
echo "Comment=Spotify" >> Spotify.desktop
iconPlace="Icon=${localSpotify}/usr/share/spotify/icons/spotify-linux-512.png"
echo ${iconPlace} >> Spotify.desktop

chmod +x Spotify.desktop
mv Spotify.desktop ~/Desktop

# grep _amd64.deb, pega as linhas que tem _amd64.deb
# wc -l lê a quantidade de linhas
# sed 'Xd' arquivo, deleta as X linhas do arquivo

# curl -s http://packages.linuxmint.com/pool/import/s/spotify-client/ | grep _amd64.deb > ok.txt | wc -l ok.txt > lines.txt  | sed '$d' ok.txt
# wc -l ok.txt