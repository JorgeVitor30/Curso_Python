class Bola:
    def __init__(self,cor,raio,material):
        self.cor = cor
        self.raio = raio  
        self.material = material
        
    
    def trocaCor(self,valor):
        self.cor = valor.title()
    
    def mostraCor(self):
        return self.cor
        
    def mostraTudo(self):
        print('-=' * 15)
        print(f'Cor: {self.cor.title()}')
        print(f'Raio : {self.raio} cm')
        print(f'Material: {self.material.title()}')
        print('-=' * 15)
        print()
        
    def mostrarArea(self):
        pi = 3.141
        return f'Área: {pow(pi,2) * self.raio:.2f} cm² '
        
        
b1 = Bola('Azul',15,'ferro')
b2 = Bola('Amarelo',30,'papel')
b3 = Bola('marrom',12,'aluminio')


b1.trocaCor('Vermelho')


b1.mostraTudo()
b2.mostraTudo()
b3.mostraTudo()


print(b1.mostrarArea())
print(b2.mostrarArea())
