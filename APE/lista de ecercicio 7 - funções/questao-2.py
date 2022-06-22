def fatorial(numero):
  if (numero == 0 or numero == 1):
    return 1
  else:
    return numero*fatorial(numero-1)

num = int(input(f'Digite o numero a calcular o fatorial: '))

print(fatorial(num))