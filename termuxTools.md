### Lista de comandos úteis para usar no meu Termux

#### Codec bom para reduzir qualidade do ScreenRecorder padrão da MIUI
``` ffmpeg -i input_file.mp4 -c:v libx264 -c:a aac -pix_fmt yuv420p -b:a 192k -ar 44100 output_file.mp4 ```

#### Em ordem crescente de maior detalhamento sobre o arquivo dado
``` file arquivo.formato``` <br>
``` ls -lh arquivo.formato``` <br> 
``` lsattr arquivo.formato``` <br>
``` stat arquivo.formato```

#### Busca arquivos + filtra por resultado
``` ls | grep busca ```
