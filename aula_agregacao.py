class CarrinhoDeCompra:
    def __init__(self):
        self.produtos = list()
    
    def inserir_Produto(self, produto):
        self.produtos.append(produto)
    
    def listar_Produto(self):
        print()
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        print()
        print(f'O valor total foi de: {total}')
        

    def mais_3000(self):
        print('Produtos com mais de 3000:')
        print()
        for produto in self.produtos:
            if produto.valor > 3000:
                print(produto.nome,produto.valor)
        

class Produto:  # CLASSE FIXA DE PRODUTO, SOMENTE PARA A BASE DO PROGRAMA
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
    


carrinho1 = CarrinhoDeCompra()

p1 = Produto('TV',5000)
p2 = Produto('Celular',2500)
p3 = Produto('Monitor',800)
p4 = Produto('Teclado',500)
p5 = Produto('Geladeira',3500)

carrinho1.inserir_Produto(p1)
carrinho1.inserir_Produto(p2)
carrinho1.inserir_Produto(p3)
carrinho1.inserir_Produto(p4)
carrinho1.inserir_Produto(p5)

carrinho1.listar_Produto()
carrinho1.soma_total()
carrinho1.mais_3000()

