""" Escreva um programa que leia 10 números e armazene-os em um vetor. Exiba:
• Os números que estão nos índices pares;
• Os números que estão nos índices ímpares. """

import random

vetor = [None]*10
for i in range(10):
    vetor[i] = random.randint(0, 9)

print(vetor)

print('Os valores que estão nos índices pares são: ', end='')
for i in range(0, 10, 2):
    print(vetor[i], end=' ')

print('\nOs valores que estão nos índices ímpares são: ', end='')
for k in range(1, 10, 2):
    print(vetor[k], end=' ')