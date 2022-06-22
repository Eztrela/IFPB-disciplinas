menor = 0
contador = 0
soma = 0
faixa = 0

while(True):
    idade = int(input('Digite a idade: '))
    if (idade == 0):
        break
    
    contador += 1
    if (contador == 1):
        menor = idade
    
    if(idade < menor):
        menor = idade

    if (idade >= 18 and idade <= 21):
        faixa += 1
    
    soma += idade

media = soma/contador
porcentagem = (faixa/contador)*100

print(f'A media de idade do publico foi de {media:.2f} anos')
print(f'A % de pessoas com idade entre 18 e 21 anos foi de {porcentagem:.2f}%')
print(f'A idade do visitante mais jovem é de {menor} anos')