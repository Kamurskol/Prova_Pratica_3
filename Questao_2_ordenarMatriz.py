import numpy as np # Aqui é importada a biblioteca NumPy (python numérico)

matriz = [[],[],[]] #A matriz recebe 3 listas vazias
for l in range(3): # A matriz terá 3 linhas...
        for c in range(3): # E 3 colunas
                matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))# as linhas e colunas da matriz serão preenchidas aqui

print('\nA matriz digitada foi:')

for l in range(3): #As linhas...
        for c in range(3): #E as colunas

                print(f'[{matriz[l][c]:^2}]', end='') #Serão impressas aqui
            
        print()

def ordenaMatriz(list): #Aqui é criada a função ordenaMatriz, com classe list

        a = np.array(matriz)# A variável 'a' recebe o array da matriz que foi digitada

        matrizord = np.sort(a, axis= None) # Aqui e ordenado o array, com eixo = 0 (a matriz vira uma lista comum, sem colunas)
        print('\nA matriz reordenada é: ')
        print(matrizord) # Aqui é impressa a matriz reordenada em formato de lista

ordenaMatriz(list) # Aqui é feita a chamada da função
