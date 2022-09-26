from filaEncadeadaNoCabeca import filaEncadeadaNoCabeca

f = filaEncadeadaNoCabeca()

f2 = filaEncadeadaNoCabeca()
fres = filaEncadeadaNoCabeca()
print(f)
for i in range(1,11):
    f.enfileira(i*10)
for i in range(12,22):
    f2.enfileira(i*10)

print(f) #10, 20, 30, 40, 50, 60, 70, 80, 90, 100
print(f'Frente : {f.frente()}, Final : {f.final()}\n') #10, 100
print(f'Vazia? {f.estaVazia()}') #False
print(f.desenfileira()) #10
print(f) #None, 20, 30, 40, 50, 60, 70, 80, 90, 100
print(f'Frente : {f.frente()}, Final : {f.final()}\n') #20, 100

f.modificar(5, 'TRICKSTER')

f.enfileira('WILDCARD')
print(f) #WILDCARD, 20, 30, 40, 50, 60, 70, 80, 90, 100
print(f'Frente : {f.frente()}, Final : {f.final()}\n') #20, WILDCARD

print(f'A posição de 40 é : {f.busca(40)}')
print(f'O elemento na posição 5 é : {f.elemento(5)}\n')

#DESENFILEIRA
print(f'f ante: {f}')
print(f'f2 ante: {f2}')
f.concatenar(f2)
print(f'f depois: {f}')
print(f'f2 depois: {f2}')

#INVERTE
print(f'f ante: {f}')
f.inverte()
print(f'f depois: {f}')