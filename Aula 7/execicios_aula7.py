ex_0 = list(range(2,21,2))
print('Numeros',ex_0)

# 1
numeros = list(range(1,11))
print('Numeros inteiros:', numeros)

#2
print('Terceiro elemento:',numeros[2])

#3
numeros.append(9)
print(numeros)

#4
numeros.remove(5)
print('Numero 5 removido',numeros)

#5
Carros = ['Civic','Sonata','Fluence']
Carros.extend(numeros)
print(Carros)