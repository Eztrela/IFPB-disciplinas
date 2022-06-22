maior = 0
menor = 0
tmaior = 0
tmenor = 0
for i in range(1,31):
    temperatura = input()
    if (i == 1):
        tmaior = temperatura
        maior = i
        tmenor = temperatura
        menor = i
    else:
        if(temperatura > tmaior):
            tmaior = temperatura
            maior = i
        elif(temperatura < tmenor):
            tmenor = temperatura
            menor = i

print(f'o dia {menor} teve a menor temperatura q foi de {tmenor}')
print(f'o dia {maior} teve a menor temperatura q foi de {tmaior}')