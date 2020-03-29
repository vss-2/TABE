# Shell Tools

### Mudar programas padrão (xdg-open) no Linux
Exemplo para mudar o programa de torrent padrão: <br>

Listando os programas <br>
``` gio mime x-scheme-handler/magnet ``` <br>
``` $ popcorn-time.desktop ``` <br>
``` $ transmission-gtk.desktop ``` <br>

Escolhendo os programas <br>
``` gio mime x-scheme-handler/magnet transmission-gtk.desktop ```
