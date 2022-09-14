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
        print(f'Cor: {self.cor}')
        print(f'Raio : {self.raio} cm')
        print(f'Material: {self.material}')
        print('-=' * 15)
        print()
        
    def mostrarArea(self):
        pi = 3.14
        return f'Área: {pow(pi,2) * self.raio:.2f} cm '
        
        
b1 = Bola('Azul',15,'ferro')
b2 = Bola('Amarelo',30,'papel')

b1.trocaCor('Vermelho')


b1.mostraTudo()
b2.mostraTudo()

print(b1.mostrarArea())
print(b2.mostrarArea())
