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
            
class VeiculoFactory(ABC): # abstract
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
            
           
           
class ZonaNorteVeiculoFactory(VeiculoFactory):
    staticmethod
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

class ZonaSulVeiculoFactory(VeiculoFactory):
    staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'Popular':
            return CarroPopular()
        if tipo == 'Moto Popular':
            return Moto_Popular()
        assert 0, 'Veiculo não existe'           
        
if __name__ == "__main__":
    from random import choice
    carros_disponiveis_zona_norte = ['Luxo', 'Popular','Moto Popular','Moto Luxo']
    carros_disponiveis_zona_sul = ['Popular','Moto Popular']
    
    print('NORTE')
    for i in range(10):
        carro = VeiculoFactory(choice(carros_disponiveis_zona_norte))
        carro.buscar_cliente()
    
    print('-='*20)
    print('SUL')
    for i in range(10):
        carro2 = VeiculoFactory(choice(carros_disponiveis_zona_sul))
        carro2.buscar_cliente()
           
        
