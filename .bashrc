alias py='python3'
alias cd.='cd ..'

# Android Studio
export ANDROID_HOME=~/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools

# Flutter
export PATH=$PATH:$HOME/.local/bin:$HOME/bin:$HOME/Flutter/flutter/bin

# LAMPP
export PATH=$PATH:/opt/lampp/bin
alias xamppmanager="cd /opt/lampp/ && sudo ./manager-linux-x64.run"

# Miscellaneous
sed -i '13 a nameserver 8.8.8.8' /etc/resolv.conf
