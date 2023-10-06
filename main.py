import numpy as np

#Acessando o array salvo no txt
matriz = np.loadtxt('array1.txt', dtype=int, delimiter="\t")
print(f'{matriz}\n')

#obtendo valores estatísticos
media_coluna = matriz.mean(axis=0)
mediana_linha = matriz.mean(axis=1)
desvio_padrao = matriz.std()
print(f" Media das colunas: {media_coluna}\n Mediana das linhas: {mediana_linha}\n Desvio padrão do array: {desvio_padrao:.2f}\n"
)

#Transposta
matriz_transposta = matriz.T
matriz2 = np.random.randint(
    0, 101, size=(2, 4))  #cria o array para multiplica a transposta
mult_matriz = matriz_transposta * matriz2
print(f'A multiplicação dos arrays é:\n {mult_matriz}\n')

#produto escalar
arr = np.random.randint(0, 101,
                        size=(2))  #cria o array para realizar o prod escalar
prod_escalar = np.dot(matriz, arr)
print(f'O produto escalar é {prod_escalar}\n')

#Filtro dos números pares
filtro = np.where(matriz % 2 == 0)
print(f'{matriz[filtro]} é um número par\n')

#operação aritmética
resultado = matriz * arr
print(
    f'O resultado da multiplicação do array bidimensional com um array é: \n {resultado}\n'
)
