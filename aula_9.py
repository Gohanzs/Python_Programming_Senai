# estruturas de dados
# 4 tipos dados boleano inteiros decimais texto


# var 
# lista []
# tuplas ()
# conjuntos {} 
# dicionarios{key:valor}


nome  =  'fernando'
lista  =  [1,2,3,5, 'teste']
print(lista[0])
tuplas  =  (1,2,3,6)
prin(tupla[0])
tupla_2 = 1,2,3,6
dicionarios = {
'key':'value',
'key2':{


'a':20


}
}


print(dicionarios['key2']['a'])



# estruturas de fluxo de controle 



nome = input('Digite seu nome: ')

#if nome == 'Fernanda':
 #   pass
#condicional composta
if nome == 'Kaio':
    print('Seja bem vindo', nome)
else:
    print('Não pode acessar')


# condicional composto if elif e else

if nome == 'Kaio':
    print('Seja bem vindo: ')
elif nome != 'Lucas':
    print('Nao pode acessar')
else: 
    print('Faça o cadastro: ')







# mercado(dicionarios, listas, variaveis)


# cadastro no e-commerce, acessar o e-commerce, verificar a lisa de produtos, comprar um produto

# Criar o e-commerce 



# cadastrono e-commerce

dados = {

'login': [],
'senha': []

}
print('Cadastre-se')
cad_login = input('Cadastre o seu login: ')
cad_senha = input('Cadastre a sua senha: ')
dados['login'].append(cad_login)
dados['senha'].append(cad_senha)

#Acessar o e-commerce
print('Acesse a aplicação')

acesso_login = input('Digite seu login para acessar: ')
acesso_senha =input('Digite sua senha para acessar: ')

if acesso_login == dados['login'][0] and acesso_senha['senha'][0]:
    print('Seja bem vindo!')
else:
    print('Seu login não esá correto! ')
    print('Tente novamente')
