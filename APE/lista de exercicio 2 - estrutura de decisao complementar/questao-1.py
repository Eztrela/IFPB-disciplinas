dias_semana = ['domingo','segunda','terça','quarta','quinta','sexta','sábado']

numero = int(input())

if(numero != 1 and numero != 7):
    print(f'{dias_semana[numero-1]} é dia de semana')
else:
    print(f'{dias_semana[numero-1]} é fim de semana')