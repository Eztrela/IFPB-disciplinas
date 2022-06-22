n = int(input('informe o valor de N: '))
primo =  True
for i in range(2,(n//2)+1):
    if (n % i) == 0:
        primo = False
        break
if(primo):
    print(f'O número {n} é primo')
elif(not primo):
    print(f'O número {n} não é primo')
