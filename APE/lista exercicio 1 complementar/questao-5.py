segundos = int(input('Digite uma quantida de segundos: '))
segundos_inicial = segundos
hora = segundos//3600
segundos = segundos%3600
minutos = segundos//60
segundos = segundos%60

print(f'{segundos_inicial} s é equivalente a {hora} h {minutos} m e {segundos} s')
