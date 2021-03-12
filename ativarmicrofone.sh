if [ $1 -eq 1 ]
then
	exec pactl load-module module-loopback
else
	exec pactl unload-module module-loopback
fi
