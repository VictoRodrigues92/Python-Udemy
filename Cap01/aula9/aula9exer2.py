nome = input('Qual é seu nome? ')
idade = input('Qual a sua idade? ')
idade = int(idade)
idade_menor = 20 #muito jovem
idade_maior =  30 #muito velho

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar emprestimo.')
else:
    print(f'{nome} NÃO pode pegar emprestimo')

