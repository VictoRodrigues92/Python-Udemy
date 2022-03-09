nome = 'João Victor'
idade = 29
altura = 1.75
e_maior = idade > 18
peso = 80
imc = peso / (altura ** 2)

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)

print(f'{nome} tem {idade} de anos de vida e seu imc é {imc:.2f}')
'''ou pode ser feito'''
print('{} tem {} de anos de vida e seu imc é {} '.format(nome, idade, imc))