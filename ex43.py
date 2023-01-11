class Meta(type):
    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)
    
class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print("New é executado")
        return super().__new__(cls)
    
    def __init__(self,nome):
        print('INIT É EXECUTADO')
        self.nome = nome
        
    def __call__(self,x,y):
        print('Call chamado')
        
        
p1 = Pessoa('Luiz')
print(p1.nome)

        
        
