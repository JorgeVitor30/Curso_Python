def soma(x , y):
    """Soma x e y
    
   >>> soma(10,20)
   30
   
   >>> soma(1,20)
   21
    
   """
    assert isinstance(x , (int, float)), 'x precisa ser INT ou FLOAT'
    assert isinstance(y , (int, float)), 'y precisa ser INT ou FLOAT'
    return x + y


def subtrai(x, y):
    """
    Subtrai x e y
    
    >>> subtrai(10,5)
    5
    
    >>> subtrai('1',5)
    Traceback (most recent call last):
    ...
    AssertionError:  x precisa ser INT ou FLOAT    
    """
    assert isinstance(x , (int, float)), 'x precisa ser INT ou FLOAT'
    assert isinstance(y , (int, float)), 'y precisa ser INT ou FLOAT'

    return x - y
    


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)





