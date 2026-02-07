
# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, negativo ou zero.
print('Idenificação -, +, 0')
numero = int(input('Digite seu numero'))
if numero >=1:
    print('Positivo!')
if numero<=-1:
    print('Negativo')
if numero == 0:
    print('Zero')

# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com  base na idade.
print('identificação de idade para votar!')
idade = int(input('Digite sua idade: '))
titulo = input('Voce tem titulo?: (sim/nao): ')
if idade>=16 and titulo == 'sim':
    print("Voce pode votar!")
else:
    print("Voce não pode votar!")
# 3*

# Declara uma variável com um número qualquer, determine se um número é par ou ímpar.
print('Sistema de identificação de par ou impar')
par = list(range(2,21,2))
Impar = list(range(1,21,2))

variavel = int(input('Digite seu numero:'))
if variavel  % 2==0:
    print('Numero é par')
else:
    print('Numero é impar')
# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

print('Sistema de identificacao do triangulo!')
lado1 = float(input('Digire o primeiro lado do triangulo: '))
lado2 = float(input('Digite o segundo lado do triangulo: '))
lado3 = float(input('Digite o terceiro lado do triangulo: '))

if lado1 == lado2 == lado3:
    print('O triangulo é equilatero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('O Triangulo é isoceles')
else:
    print('O triangulo é escaleno')


# 5*

	# Determine se um número é múltiplo de 5 e 7.
    print('Sistema de multiplicacao')
    n = int(input('Digite seu numero: '))

    if n % 5 == 0 and n % 7 == 0:
        print('Multiplo')
    else:
        print('Não multiplo')

# 6*

# Verifique se um número é positivo e maior que 10
print('Sistema de indetificação de > ou = a 10')
n = int(input('Digite seu numero: '))
if n >=10 and n>=0:
    print('Seu numero positivo ou maior que 10 :)')
else:
    print('Seu numero é negativo ou menor que 10 :(')

# 7*

# Verifique se um número é divisível por 3 ou 5.

n = int(input('digite seu numero'))
if n    % 3 or n % 5:
    print('Divisivel')
else:
    print('Não divisivel')