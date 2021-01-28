# Variavéis
string = "Bem simples"
inteiro = 69
float = 7,77

# Booleanos
verdadeiro = true
falso = false

# Simbolos
simbolo = :primeiroSimbolo
simbolo2 = :primeiroSimbolo
# Mas qual a diferença de um
# símbolo para uma String?
# Os símbolos não são mutáveis,
# no caso acima, ambos os símbolos
# apontam para o mesmo endereço
# de memória e não podem ser mudados.
# Sua utilidade é para dicionários
# como chaves de um dicionário

# Printando
# Suponha a estrutura de dados
# [[1,2,3], [4,5,nil]]
puts [[1,2,3], [4,5,nil]]
# Irá printar:
# 1
# 2 ...
# 5
# E não printará o nil
print [[1,2,3], [4,5,nil]]
# Irá printar:
[[1,2,3], [4,5,nil]]

# Iterador para cada (Each)
[[1,2,3], [4,5,nil]].each do |estaConjunto|
	print "O número: "
	print estaConjunto
	print "está no conjunto!"
	puts " "
end 
# Para este código estaConjunto 
# é uma variável existente apenas
# nessa parte (não é global)

# Laços
for X in 0...7
	puts X
end

# Condicionais
if 4 <= 5
	puts "Parece que funciona"
else if
	puts "Deu errado a condicional"
else
	puts "Como é que chegou nessa condição"
end

# Arrays
arrayzin = [1, 9, 8, 7]
arrayzao << "Oitenta e sete é nosso"
# Nessa segunda forma,
# o que está acontecendo é:
# arrayzao.<<("Oitenta e sete é nosso")

# Estrutura de Dados Chave
hash_Simples = {
	"taNoGithub" => "To sim!",
	"taNoZap" => "To não!",
	"fazQuantoTempo" => 13
}
# Para printar isso:
puts "Este código está hospedado no GitHub #{hash_Simples[taNoGithub]}
