soma_idades = 0
flor_da_idade = 0
juvenil = 0
pessoas = 0
idade_visitante = -1
while idade_visitante != 0:
    idade_visitante = int(input("Digite a idade do Visitante: "))
    if (idade_visitante == 0):
        break
    elif(idade_visitante >= 18 and idade_visitante<= 21):
        flor_da_idade += 1
    if pessoas == 0:
        juvenil = idade_visitante
    elif (idade_visitante < juvenil):
        juvenil = idade_visitante
    soma_idades += idade_visitante
    pessoas += 1

media = soma_idades / pessoas
p_flor_da_idade = flor_da_idade/pessoas*100

print(f'Media: {media}, Porcentagem: {p_flor_da_idade}%, idade do juvenil: {juvenil}')