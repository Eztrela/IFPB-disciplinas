massa = int(input())
tempo = 0
while(massa > 0.5):
    massa /= 2
    tempo += 50

hora = tempo // 3600
tempo -= hora * 3600
minuto = tempo // 60
tempo -= minuto * 60
segundos = tempo
print(hora, minuto, segundos)
