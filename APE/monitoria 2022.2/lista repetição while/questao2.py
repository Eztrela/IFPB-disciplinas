""" Faça um programa que leia vários números, calcule e exiba a média desses
números.
Obs: a leitura do número 999 indica o fim dos dados de entrada e não deve ser
computado na média) """

numero = int(input('Digite um número: '))
soma = 0
qnt_numeros = 0
while numero != 999:
    soma += numero
    qnt_numeros += 1
    numero = int(input('Digite um número: '))

media = soma / qnt_numeros

print(f'A média desses números é {media}.')
