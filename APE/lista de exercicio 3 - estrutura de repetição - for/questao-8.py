numero = int(input('informe o numero'))
quadrado = 0
for i in range(1,(numero//2)+1):
    if(i * i <= numero):
        quadrado = i * i
    else:
        break

print(quadrado)
