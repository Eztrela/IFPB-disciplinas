frase = input('Digite uma frase: ').upper()
for i in range(len(frase)):
  print(frase[i]*(i+1))
for i in range(-2,-(len(frase)+1),-1):
  print(frase[i]*((len(frase)+1)+i))

#outra forma

frase = input('Digite uma frase: ').upper()
for i in range(len(frase)*2-1):
  if i < len(frase):
    print(frase[i]*(i+1))
  else:
    print(frase[(len(frase)*2-2)-i]*((len(frase)*2-1)-i))