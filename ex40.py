# QQLR COISA
from abc import ABC, abstractclassmethod


class VeiculoLuxo(ABC):
    @abstractclassmethod
    def buscar_cliente(self) -> None:
        pass
    
class VeiculoPopular(ABC):
    @abstractclassmethod
    def buscar_cliente(self) -> None:
        pass
    
class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZN está buscando o cliente...')
        
class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro Popular ZN está buscando o cliente...')
        
class MotoPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto Popular ZN está buscando o cliente...')        
      
class MotoLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de Luxo ZN está buscando o cliente...')  
        
#####################################       
        
class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZN está buscando o cliente...')
        
class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro Popular ZN está buscando o cliente...')
        
class MotoPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto Popular ZN está buscando o cliente...')        
      
class MotoLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de Luxo ZN está buscando o cliente...')    
    
class VeiculoFactory(ABC):
    @staticmethod
    def get_carro_luxo(tipo: str) -> VeiculoLuxo:
        pass
    @staticmethod
    def get_carro_popular(tipo: str) -> VeiculoPopular:
        pass
    @staticmethod
    def get_moto_popular(tipo: str) -> VeiculoPopular:
        pass
    @staticmethod
    def get_moto_luxo(tipo: str) -> VeiculoLuxo:
        pass
            
class ZonaNorteVeiculoFactory(VeiculoFactory):
    
    @staticmethod
    def get_carro(tipo: str) -> VeiculoFactory:
        if tipo == 'Luxo':
            return CarroLuxoZN()
        if tipo == 'Popular':
            return CarroPopularZN()
        if tipo == 'Moto Popular':
            return MotoPopularZN()
        if tipo == 'Moto Luxo':
            return MotoLuxoZN()
        assert 0, 'Veiculo não existe'
            
    def buscar_cliente(self):
        self.carro.buscar_cliente()    
   
class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> VeiculoFactory:
        if tipo == 'Luxo':
            return CarroLuxoZS()
        if tipo == 'Popular':
            return CarroPopularZS()
        if tipo == 'Moto Popular':
            return MotoPopularZS()
        if tipo == 'Moto Luxo':
            return MotoLuxoZS()
        assert 0, 'Veiculo não existe'
            
    def buscar_cliente(self):
        self.carro.buscar_cliente()     
         
   
class Filiais:
    def busca_clientes(self):
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_pupular()
            carro_popular.buscar_cliente()
            
            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()
if __name__ == "__main__":
    pass
        
        
        
