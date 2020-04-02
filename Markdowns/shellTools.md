# Shell Tools

### Mudar programas padrão (xdg-open) no Linux
Exemplo para mudar o programa de torrent padrão: <br>

Listando os programas <br>
``` gio mime x-scheme-handler/magnet ``` <br>
``` $ popcorn-time.desktop ``` <br>
``` $ transmission-gtk.desktop ``` <br>

Escolhendo os programas <br>
``` gio mime x-scheme-handler/magnet transmission-gtk.desktop ```

### Compartilhando arquivos de forma local usando pacote ``` woof ``` <br>
Compartilhando um arquivo, após concluído o woof irá encerrar. <br>
``` woof ~/DIRETORIO/arquivo.file ```

Compartilhando um arquivo por 5 vezes, após concluído o woof irá encerrar. <br>
``` woof -c 5 ~/DIRETORIO/arquivo.file ```

Compartilhando usando ip e porta definidos <br>
``` woof -i 127.0.0.1 -p 8080 ~/DIRETORIO/arquivo.file ```

Compartilhando arquivo compactando antes de disponibilizá-lo {-z: gzip, -j: bzip2, -Z: ZIP, -U: sem compressão} <br>
``` woof -Z ~/DIRETORIO/arquivo.file ```

Recebendo arquivo no dispositivo usando woof <br>
``` woof -U ```
