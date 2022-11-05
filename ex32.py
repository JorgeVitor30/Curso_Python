def soma(x , y):
    assert isinstance(x , (int, float)), 'x precisa ser INT ou FLOAT'
    assert isinstance(y , (int, float)), 'x precisa ser INT ou FLOAT'
    return x + y

    # é um tratamento de erro mais saudável

try:
    print(soma('3' , 5))
except AssertionError as e:
    print(f'Conta inválida: {e}')
