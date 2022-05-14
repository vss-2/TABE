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
echo "alias py=\"python3\"" >> ~/.bashrc
echo "alias py=\"python3\"" >> ~/.zshrc

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
echo "VideoSpeed https://github.com/igrigorik/videospeed"
echo "Tradutor https://addons.opera.com/pt-br/extensions/details/translator/"
echo "SaveFromNet https://addons.opera.com/pt-br/extensions/details/savefromnet-helper/"
echo "Return Youtube Dislike https://github.com/Anarios/return-youtube-dislike/"

alias telegram='cd ~/Telegram && ./Telegram'

# Backup diversos
alias backuplistaprogramasarq="mkdir ~/BackupListaProgramas && cp -r /usr/share/applications/ ~/BackupListaProgramas"
alias backupextensoesvscode="mkdir ~/ExtensoesVSCode && cp -r ~/.vscode/extensions/ ~/ExtensoesVSCode/"
alias backuplistaprogramasdpkg="dpkg --get-selections > ~/dpkg_get_selections.list"
alias restaurarlistaprogramasdpkg="sudo dpkg --set-selections < ~/dpkg_get_selections.list && sudo apt-get dselect-upgrade -y"
alias backuplistafontes="sudo cp -R /etc/apt/sources.list* ~/"
alias backupaptcompleto="sudo apt-key exportall > ~/apt_exportall.keys"
alias restauraraptcompleto="sudo apt-key add ~/apt_exportall.keys && sudo apt-get update && sudo apt-get install dselect"

sudo apt-get install zsh -y
sudo apt install zsh-syntax-highlighting
echo "source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ~/.zshrc

sudo apt install resolvconf
sudo systemctl enable resolvconf.service
sudo systemctl start  resolvconf.service
sudo echo "nameserver 8.8.8.8 \nnameserver 8.8.4.4\nnameserver 1.1.1.1" >> /etc/resolvconf/resolv.conf.d/head
sudo resolvconf --enable-updates
sudo resolvconf -u
