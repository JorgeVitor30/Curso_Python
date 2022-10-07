class Eletronico:
    def __init__(self,nome):
        self.nome = nome
        self.ligado = False
        
        
    def ligar(self):
        if self.ligado:
            print('O dispositivo ja está LIGADO')
            pass
        else:
            print('O dispositivo foi LIGADO')
            self.ligado = True
            
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print('O dispositivo foi DESLIGADO')
        else:
            print('O dispositivo ja está DESLIGADO')
        
        

class Geladeira(Eletronico):
    def __init__(self, nome):
        super().__init__(nome)
        self.comer = False
        self.porta = False

    def abrir(self):
        if self.ligado:
            if self.porta:
                pass
            else:
                self.porta = True
        else:
            print('O Dispositivo está DESLIGADO')

    def fechar(self):
        if self.ligado:
            if self.porta:
                self.porta = False
            else:
                pass
        else:
            print('O dispositivo está DESLIGADO')
            
    def pegar_alimento(self):
        if self.ligado:
            if self.porta:
                self.comer = True
                print('Você conseguiu pegar o alimento com SUCESSO')
            else:
                print('A porta do dispositivo está FECHADO')
        else:
            print('O dispositivo está DESLIGADO')

geladeira = Geladeira('LG')
geladeira.ligar()
geladeira.abrir()
geladeira.ligar()
geladeira.desligar()
geladeira.pegar_alimento()
geladeira.ligar()


