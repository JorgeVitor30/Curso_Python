class bombaCombustivel:
    def __init__(self, qtdTanque , limiteTanque = 55):
        self.qtdTanque = qtdTanque
        self.maxTanque = limiteTanque
        self.qtd_bomba = 1000
        self.litroG = 5.25
        self.litroA = 4.97


        
    def abastecerPorValor(self, real, tipo):
        if tipo == 'gasolina' and (self.qtdTanque + real / self.litroG) < self.maxTanque:
            a = self.qtdTanque
            self.qtdTanque += real / self.litroG
            self.qtd_bomba -= self.qtdTanque - a
            print()
            print(f'\033[32mAbestecido {real/self.litroG:.2f} L com sucesso!\033[m')
        else:
            print()
            print('\033[31mO tanque do carro não suporta esse tanto de Litros\033[m')
            print()
            
        if tipo == 'alcool' and (self.qtdTanque + real / self.litroA) < self.maxTanque:
            b = self.qtdTanque
            self.qtdTanque += real / self.litroA 
            self.qtd_bomba -= self.qtdTanque - b
            print(f'\033[32mAbestecido {real/self.litroG:.2f} L com sucesso!\033[m')
            
            
    def abastecerPorLitro(self,valor,tipo):
        if tipo == 'gasolina' and (self.qtdTanque + valor ) < self.maxTanque:
            c = self.qtdTanque
            self.qtdTanque += valor * self.litroG 
            self.qtd_bomba -= valor - c
  
        
        if tipo =='alcool' and (self.qtdTanque + valor) < self.maxTanque:
            d = self.qtdTanque
            self.qtdTanque += valor * self.litroA
            self.qtd_bomba -= valor - d
   
        
    
    def alterarValor(self,valor,tipo):
        if tipo == 'gasolina':
            self.litroG = valor
        if tipo == 'alcool':
            self.litroA = valor
    

    def mostrar_tanque(self):
        print(self.qtdTanque)
    

    def completa_tanque(self,tipo):
        self.abastecerPorLitro((self.maxTanque - self.qtdTanque) ,tipo)



carro1 = bombaCombustivel(5) 
carro2 = bombaCombustivel(2)
carro3 = bombaCombustivel(10)

carro1.abastecerPorLitro(40,'gasolina')


carro1.completa_tanque('gasolina')


carro3.completa_tanque('alcool')
carro3.mostrar_tanque()
