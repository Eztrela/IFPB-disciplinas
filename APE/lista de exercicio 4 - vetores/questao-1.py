n= int(input('Digite o valor de N : '))

vetor_a = [None] * n
vetor_b = [None] * n

k = int(input('Digite o valor de K : '))

for i in range(n):
    vetor_a[i] =  int(input(f'Digite o valor de vetor_a{[i]} : '))
    vetor_b[i] = vetor_a[i] * k

print(vetor_b)