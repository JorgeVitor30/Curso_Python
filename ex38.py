# QQLR COISA
from abc import ABC, abstractclassmethod



class Veiculo:
    @abstractclassmethod
    def buscar_cliente(self) -> None:
        pass
    
class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo está buscando o cliente...')
        
class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro Popular está buscando o cliente...')
        
class Moto_Popular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto Popular está buscando o cliente...')        
      
class Moto_Luxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de Luxo está buscando o cliente...')    
            
class VeiculoFactory:
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)
    
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'Luxo':
            return CarroLuxo()
        if tipo == 'Popular':
            return CarroPopular()
        if tipo == 'Moto Popular':
            return Moto_Popular()
        if tipo == 'Moto Luxo':
            return Moto_Luxo()
        assert 0, 'Veiculo não existe'
            
    def buscar_cliente(self):
        self.carro.buscar_cliente()    
            
        
if __name__ == "__main__":
    from random import choice
    carros_disponiveis = ['Luxo', 'Popular','Moto Popular','Moto Luxo']
    
    for i in range(10):
        carro = VeiculoFactory(choice(carros_disponiveis))
        carro.buscar_cliente()
        
        
        
