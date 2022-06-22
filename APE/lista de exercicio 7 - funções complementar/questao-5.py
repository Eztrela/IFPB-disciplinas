import math

def fatorial(num):
  f = 1
  for i in range(1,num+1):
    f*=i
  return f

def pow(num,exp):
  result = 1
  for i in range(exp):
    result *= num
  return result


x = float(input(f'Digite o valor de X: '))
neg = 0
pos = 0
for i in range(2,38,4):
  neg -= (pow(x,i)/fatorial(i))
  print(neg)
print(neg)
for i in range(4,39,4):
  pos += (pow(x,i)/fatorial(i))
print (pos)

print(f'O cosseno de x = {x} é {1+pos+neg}')

print(math.cos(x))