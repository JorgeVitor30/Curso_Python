from random import randint

class Pessoa:
    def __init__(self,nome,idade,sexo,id):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.id = id
    
        print('-=' * 15)
        print(f'{(self.nome).title()} de {self.idade} anos seu id é: {self.id} ')
        if self.idade >= 16:
            print()
            print('Você Está apto a votar')
            
        if self.sexo and self.idade >= 70  == 'M':
            print(f'{self.nome} Você está apto a se aposentar')
        elif self.sexo and self.idade >= 65 == 'F':
            print(f'{self.nome} Você está apto a se aposentar')
        else:
            print(f'Ainda faltam {70 - self.idade} anos para a sua aposentadoria')
        
        

while True:
    resp = int(input('Digite uma opção: [0 to exit , 1 to cadastro]: '))
   
    
    if resp == 1:    
        n1 = str(input('Digite seu nome: '))
        idad1 = int(input('Digite sau idade: '))
        sexo = str(input('Digite sau sexo[M/F]: ').upper())
        Pessoa(n1,idad1,sexo,randint(1000,9999))
        
    if resp == 0:
        break
    
    
