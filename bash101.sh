!/bin/bash
# Simples shebang (parâmetros pro sistema)
# Está só dizendo que é pra executar o bash,
# que se espera estar na pasta bin.
# Você pode checar quais shells existem
# no sistema através do comando: cat /etc/shells
# Pode verificar qual destes o seu terminal usa: which bash

# Comandos mais simples
# tac: Faz o cat ao contrário, ou seja, printa na ordem inversa
# which $cmd: Exibe qual arquivo está sendo executado na chamada do comando
# ls -alh: Exibe conteúdo de forma detalhada do diretório atual
# ls -ltr: Exibe os arquivos no formato Longo, na ordem inveRsa de daTa
# du -h: Exibe o tamanho do diretório em KiloBytes
# head $file: Printa as primeiras 10 linhas do arquivo
# tail $file: Printa as ultimas 10 linhas do arquivo
# chmod +x: Torna o arquivo .sh executável
# cp $fileIn $fileOut: Copia o conteúdo do arquivo in para o outro
# cp $fileIn ... $dirTarget: Copia o conteúdo do arquivo para o diretório destino
# Obs: cp aceita o -r para copiar diretório recursivamente, -p para preservar características (data, dono, permissões)
# mv: Move um arquivo para outro diretório ($file $dirTarget) ou renomeia o mesmo ($fileOld $fileNew)

# Comandos
echo Printa qualquer coisa, sério, vai printar até vc pular a linha ou ponto e vírgula.
variaveis='sao definidas assim!'

# Criar arquivos
# Dá pra criar um arquivo vazio usando o comando "touch"
touch arquivoVazio.txt

# Caso queira criar um arquivo já com conteúdo, pode usar
cat > arquivoPreenchido.txt
# Isso irá receber seus inputs, até que pressione Ctrl + D, então ele salva o arquivo
# Lembre-se que com ">" você sobrescreve, com ">>" você concatena ao fim (append)

:'
Para comentar em sequência basta fazer isso que está vendo
colocar dois pontos e inserir o comentário entre aspas simples


# Uso de delimitadores
# Ao criar uma variável, podemos atribuir um série de textos
cat << printaEarquiva
echo estou printando e arquivando
echo estou printando e arquivando
echo estou printando e arquivando
echo estou printando e arquivando
printaEarquiva

# Condicionais
# São no formato
# if [ condicao ] then ... else ... fi
valorDez=10
if [ $valorDez -eq 5 ]
then
    echo o valorDez é igual a 5
elif (( $valorDez > 11 ))
then
    echo o valorDez é maior que 11
else 
    echo o valorDez não é igual 5, mas sim igual a $valorDez
fi

# Esse site tem uma boa lista de condicionais:
# https://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php