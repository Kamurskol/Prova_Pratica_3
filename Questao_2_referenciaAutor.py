def referenciaAutor(str):# Definida a função de referência, com classe string

    nome = str(input('Digite o nome do autor: '))# Aqui é digitado o nome do autor

    nmlista = nome.split()# O nome é dividido em pedaços e adicionado a uma lista
    autor = nmlista[0:-1]# Essa lista contém o nome do autor, menos o último sobrenome

    print(f'{nmlista[-1].upper()},', *autor)# 'nmlista[-1].upper()' vai imprimir o último elemento da lista que contém o nome - o último sobrenome - em caixa alta
                                            # O '*' imprime a lista autor (que não contém o último sobrenome) sem os colchetes
referenciaAutor(str)# Aqui é chamada a função de referência
