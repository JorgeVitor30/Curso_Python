class LogMixin:
        @staticmethod
        def write(msg):
            with open('log.log','a+') as f:
                f.write(msg)
                f.write('\n')
            
        def log_info(self,msg):
            self.write(f'INFO: {msg}')

        def log_error(self, msg):
            self.write(f'ERROR: {msg}')

class Eletronico:
    def __init__(self,nome):
        self._nome = nome
        self._ligado = False
        
    def ligar(self):
        if self._ligado:
            return
        else:
            self._ligado = True
            
    def desligar(self):
        if self._ligado:
            self._ligado = False
        else:
            return
        
class smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False
        
    def conectar(self):
        if self._ligado:
            if self._conectado:
                error = f'{self._nome} Já esta CONECTADO'
                print(error)
                self.log_error(error)
                return
            else:
                info = f'{self._nome} FOI CONECTADO'
                print(info)
                self.log_info(info)
                self._conectado = True
        else:
            error = f'{self._nome} ESTÁ DESLIGADO'
            print(error)
            self.log_error(error)
            return
        
    def desconectar(self):
        if not self._conectado :
            error = f'{self._nome} Já esta DESCONECTADO'
            print(error)
            self.log_error(error)
            return
        else:
            info = f'{self._nome} Foi DESCONECTADO'
            print(info)
            self.log_info(info)
            self._conectado = False

    

cell = smartphone('Celular Xiaomi')
cell.conectar()
cell.desligar()
cell.ligar()
cell.conectar()
cell.desligar()
cell.conectar()
