peso = float(input())
altura = float(input())

grau_obesidade = peso / (altura**2)

if(grau_obesidade < 26):
    print(f'grau de obesidade: normal')
elif(grau_obesidade >= 26 or grau_obesidade < 30):
    print(f'grau de obesidade: obeso')
else:
    print(f'grau de obesidade: obeso morbido')