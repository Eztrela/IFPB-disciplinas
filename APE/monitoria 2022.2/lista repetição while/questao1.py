"""Faça um programa que leia vários números, determine e mostre o maior e o menor deles.
Obs: a leitura do número 0 (zero) encerra o programa."""

numero = int(input('Digite um número: '))
maior = numero
menor = numero
while numero != 0:
    numero = int(input('Digite um numero: '))
    if numero != 0 and numero > maior:
        maior = numero
    elif numero != 0 and numero < menor:
        menor = numero

print(f'O maior número é {maior}.')
print(f'O menor número é {menor}.')





