class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = []

    def insere_end(self, cidade, estado, num):
        self.endereco.append(Estado(cidade, estado , num))


    def listar_end(self):
        for endereco in self.endereco:
            print(self.nome, end = ': ')
            print(endereco.cidade, endereco.estado, endereco.num)
            if endereco.num % 2 == 1:
                print('Taxa mais alta de entrega')
            print()


class Estado:
    def __init__(self, cidade, estado, num):
        self.cidade = cidade
        self.estado = estado
        self.num = num

cliente1 = Cliente('Jorge', 19)
cliente1.insere_end('Fortaleza', 'CE', 450)

cliente1.listar_end()


cliente2 = Cliente('Artur', 47)
cliente2.insere_end('Pernambuco', 'PE', 723)

cliente2.listar_end()


cliente3 = Cliente('Jon', 24)
cliente3.insere_end('Belo Horizonte', 'MG', 289)

cliente3.listar_end()
