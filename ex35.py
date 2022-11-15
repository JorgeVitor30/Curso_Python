
from collections.abc import Callable
from typing import TypeVar

lista_inteiros : list[int] = [1,2,3,4]
lista_string : list[str] = ['a', 'b', 'c', 'd']
lista_inteiros : list[tuple] = (1,2,3,4)
lista_listas_int : list[list[int]] = [[1],2,3,4]


um_dict : dict[str, int] = {
    "A" : 0,
    "B" : 1,
    "C" : 2 
}
um_dict_de_listas : dict[str, list[int]] = {
    "A" : [1,2],
    "B" : [3,4],
    "C" : [5,6] 
}

um_set_de_inteiros : set[int] = {1,2,3}

ListaInteiros = list[int]
DictListaInteiros = dict[str, ListaInteiros]

um_dict_de_listas2 : DictListaInteiros = {
    "A" : [1,2],
    "B" : [3,4],
    "C" : [5,6] 
    
}

string_e_inteiros : str | int = 1
lista: list[int | str] = [1, 2, 3, 'a']



def soma(x: int, y: float | None = None) -> float:
    if isinstance(y , float):
        return x + y
    return x + x

SomaInteiros = Callable[[int, int], int]

def executa(func: SomaInteiros, a: int, b: int) -> int:
    return func(a,b)

T = TypeVar('T')

def get_item(list: list[T], index: int) -> T:
    return list[index]

list_int = get_item([1,2,3], 1)
list_str = get_item(['a', 'b', 'c'], 1)


class Person:
    def __init__(self, fn, ln) -> int:
        self.fn = fn
        self.ln = ln
    
    def full_name(self):
        return f'{self.fn} , {self.ln}'
   
   
    
def say_name(person: Person) -> str:
    return person.full_name
    
