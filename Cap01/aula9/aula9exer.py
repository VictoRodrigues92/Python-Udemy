nome = input('Qual é seu nome? ')
idade = input('Qual a sua idade? ')
idade = int(idade)
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar emprestimo.')
else:
    print(f'{nome} NÃO pode pegar emprestimo')