class StringReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{k}={v}' for k,v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'



class MonoStateSimple(StringReprMixin):
    _state = {
        'x': 10,
        'y': 20,
    }
    
    def __init__(self, nome=None, sobrenome=None):
        self.__dict__ = self._state
        
        
        if nome is not None:
            self.nome = nome
        if sobrenome is not None:
            self.sobrenome = sobrenome  
            


m1 = MonoStateSimple('Luiz')
m2 = MonoStateSimple()
print(m1)
print(m2)



