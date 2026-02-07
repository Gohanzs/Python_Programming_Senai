ecommerce = {
    'livro': 25.15,
    'tablet':3000.0,
    'fone': 250.0
}

carrinho = {
    'produtos':[],
    'valores':[]
}

produto1 = input('produto: ')
produto2 = input('Produto: ')

carrinho['produtos'].append(produto1)
carrinho['produtos'].append(produto2)
carrinho['valores'].append(ecommerce[produto1])
carrinho['valores'].append(ecommerce[produto2])

soma = sum(carrinho['valores'])

print('Total - R$', soma)

print(carrinho)

formas_pagamento = ['pix', 'cartao de credito', 'cartao de debito']
escolhe_forma = input('Digite sua forma de pagamento: ')

indice = formas_pagamento.index(escolhe_forma)

def pagamento_pix():
    chave_pix = '123.456.78-99'
    print(pagamento_pix)
    print(chave_pix)

def pagamento_credito():
    print('Cartão de credito: ')
    int(input('Número do cartão: '))
    input('Nome do cartão: ')
    int(input('Cvv: '))
    print(f'Parcelamento em {list(range(1,13))[parcelas-1]}x')

def pagamento_debito():
    print('Pagamento com cartão de debito')
    input('nome do cartao')
    int(input('numero do cartao'))
    int(input('Cvv'))

