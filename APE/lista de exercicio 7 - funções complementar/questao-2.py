def primo(num):
  retorno = True
  for i in range(2,int((num/3))+1):
    if (num % i) == 0:
      retorno = False
      break
  return retorno

print(f'Numeros Primos: ')

for i in range(2,101):
  if primo(i):
    print (i)