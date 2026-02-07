import random

lista_maq = ['🪨','🧻','✂️']
chute_maq = random.choice(lista_maq)

minha_lista = ['🪨','🧻','✂️']

print('Escolha seu icone')
print('0 - 🪨', '2 - 🧻', '3 - ✂️')

meu_chute = int(input('Escolha pelo indice:'))

if chute_maq == minha_lista[meu_chute]:
    print('EMPATE')
