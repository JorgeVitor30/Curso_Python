class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso= peso
        self.altura = altura
        
        
    def envelhecer(self,valor):
        if self.idade < 21:
            self.altura =  (valor * 0.04 ) + self.altura
            self.idade += valor
            
        elif self.idade > 60:
            self.altura =  self.altura - (valor * 0.02 ) 
            self.idade += valor
            
        else:
            self.idade += valor
            
        
        
        
    def engordar(self,valor):
        self.peso += valor

    def emagrecer(self,valor):
        self.peso -= valor


p1 = Pessoa('Luana',17, 49, 1.63)
p2 = Pessoa('Aline',18, 54, 1.57)
p3 = Pessoa('Joelma',64, 62, 1.70)

p1.envelhecer(2)
p1.engordar(20)


p2.envelhecer(2)
p2.emagrecer(5)
p2.engordar(10)


p3.envelhecer(8)


print('-='*15)
print()
print(f'Nome : {p1.nome}\nIdade: {p1.idade}\nPeso: {p1.peso}\nAltura: {p1.altura:.2f}')
print()
print('-='*15)
print()
print(f'Nome : {p2.nome}\nIdade: {p2.idade}\nPeso: {p2.peso}\nAltura: {p2.altura:.2f}')
print()
print('-='*16)
print(f'Nome : {p3.nome}\nIdade: {p3.idade}\nPeso: {p3.peso}\nAltura: {p3.altura:.2f}')

