# Introdução ao Python


## Tipos Primitivos
``` $ type(True) ``` <br>
``` $ <class 'bool'> ``` <br><br> 
### True e False são os únicos membros da classe booleana
``` $ type(3) ``` <br>
``` $ <class 'int'> ``` <br><br>
### Qualquer número inteiro, positivo ou negativo é membro da classe int
``` $ type(4/3) ``` <br>
``` $ <class 'float'> ``` <br><br>
### Qualquer número fracionário positivo ou negativo, ou seja, que possa ser representado por uma fração é membro da classe float
```$ type('Oi 9')``` <br>
```$ <class 'str'>```
### Qualquer texto que estiver entre áspas, "" ou '', é membro da classe str, abreviação de string (ou em português, cadeia de caracteres)
<br>

## Atribuindo valores
### Python é fracamente tipada, ou seja, você não precisa indicar a qual classe você querendo atribuir a sua variável
```$ sua_variavel = 1 ``` <br>
```$ print(sua_variavel) ``` <br>
```$ 1 ```
### Em outras linguagens, teríamos que indicar a qual classe desejaríamos trocar ```sua_variavel``` (no caso, saindo de int para str) 
```$ sua_variavel = 'Um' ``` <br>
```$ print(sua_variavel) ``` <br>
```$ Um ```

## Função ```print()```
### Serve para exibir quaisquer informações ou variáveis que forem colocadas entre os parênteses, a função ```type()``` verifica a qual classe o parâmetro pertence e print a resposta

## Cast e composição de funções
### Podemos trocar a classe de variáveis, caso a mesma respeite a nova classe. <br> Podemos fazer casts várias vezes, sendo este um exemplo de composição de funções
#### Cast de str para int
```$ type(int('1'))```<br>
```$ <class 'int'>```<br><br>
#### Cast de int para bool
```$ type(bool(int(str('0'))))```<br>
```$ <class 'bool'>```
#### Observe que a ordem importa, caso fizessemos:
```$ type(str(bool(int('0'))))```<br>
```$ <class 'str'>```

## Booleanos
### Avaliam condicionais
#### Podemos usar as funções ```print()``` e ```type()``` e os casts vistos anteriormente para aprender mais sobre booleanos:
```$ print(type('1') == type('Oi'))``` <br>
```$ True``` <br><br>
```$ print(int('1') < 0)```<br>
```$ False```<br><br>
```$ print(3 != 3.1415)```<br>
```$ True```<br><br>


### Observação: Python foi construído em cima da linguagem C, portanto, algumas de suas avaliações de condicionais são herdadas. <br>
### Qualquer string é ```True```, exceto strings vazias ```''```
### Qualquer número é ```True```, exceto ```0```
### Qualquer lista, tupla, conjunto ou dicionário é ```True```, exceto os vazios ```[]```<br>

## Tuplas
### O grande diferencial de tuplas para outras estruturas é sua imutabilidade, uma vez criado uma tupla, ela não poderá ser alterada, caso tente, o Python não permitirá e lhe exibirá um erro. Podemos contornar a situação dando um cast list() numa tupla, e depois outro cast para tuple() substituindo a variável que guardava a tupla imutável.
```$ minha_tupla = ('unaria', 'dupla', 'tripla', 'quadrupla', 'quintupla')```
#### Podemos acessar cada valor da tupla usando [], lembre-se que a contagem começa de 0.
```$ print(minha_tupla[2])```<br>
```$ tripla```<br>
#### Obs: Podemos começar a contagem de trás pra frente, o último é [-1], o penúltimo é [-2] e assim por diante<br>

#### Podemos ainda percorrer pelos limites ```[sim-primeiro:não-último]```, por exemplo:
```$ print(minha_tupla[1:4])```
#### Vai pegar, começando de 0, o item  [1] = ```'dupla'``` até [4] = ```'quintupla'```, porém, não pega o ```'quintupla'```, por isso ```[sim-primeiro:não-último]```
```$ ('dupla', 'tripla', 'quadrupla')```

#### Podemos juntar duas tuplas (obs: a ordem importa)
```$ print(minha_tupla + minha_tupla)```<br>
```$ 'unaria', 'dupla', 'tripla', 'quadrupla', 'quintupla', 'unaria', 'dupla', 'tripla', 'quadrupla', 'quintupla'```<br>

#### A função len() mede o tamanho do conjunto fornecido como parâmetro, o len conta começando do 1, não se confunda com [], o qual começa de 0!!!
```$ len(minha_tupla)```<br>
```$ 5```

#### A função count() verifica quantas vezes o parâmetro fornecido aparece na tupla
```$ minha_tupla.count('dupla')```<br>
```$ 1```<br><br>

#### A função index() verifica qual a posição está o primeiro parâmetro fornecido, caso apareça mais de uma vez, será retornada a posição da primeira ocorrência <br>
```$ minha_tupla.count('tripla')```<br>
```$ 2```<br><br>

## Listas
### Em resumo, são tuplas que podem ser modificadas, todos os métodos vistos acima continuam válidos e ganhamos algumas novas funções:

#### append(): Adiciona um elemento ao fim da lista <br>
#### clear(): Remove todos os elementos da lista, deixando-a vazia<br>
#### copy(): Copia todos os elementos de uma lista, é útil para transferí-la para outra variável<br>
#### extend(): Adiciona qualquer estrutura (lista, tupla, elemento) dada como parâmetro ao fim da lista<br>
#### insert(): Recebe dois parâmetros: posição, elemento; ou seja, você pode inserir numa dada posição específica da lista<br>
#### pop(): Recebe dois parâmetros: posição, elemento; ou seja, você pode remover numa dada posição específica da lista<br>
#### remove(): Remove o elemento dado, caso ele exista na lista
#### reverse(): Inverte a ordenação da lista
#### sort(): Orderna a lista (0-9) e (a-Z)

## Dicionários
### Armazenam informação no formato: ```variavel = {'chave': valor}```
```$ guardioes_da_galaxia = {'humano': 'Peter Quill', 'poder': 'Gosto musical', 'idade': 40} ``` <br>
```$ print(guardioes_da_galaxia['humano'])```<br>
```$ Peter Quill```<br>