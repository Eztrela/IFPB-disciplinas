frase = input('Digite uma frase: ').upper().strip()

frase = frase.replace('A','*')
frase = frase.replace('E','#')
frase = frase.replace('I','&')
frase = frase.replace('O','%')
frase = frase.replace('U','!')
frase = frase.replace(' ','A')
frase = frase.replace('*',' ')
frase = frase.replace('#','U')
frase = frase.replace('&','O')
frase = frase.replace('%','I')
frase = frase.replace('!','E')

  

print(frase)