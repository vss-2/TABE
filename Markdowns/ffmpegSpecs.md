### Codec de vídeo mp4/h264 outputado do Kazam para WhatsApp e Telegram
``` ffmpeg -y -i input_file.mp4 -c:v libx264 -c:a aac -strict experimental -tune fastdecode -pix_fmt yuv420p -b:a 192k -ar 48000 output_file.mp4 ```

### Codec para extrair áudio do ```audio-recorder``` ou ```ocenaudio``` .flac e converter para .m4a 320kbps (vbr)
``` ffmpeg input_file.flac -ab 320000 output_file.m4a ```

### Extrair áudio baixado do youtube-dl
``` ffmpeg input_file.mp4 -x --audio-format "m4a" -ab 320000 output_file.m4a  ```

### Para saber informações do arquivo
``` ffprobe input_file.xyz ```

### Cortando vídeo do começo até 1hr 1min e 25s
``` ffmpeg -ss 00:00:00 -i input.mp4 -to 01:01:25 -c copy output.mp4```

### Convertendo vídeo para gif
``` ffmpeg -i input.mp4 -vf "fps=10,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output_gif.gif ```

### Significado das flags:
* ```-y: Sobrescreve o output, sem perguntar```
* ```-i: Arquivo input```
* ```-c: a/v codec de audio/video```
* ```-pix_fmt: Formato de pixel```
* ```-b: a/v bitrate de audio/video```
* ```-ar: Frequência do audio```
* ```-an: Remove áudio```
* ```-loop: Repetir o vídeo, quando terminar exibição```
* ### Especificação avançada:
* ```fps=10,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse```
*  O vídeo vai ter 10fps;
*  A escala usada preservará a proporção usando 480 como base (a largura);
*  Será usado o algoritmo de Lanczos (matrizes de eigenvectors) para conversão;
*  Split permite trabalhar com múltiplas inputs e outputs. Acontece: ```split[output1][output2]```; no ```[s0]palettegen[p]```, s0 é input e p é output, assim por diante.
