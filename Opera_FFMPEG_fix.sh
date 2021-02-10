echo 'Download and extract the latest lib for your Linux version: https://github.com/iteufel/nwjs-ffmpeg-prebuilt/releases/'
sudo mkdir -p /usr/lib/chromium-browser
sudo cp libffmpeg.so /usr/lib/chromium-browser
sudo chmod 555 /usr/lib/chromium-browser/libffmpeg.so
sudo ldconfig
