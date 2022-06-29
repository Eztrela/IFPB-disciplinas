import random
while(True):
    linhas1 = int(input('Informe o numero de linhas: '))
    colunas1 = int(input('Informe o numero de colunas: '))

    linhas2 = int(input('Informe o numero de linhas: '))
    colunas2 = int(input('Informe o numero de colunas: '))

    if(colunas1 == linhas2):
        matriz1 = [[None]*colunas1 for i in range(linhas1)]
        matriz2 = [[None]*colunas2 for i in range(linhas2)]
        matriz_result = [[None]*linhas1 for i in range(colunas2)]
        for i in range(linhas1):
            for j in range(colunas1):
                matriz1[i][j] = random.randint(1,5)
        
        print(matriz1)
        
        for i in range(colunas1):
            for j in range(linhas1):
                matriz2[i][j] = random.randint(1,5)
        
        print(matriz2)
        print(matriz_result)
        for i in range(linhas1):
            
            for j in range(colunas2):
                soma = 0
                for k in range(colunas1):
                    soma += matriz1[i][k]*matriz2[k][j]
                matriz_result[i][j] = soma
        
        print(matriz_result)