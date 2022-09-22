class macaco:
    def __init__(self, nome, bucho=None):
        self.nome = nome
        self.bucho = bucho
        self.barriga = list()
   
    
    
    def comer(self,comida):
        self.barriga.append(comida)
        self.bucho = self.barriga
        
        
    def verBucho(self):
        if self.barriga:
            print()
            print('Estômago:', end = ' ')
            for c in self.barriga:
                print(c, end = ', ')
        else:
            print()
            print(f'O bucho de {self.nome} está vazio')
    
    
    def digerir(self,valor):
        if valor in self.barriga:
            self.barriga.remove(valor)
            print()
            print(f'\033[31m{valor} foi digerido\033[m')
            print()
        else:
            print()
            print(f'\n{self.nome} não comeu isso')
    
    
m1 = macaco('Jorge','Sim')
m2 = macaco('JonJon')

m1.comer('Banana')
m1.comer('Laranja')
m1.comer('Maça')

m1.verBucho()
m1.digerir('Graviola')
m1.digerir('Maça')
m1.verBucho()


