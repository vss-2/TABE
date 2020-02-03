### Lista de comandos úteis para usar no meu Termux

#### Codec bom para reduzir qualidade do ScreenRecorder padrão da MIUI
``` ffmpeg -i input_file.mp4 -c:v libx264 -c:a aac -filter:a "volume=2.0" -pix_fmt yuv420p -b:a 192k -ar 44100 output_file.mp4 ```

#### Em ordem crescente de maior detalhamento sobre o arquivo dado
``` file arquivo.formato``` <br>
``` ls -lh arquivo.formato``` <br> 
``` lsattr arquivo.formato``` <br>
``` stat arquivo.formato```

#### Busca arquivos + filtra por resultado
``` ls | grep busca ```

#### Atalhos do youtube-dl
Vai extrair o áudio do link, converter para m4a, e depois salvar na pasta específica <br>
``` youtube-dl LINK -x --audio-format "m4a" -o "~/storage/shared/Music/%(title)s.%(ext)s"```

#### Firefox Nightly Settings Pessoais
* Baixar qualquer versão 08/18
* ``` about:config ```
* ``` layout.css.devPixelsPerPx ``` de -1 para 2 (ou menos)
* Baixar addon: ``` User Agent Switcher ``` settar para Firefox Windows (v63.0 pra cima), aplicar
* Baixar addon: ``` uBlock Origin ``` settar nos ``` My Filters ``` : <br>
``` ||www.link.com/*$document,domain=www.link.com ``` e salvar
