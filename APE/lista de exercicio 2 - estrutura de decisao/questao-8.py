operando1 = float(input())
operando2 = float(input())
operador = input()

resultado = 0

if(operador == '+'):
    resultado = operando1 + operando2
elif(operador == '-'):
    resultado = operando1 - operando2
elif(operador == '*'):
    resultado = operando1 * operando2
elif(operador == '%'):
    resultado = operando1 % operando2
elif(operador == '/'):
    resultado = operando1 / operando2
else:
    resultado = 'operador desconhecido'

print(f'resultado da operacao é: {resultado}')

