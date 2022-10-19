pontos_a = 0
pontos_b = 0

while (pontos_a < 5 and pontos_b < 5) or (pontos_a-pontos_b < 2 and pontos_b-pontos_a < 2):
    ponto = input('Digite a equipe que pontuou (A ou B): ').upper()
    if ponto == 'A':
        pontos_a += 1
    if ponto == 'B':
        pontos_b += 1
if pontos_a > pontos_b:
    ganhador = 'Equipe A'
else:
    ganhador = 'Equipe B'

print(f'A equipe vencedora foi a {ganhador}')



def ex8():
#Questão 8
 
  pontos_A =0
  pontos_B= 0
  while (pontos_A < 5 and pontos_B < 5) or (pontos_A - pontos_B < 2 and pontos_B - pontos_A < 2):
    codigo = input('Qual o código da equipe(A-B) que marcou ponto: ').upper()
    if codigo == 'A':
      pontos_A+=1
      print(f'{pontos_A} vs {pontos_B}')
    if codigo == 'B':
      pontos_B+=1
      print(f'{pontos_A} vs {pontos_B}')
    
  if pontos_A>pontos_B:
    ganhador='A'
  else:
    ganhador= 'B'
  print(f'Fim da partida. O ganhador é o time {ganhador}')
ex8()