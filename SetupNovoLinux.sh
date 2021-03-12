# Pacote de ícones Papirus
sudo add-apt-repository ppa:papirus/papirus
# Gravador de tela SimpleScreenRecorder
sudo add-apt-repository ppa:maarten-baert/simplescreenrecorder
# Streaming de música Spotify
curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | sudo apt-key add - 
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
# KDEnLive
sudo add-apt-repository ppa:kdenlive/kdenlive-stable
# SimpleScreenRecorder
sudo apt-add-repository ppa:maarten-baert/simplescreenrecorder

# Atualização da lista de repositórios
sudo apt-get update
# Instalação dos supracitados e mais alguns
sudo apt install git
sudo apt install gimp
sudo apt install nodejs
sudo apt install npm
sudo apt install python3-pip
sudo apt install vlc-bin
sudo apt install gparted
sudo apt install kdenlive
sudo apt-get install spotify-client
sudo apt-get install papirus-icon-theme
sudo apt-get install simplescreenrecorder

mkdir Github

# Downloads
mkdir Programas
cd Programas
wget -O discord.deb https://discord.com/api/download?platform=linux&format=deb
wget -O opera.deb https://download.opera.com/download/get/?partner=www&opsys=Linux
wget -O vscode.deb https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64

# Atalhos
alias py='python3'

# Config manual
# "https://www.leaseweb.com/labs/2013/07/5-crucial-optimizations-for-ssd-usage-in-ubuntu-linux/"
echo "editar: nano /etc/fstab adicionar: none /tmp tmpfs defaults 0 0"
echo "rodar: echo -e "vm.swappiness=0" | sudo tee -a /etc/sysctl.conf"
echo "ativar: echo -e "#\x21/bin/sh\\nfstrim -v /" | sudo tee /etc/cron.daily/trim permitir: sudo chmod +x /etc/cron.daily/trim"

# Ir em tema ligar o tema escuro baixar "qob" ou "arc"
# Painel 28px
# Fontes: todas 11
echo "temas: https://www.cinnamon-look.org/p/1247470/"

# xed
echo "xed tema: https://draculatheme.com/gedit/"

# Firefox
# Homepage, Download localização específica

# Opera
# Meliuz, Tradutor, Video Downloader, Guias (por frequencia), Rastreadores e Anúncios, FFMPEG-fix, Download localização específica
alias telegram='cd ~/Telegram && ./Telegram'
