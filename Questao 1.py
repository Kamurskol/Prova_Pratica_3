import re # Aqui é importada a função re, que permite trabalhar com expressões regulares

str = str(input('Digite algo: ')) #Aqui será digitada a string

novastring = re.sub('[\s\d]', '' ,str) #A função re.sub irá substituir \s (espaços em branco) e \d (números/dígitos) por '' (vazio)

nova = novastring.replace('a', 'A') # Aqui é criada uma nova string utilizando a string onde foram retirados os números e espaços em branco, nela todo 'a' minúsculo é substituido por um 'A' maiúsculo
nova = nova.replace('e', 'E') # Aqui é usada a lista que foi recém-criada, nela trocamos os 'e's minúsculos por 'E's maiúsculos
nova = nova.replace('i', 'I') # Aqui acontece a mesma coisa
nova = nova.replace('o', 'O') # Aqui acontece a mesma coisa
nova = nova.replace('u', 'U') # Aqui acontece a mesma coisa

print(nova)
