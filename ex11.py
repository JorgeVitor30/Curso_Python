class bichinho_vitual:
    from datetime import datetime
    data_atual = datetime.now()
    horario = datetime.strftime(data_atual, '%H:%M')
    dia = data_atual.day
    def __init__(self,nome,fome,saude,idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        
    def alterar_nome(self,valor):
        self.nome = valor

        
    def dia_aleatorio(self,valor):
        self.dias_passados = self.dia - valor
       
       
    def dar_comida(self,valor):
        self.fome += valor
   
    
    def sts_fome(self):
        '''self.tempo = horario.split(':')
        self.hora = self.tempo[0]
        self.min = self.tempo[1]'''
        self.data = bichinho_vitual.dia  
        self.fome -= self.dias_passados * 5
        return self.fome
        
        
    def alt_saude(self,valor):
        self.saude = valor
        
    def alt_idade(self,valor):
        if valor > self.idade:
            self.saude -=  0.25 * (valor - self.idade)
            self.idade = valor
        else:
            pass
        
    def status(self):
        self.humor = (3 * self.fome + 2 * self.saude) / 5.75
        print('-=' * 25)
        print(f'Nome: {self.nome}')
        print(f'Fome: {self.fome:.2f}')
        print(f'Saúde: {self.saude:.2f}')
        print(f'Idade: {self.idade}')
        print(f'Humor: {self.humor:.2f}')
        
        print('-=' * 25)
        print()
    
   

b1 = bichinho_vitual('Careca',80 ,70 ,18)
b2 = bichinho_vitual('Levy',75 ,60 ,20)

b1.dia_aleatorio(15)

b1.sts_fome()
b1.dar_comida(5)


b1.status()
# FOME TÁ 60 , AMANHÃ É PRA TAR 65


b2.alt_idade(50)


b2.status()
