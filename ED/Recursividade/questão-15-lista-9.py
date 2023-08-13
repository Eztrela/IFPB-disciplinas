def esta_ordenado(vetor):
  if len(vetor) < 2:
    return True
  if vetor[0] <= vetor[1]:
    return esta_ordenado(vetor[1:])
  else:
    return False
a = [1, 5, 5, 5, 75, 100]
print(esta_ordenado(a))

def soma_vetor(vetor):
  if len(vetor) == 0:
    return 0
  return vetor[0] + soma_vetor(vetor[1:])

print(soma_vetor(a))