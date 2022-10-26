from threading import Thread
from time import sleep
from threading import Lock


class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        
        super().__init__()
    
    def run(self):
        sleep(self.tempo)
        print(self.texto)
        
        
    
t1 = MeuThread('Qualquer Texto 1', 5)
t1.start()

t2 = MeuThread('Qualquer Texto 2', 9)
t2.start()

t3 = MeuThread('Qualquer Texto 3 ', 6)
t3.start()


for i in range(20):
    print(i)
    sleep(1)
'''
   
''' 
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)
    
t = Thread(target = vai_demorar, args=('Ola mundo', 5))
t.start()
# t.join()   é um block da thread

while t.is_alive():
    print('Esperando a Thread')
    sleep(1)
 
print('Thread acabou!')



class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()
        
    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print('N temos mais ingressos suficientes')
            self.lock.release()
            return
        sleep(1)
        
        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s).\n'
              f'ainda tem no estoque {self.estoque} no estoque\n')
        self.lock.release()
    
if __name__ == '__main__':
    ingressos = Ingressos(10)
    
    for i in range(1,10):
        t = Thread(target = ingressos.comprar, args = (1,))
        t.start()
    
    print(ingressos.estoque)
