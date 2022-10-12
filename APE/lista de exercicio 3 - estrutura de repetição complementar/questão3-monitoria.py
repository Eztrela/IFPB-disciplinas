from pickletools import ArgumentDescriptor


num1 = int(input('Digite o numero 1: '))
num2 = int(input('Digite o numero 2: '))
aux = 0
numero1 = num1
numero2 = num2

while(num2 != 0):
    aux = num1 % num2
    num1 = num2 
    num2 = aux  

print(f'O MDC entre {numero1} e {numero2} é igual a {num1}')
