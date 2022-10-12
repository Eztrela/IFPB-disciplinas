n = int(input("Digite o valor de N: "))
a = [None]*n
k = int(input("Digite o valor de k: "))
b = [None]*n
for i in range(n):
    a[i] = int(input('Digite um valor: '))
    b[i] = a[i] * k
print(a ,'\n',b)