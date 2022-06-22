def menor(numero1, numero2, numero3):
  menor = numero1
  if numero2 < menor:
    menor = numero2
  if numero3 < menor:
    menor = numero3
  return menor

num1 = float(input(f'Digite o numero 1: '))
num2 = float(input(f'Digite o numero 2: '))
num3 = float(input(f'Digite o numero 3: '))

print(f'{menor(num1,num2,num3)}')