    #Aula 7

#Cria lista sozinho
l = list(range(1,200,10))
print(l)

#Acessando indices
lista =[1,2,3,4]
print(lista[0] + lista[2])

# alteração de vaor do indice

lista[3] = 100
print(lista)
print(lista[2]**2)

#alterar / verificar dado da lista
# inserção

# append() - add no final da lista
lista.append(100)

#Verifica os metodos que posso utilizar
print(dir(lista))

#insert() - add apartir do indice que foi declarado
lista.insert(0,'teste')
print(lista)

# extend() - add no final da lista varios números

lista.extend([1,2,3,4,5,6,7,8,9,10])
print(lista)

#-----------------------------


# Remover dados da lista

# remove - remove a partir do valor

lista.remove('teste')

# pop - remove o ultimo

lista.pop

#pop(indice) - remove o indice

lista.pop(0)

print (lista)


#del - remove a partir do indice

del lista[1]
print(lista)


# ------------------------------------

# metodos e funcoes que verificam algum dado da lista
# ações - Ordem alfabética
print(min(lista)) # Menor valor
print(max(lista)) # Maior valor
print('Tamanho',len(lista)) # quantos intens de valor declarado
print(lista.count(3)) # contagem da lista, por ordem alfábetica ou do '<' para o '>'


#ordenar lista

lista.sort()
lista.sort(reverse=True)


# sum - soma a lista

print(sum(lista))

# copy - copiar
x = lista.copy()
print(x)


#indice

x = lista.index(10)
print('posicao',lista)