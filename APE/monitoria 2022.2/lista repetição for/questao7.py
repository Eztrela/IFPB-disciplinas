num = int(input('digite o numero: '))

if(num == 1 or num == 0):
    print('1 e zero não é primo e nem composto')
else:
    primo = True
    for div in range(2, num):
        if(num % div == 0):
            primo = False

    if(primo):
        print(f'É primo')
    else:
        print(f'Não é primo')