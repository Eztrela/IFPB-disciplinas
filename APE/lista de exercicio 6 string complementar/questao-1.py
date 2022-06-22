email = input('Digite seu email: ')
split = email.split('@')
login = split[0]
provedor = split[1]
print(f'Login: {login}')
print(f'Provedor: {provedor}')