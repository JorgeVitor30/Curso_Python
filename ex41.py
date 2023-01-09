
class AppSettings:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, *kwargs)
        return cls._instance

    def __init__(self):
        self.tema = 'Tema Claro'
        self.font = '18px'


if __name__ == "__main__":
    as1 = AppSettings()
    as2 = AppSettings()
    as3 = AppSettings()

    as1.nome = 'Luiz'
    as1.tema = 'Tema Escuro'
    print(as1.tema)


print(as1)
print(as2)
print(as2.nome)
print(as2.tema)
