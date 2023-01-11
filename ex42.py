def singleton(the_class):
    instances = {}
    
    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]
    
    return get_class
    


@singleton
class AppSettings:
    def __init__(self):
        self.tema = 'Tema Escuro'
        self.font = '18px'
        
if __name__ == "__main__":
    as1 = AppSettings()
    as2 = AppSettings()
    as3 = AppSettings()
    as1.tema = 'O tema claro'
    print(as1.tema)

    print(as2.tema)


      
