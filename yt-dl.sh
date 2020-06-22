if [ $2 = "pc" ]
then
	youtube-dl $1 -x --audio-format "m4a" --audio-quality 320K -o "~/Música/%(title)s.%(ext)s"
else
	youtube-dl $1 -x --audio-format "m4a" --audio-quality 320K -o "~/storage/shared/Music/%(title)s.%(ext)s"
fi
