def par_impar(num1, num2):
    p_1 = ""
    p_2 = ""


    if num1 % 2 == 0:
        p_1 = "Par"
    else:
        p_1 = "Impar"

    if num2 % 2 == 0:
        p_2 = "Par"
    else:
        p_2 = "Impar"

    if p_1 == p_2:
        print(f"os dois númeos são {p_1}.")
    else:
        print(f"O Primeiro número é {p_1} e o segundo é {p_2}.")


n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

par_impar(n1, n2)



#2 CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.
def multiplicar_tres(a, b, c):
    return a * b * c

n1 = float(input("Digite o primeiro numero "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numeo: "))

resultado = n1*n2*n3

print("Resultado: ", resultado)


#3 CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.

def elevar(base, expoente):
    return base ** expoente

base = float(input("Digite seu numero base: "))
expoente = float(input("Digite o expoente"))

resultado = elevar(base, expoente)
print("Resultado; ", resultado)


#4 CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.

def verificar_idade(idade):
    if idade ==18:
        print("Voce tem 18 anos!")
    else:
        print("Idade diferente de 18.")
    
    idade_usuario = int(input("Digite sua idade: "))

    verificar_idade(idade_usuario)


#5 DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.
def calcular_idade(ano_nascimento, ano_atual):
    idade =  ano_atual - ano_nascimento
    return idade

nascimento = int(input("Digite a idade do seu nascimento: "))
atual = int(2026)

idade = calcular_idade(nascimento, atual)
print("Sua idade é: ", idade)

#6 Desenvolva uma funçao para saber se o brasil foi campeão da copa de 1999


titulos_brasil = [1958, 1962, 1970, 1994, 2002]
ano = int(input("Digite o ano de copa: "))    
    
def brasil_campeao():

    if ano == len(titulos_brasil):
        print("Brasil foi campeão 😁")
    else:
        print("Brasil não foi campeão 😔")
brasil_campeao()

#7 DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.  
cardapio = ['Salada', 'Macarronada', 'Sanduiche', 'Sorvete']

def cumprimentar():
    print('🍽️Seja bem vindo!')
    print("Escolha os intens do cardapio \n")

def restaurante():
    pedido = [] 

    while True:
        print("Cardapio: ")
        for i in range(len(cardapio)):
            print(f'{i+1} - {cardapio[i]}')
        print('0 - Finalizar o pedido')

        escolha = input('Digite o número do item: ')

        if escolha == 0:
            break
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(cardapio):
                item = cardapio[escolha-1]
                pedido.append(item)
                print(f'✅{item} adicionado ao pedido \n')
            else:
                print("❌ Número inválido \n")
        else:
            print("❌ Digite apenas números \n")

    print("\n📋 Seu pedido: ")
    if len(pedido) == 0:
        print("Nenum item escolhido.")
    else:
        for item in pedido:
            print('-', item)

cumprimentar()
restaurante()
    

