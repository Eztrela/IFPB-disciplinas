'''

grupo de pessoas que foi ao show, perguntar a cada pessoa o nome, idade, sexo, estado civil

1 - % de homens que foram a festa
2 - % de mulheres que foram a festa
3 - quantidade de mulheres solteiras e com idade menor que 20
4 - homens casados com idade maior que 30
5 - acumular total de pessoas que foram ao show

'''
from ossaudiodev import SNDCTL_DSP_SETFRAGMENT
from signal import SIG_DFL


nome = ''
phomens = 0
pmulheres = 0
novinhas = 0
velhos = 0
total_pessoas = 0
total_homens = 0
total_mulheres = 0


while True:
    nome = input('Digite o seu nome: ')
    if nome == '0':
        break
    idade = int(input('Digite a sua idade: '))
    sexo = input('Digite o Sexo (M para masculino  e F para Feminino):').upper()
    estado_civil = input('Digite o Estado Civil:').upper()
    total_pessoas += 1
    if(sexo == 'F'):
        total_mulheres += 1
        if(idade < 20 and estado_civil == 'S'):
            novinhas += 1
    else:
        total_homens += 1
        if(idade > 30 and estado_civil == 'C'):
            velhos += 1

print(f'A porcentagem de homens na festa foi de: {total_homens/total_pessoas * 100:.2f}%')

print(f'A porcentagem de mulheres na festa foi de: {total_mulheres/total_pessoas *100:.2f}%')
    
print(f'A quantidade de novinhas na festa foi de: {novinhas}')

print(f'A quantidade de velhos na festa foi de: {velhos}')

print(f'O total de pessoa que foi na festa foi de: {total_pessoas}')
