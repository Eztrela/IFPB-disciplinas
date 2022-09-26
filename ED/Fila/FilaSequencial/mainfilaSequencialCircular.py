from filaSequencialCircular import filaSequencialCircular

f = filaSequencialCircular()

f2 = filaSequencialCircular()
fres = filaSequencialCircular()
print(f)
for i in range(1,11):
    f.enfileira(i*10)
for i in range(12,22):
    f2.enfileira(i*10)

print(f)
print(f2)
f.desenfileira()
f.desenfileira()
f.desenfileira()
f.enfileira(20)
print(f.busca(100))
f.modificar(8,'EITA')
print(f)