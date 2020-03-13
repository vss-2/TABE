### Codec de vídeo mp4/h264 outputado do Kazam para WhatsApp e Telegram

``` ffmpeg -y -i input_file.mp4 -c:v libx264 -c:a aac -strict experimental -tune fastdecode -pix_fmt yuv420p -b:a 192k -ar 48000 output_file.mp4 ```

### Codec para extrair áudio do ```audio-recorder``` ou ```ocenaudio``` .flac e converter para .m4a 320kbps (vbr)
``` ffmpeg input_file.flac -ab 320000 output_file.flac ```

### Para saber informações do arquivo
``` ffprobe input_file.xyz ```

### Significado das flags:
* ```-y: Sobrescreve o output, sem perguntar```
* ```-i: Arquivo input```
* ```-c: a/v codec de audio/video```
* ```-pix_fmt: Formato de pixel```
* ```-b: a/v bitrate de audio/video```
* ```-ar: Frequência do audio```
