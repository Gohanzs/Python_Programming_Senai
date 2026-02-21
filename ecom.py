# mercado(dicionarios, listas, variaveis)


# cadastro no e-commerce, acessar o e-commerce, verificar a lisa de produtos, comprar um produto

# Criar o e-commerce 



# cadastrono e-commerce

dados = {

        'login': [],
        'senha': [],
        'produtos':{
            1 : ['Computador Dell', 5000.0],
            2 : ['Memoria ram', 3200.00],
            3 : ['Mouse Redragon', 2000.00],
            4 : ['Monitor Pichau CRS24B', 890.00]
            }

}
print('Cadastre-se')
cad_login = input('Cadastre o seu login: ')
cad_senha = input('Cadastre a sua senha: ')
dados['login'].append(cad_login)
dados['senha'].append(cad_senha)

#Acessar o e-commerce
print('Acesse a aplicação')

acesso_login = input('Digite seu login para acessar: ')
acesso_senha = input('Digite sua senha para acessar: ')

if acesso_login == dados['login'][0] and acesso_senha == dados['senha'][0]:
    print('Seja bem vindo!')

    # verifica a lista de produtos
    print('produtos')
    produto = input (f'''
    
    {dados['produtos']} 
    
    
    ''')



# comprar produto
    carrinho = []
    valores = []
    carrinho.append(dados['produtos'][produto][0])
    valores.append(dados['produtos'][produto][1])
    print(carrinho)
    print(carrinho[0], valores[0])





    #paga o produto
    soma = sum(valores)
    print('Valor a pagar - R$')













else:
    print('Seu login não esá correto! ')
    print('Tente novamente')