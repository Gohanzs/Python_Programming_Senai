nomes = ['','','']
idades = [0,0,0]
quartos = ['','','']
valores = [0,0,0]
dias = [0,0,0]


nomes[0] = input('Digite o nome do primeiro cliente: ')
idades[0] = int(input('Digite a idade: '))
quartos[0] = input('Tipos de quartos (Simples/Duplo/Luxo): ')
dias[0] = int(input('Digite a quantidade de dias: '))


if quartos[0] == 'Simples':
    valores[0] = 150 * dias[0]
elif quartos[0] == 'Duplo':
    valores[0] = 250 * dias[0]
elif quartos[0] == 'Luxo':
    valores[0] = 300 * dias[0]
else:
    valores[0] = 0
    print('Quarto invalido para o cliente.')


nomes[1] = input('Digite o nome do segundo cliente: ')
idades[1] = int(input('Digite a idade: '))
quartos[1] = input('Tipos de quartos (Simples/Duplo/Luxo): ')
dias[1] = int(input('Digite a quantidade de dias: '))


if quartos[1] == 'Simples':
    valores[1] = 150 * dias[1]
elif quartos[1] == 'Duplo':
    valores[1] = 250 * dias[1]
elif quartos[1] == 'Luxo':
    valores[1] = 300 * dias[1]
else:
    valores[1] = 0
    print('Quarto invalido para o cliente.')


nomes[2] = input('Digite o nome do terceiro cliente: ')
idades[2] = int(input('Digite a idade: '))
quartos[2] = input('Tipos de quartos (Simples/Duplo/Luxo): ')
dias[2] = int(input('Digite a quantidade de dias: '))


if quartos[2] == 'Simples':
    valores[2] = 150 * dias[2]
elif quartos[2] == 'Duplo':
    valores[2] = 250 * dias[2]
elif quartos[2] == 'Luxo':
    valores[2] = 300 * dias[2]
else:
    valores[2] = 0
    print('Quarto invalido para o cliente.')


print('\n Valor total a ser pago')

print(valores[0], 'R$', nomes[0])
print(valores[1], 'R$', nomes[1])
print(valores[2], 'R$', nomes[2])

print('Obrigado pela preferencia volte sempre! ')