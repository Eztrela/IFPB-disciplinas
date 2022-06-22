N =  int(input())
cont = 1
descartar = 0
atualizar = 1
aux = 0
while (cont <= N):
    if(cont==1):
        print(0)
    elif(cont==2):
        print(1)
    else:
    
        aux = atualizar
        atualizar += descartar
        descartar = aux

        print(atualizar)
    cont += 1
