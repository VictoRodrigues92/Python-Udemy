user = input('Nome de usuário: ')
pw = input('Senha do Usuário: ')

user_bd = 'Joao'
senha_bd = '123456'

if user_bd == user and senha_bd == pw:
    print('Você está logado no sistema')

else:
    print('Usuário ou senha incorreta')