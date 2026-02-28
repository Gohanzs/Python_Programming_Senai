#Ex_1
try:
    numero = int(input("Digite seu numero inteiro: "))
    print("Voce digiou o numero: ", numero)
except ValueError:
    print("Erro: você não digitou um número inteiro válido!")


#Ex_2

try:
    n1 = float(input('Digite seu primeiro número'))
    n2 = float(input('Digite seu segundo número'))

    resultado = n1 / n2
    print('Resultado da divisão: ', resultado)

except ZeroDivisionError:
    print('Erro não é possivel dividir por zero!')

#Ex_3 
lista = ["maçã", "banana", "laranja", "uva", "manga"]

try:
    indice = int(input("Digite um índice da lista (0 a 4): "))
    print("Elemento no índice", indice, ":", lista[indice])

except IndexError:
    print("Erro: índice inválido. Não existe elemento nessa posição.")

except ValueError:
    print("Erro: você deve digitar um número inteiro para o índice.")

print("Fim do código.")
