# Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
# O consumo é especificado no construtor e o nível de combustível inicial é 0.
# Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
# Forneça um método obterGasolina( ), que retorna o nível atual de combustível.

class carro:
    def __init__(self,kmpl,tanque = 0):
        self.kmpl = kmpl    # km/l
        self.tanque = tanque    #L  
    

    def andar(self, valor):     # valor em km
        if self.tanque > 0 and self.tanque - valor / self.kmpl > 0:
            self.tanque -= valor / self.kmpl
            print(f'O carro andou {valor} km')
        else:
            print()
            print('\033[31mO carro não tem combustível suficiente para andar mais\033[m')

    def mostrarGasolina(self):
        print(f'{self.tanque:.2f} L restantes no tanque')
        print()

    def abastecer(self,valor):
        a = self.tanque
        self.tanque += valor
        print(f'O carro foi abastecido com {valor} L')
        

Fusca = carro(12,5)
Jeep = carro(10)



Fusca.andar(12)
Fusca.andar(250)
Fusca.abastecer(10)
Fusca.andar(50)

Fusca.mostrarGasolina()

Jeep.abastecer(50)
Jeep.andar(100)