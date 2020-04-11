# Introdução ao Python


## Tipos Primitivos
```python
type(True)
<class 'bool'> 
```
### True e False são os únicos membros da classe booleana
```python
type(3)
<class 'int'> 
```
### Qualquer número inteiro, positivo ou negativo é membro da classe int
```python
type(4/3)
<class 'float'> 
```
### Qualquer número fracionário positivo ou negativo, ou seja, que possa ser representado por uma fração é membro da classe float
```python
type('Oi 9')
<class 'str'>
```
### Qualquer texto que estiver entre áspas, "" ou '', é membro da classe str, abreviação de string (ou em português, cadeia de caracteres)
<br>

## Atribuindo valores
### Python é fracamente tipada, ou seja, você não precisa indicar a qual classe você querendo atribuir a sua variável
```python
sua_variavel = 1
print(sua_variavel)
1 
```
### Em outras linguagens, teríamos que indicar a qual classe desejaríamos trocar ```sua_variavel``` (no caso, saindo de int para str) 
```python
sua_variavel = 'Um' 
print(sua_variavel)
Um 
```

## Função ```print()```
### Serve para exibir quaisquer informações ou variáveis que forem colocadas entre os parênteses, a função ```type()``` verifica a qual classe o parâmetro pertence e print a resposta

## Cast e composição de funções
### Podemos trocar a classe de variáveis, caso a mesma respeite a nova classe. <br> Podemos fazer casts várias vezes, sendo este um exemplo de composição de funções
#### Cast de str para int
```python
type(int('1'))
<class 'int'>
```
#### Cast de int para bool
```python
type(bool(int(str('0'))))
<class 'bool'>
```
#### Observe que a ordem importa, caso fizessemos:
```python
type(str(bool(int('0'))))
<class 'str'>
```

## Booleanos
### Avaliam condicionais
#### Podemos usar as funções ```print()``` e ```type()``` e os casts vistos anteriormente para aprender mais sobre booleanos:
```python
print(type('1') == type('Oi'))
True
print(int('1') < 0)
False
print(3 != 3.1415)
True
```


### Observação: Python foi construído em cima da linguagem C, portanto, algumas de suas avaliações de condicionais são herdadas. <br>
### Qualquer string é ```True```, exceto strings vazias ```''```
### Qualquer número é ```True```, exceto ```0```
### Qualquer lista, tupla, conjunto ou dicionário é ```True```, exceto os vazios ```[]```<br>

## Tuplas
### O grande diferencial de tuplas para outras estruturas é sua imutabilidade, uma vez criado uma tupla, ela não poderá ser alterada, caso tente, o Python não permitirá e lhe exibirá um erro. Podemos contornar a situação dando um cast list() numa tupla, e depois outro cast para tuple() substituindo a variável que guardava a tupla imutável.
```python
minha_tupla = ('unaria', 'dupla', 'tripla', 'quadrupla', 'quintupla')
```
#### Podemos acessar cada valor da tupla usando [], lembre-se que a contagem começa de 0.
```python
print(minha_tupla[2])
tripla
```
#### Obs: Podemos começar a contagem de trás pra frente, o último é [-1], o penúltimo é [-2] e assim por diante<br>

#### Podemos ainda percorrer pelos limites ```[sim-primeiro:não-último]```, por exemplo:
```python
print(minha_tupla[1:4])
```
#### Vai pegar, começando de 0, o item  [1] = ```'dupla'``` até [4] = ```'quintupla'```, porém, não pega o ```'quintupla'```, por isso ```[sim-primeiro:não-último]```
```python
('dupla', 'tripla', 'quadrupla')
```

#### Podemos juntar duas tuplas (obs: a ordem importa)
```python
print(minha_tupla + minha_tupla)
'unaria', 'dupla', 'tripla', 'quadrupla', 'quintupla', 'unaria', 'dupla', 'tripla', 'quadrupla', 'quintupla'
```

