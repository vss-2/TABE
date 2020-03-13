#/bin/bash
cd $PWD
grep data-value=\"2 site.html >> lista.txt
grep selected lista.txt  >> dataAtual.txt
cut -c 161-170 lista.txt >> dataAtual2.txt
cut -c 113-122 lista.txt >> lista2.txt
cat dataAtual2.txt lista2.txt > listaFinal.txt