#### A função len() mede o tamanho do conjunto fornecido como parâmetro, o len conta começando do 1, não se confunda com [], o qual começa de 0!!!
```python
len(minha_tupla)
5
```

#### A função count() verifica quantas vezes o parâmetro fornecido aparece na tupla
```python
minha_tupla.count('dupla')
1
```

#### A função index() verifica qual a posição está o primeiro parâmetro fornecido, caso apareça mais de uma vez, será retornada a posição da primeira ocorrência <br>
```python
minha_tupla.count('tripla')
2
```

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
```python
guardioes_da_galaxia = {'humano': 'Peter Quill', 'poder': 'Gosto musical', 'idade': 40}
print(guardioes_da_galaxia['humano'])
Peter Quill
```
## Funções Anônimas (Lambda)

### Usamos a palavra reservada ```lambda``` para indicar que estamos definindo uma função lambda. Seu classe é ```function```

```python
a = lambda y: y*23
a(34)
782
b = a(10)
c = lambda z: b*z
c(30)
6900
soma_quadrados = lambda w,k: w**2+k**2
soma_quadrados(2,3)
13
```

### Composição de funções
```python
def funcao_quadratica(a, b, c):
      return lambda x: a*x**2 + b*x + c

f = funcao_quadratica(3,5,8)
f(2)
30
# ou #
funcao_quadratica(3,5,8)(2)
30
```

### Ordenando pelo sobrenome usando ```sort()``` e função lambda
```python
a = []
a.append('A. Zezo')
a.append('Z. Alberto')
a.append('L. Madruga')
a.append('B. Barcos')
a.append('F. Jackson')
a.append('G. Helio')
# Ordenando: quebro nomes, pego o último nome, e diminuo e ordena
a.sort(key = lambda n: n.split(' ')[-1].lower())
```

### Usando sort para ordenar a partir de um subconjunto de dados
```python
capacidade_estadios_dec = [
('Arruda', 60044, 'PE'),
('Mineirão', 61846, 'MG'),
('Castelão', 63903, 'CE'),
('Mané Garrincha', 72788, 'DF'),
('Morumbi', 77011, 'SP'),
('Maracanã', 78838, 'RJ')
]
# Já que o sort realiza in-place, posso usar o sorted()
# para copiar a preservar a estrutura original e dar sort
capacidade_estadios_cre = sorted(capacidade_estadios_dec[1])
# Posso também usar uma função lambda, caso não me importe com o original
tam_crescente = lambda e: e[1]
capacidade_estadios_dec.sort(key=tam_crescente)

```

## Exponenciação Rápida (Fast exponentiation)
### Serve para reduzir o tempo de calcular a exponenciação de O(n) para O(log n)

```python
def expo_rapida(a,n):
      if(n==0):
          return 1
      x = expo_rapida(a,n/2)
      x = x*x
      if(n%2 == 1):
          x = x*a
      return x
```

## Exceções
### O uso de exceções é fundamentado na ideia de criar um programa que seja a prova de falhas ou, no mínimo, prevenir erros e falhas previsíveis do seu código. Usamos o quarteto ```try, except, else, finally```;

```python
try:
      # Tentando abrir um arquivo 
      with open('arquivo.txt') as arqtxt:
          leitor = arqtxt.read().decode('utf-8')
except FileNotFoundException as FNFE:
      # Exceção caso o arquivo não exista
      print('O arquivo não existe, verifique e tente novamente!\n')
      raise
except EOFError as EOF:
      # O arquivo chegou ao fim
      print('O arquivo está vazio, verifique e tente novamente!\n')
      raise
else:
      # Caso o try não gere nenhuma exceção, e tudo dê OK
      print('O conteúdo do arquivo é:\n', leitor)
finally: 
      # Este código será executado mesmo que haja exceções ou não
      print('Encerrando aplicação!')
      exit()
```

