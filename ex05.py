from itertools import zip_longest
a = [3,4,5,6,9]
b = [7,9,3,2,1,3,0,7]


print('-=' * 15)
print('SOMADOR MAIOR')
somador_maior = [x + y for x,y in zip_longest(a,b,fillvalue=0)]
print(somador_maior)


print('-=' * 16)
print('SOMADO MENOR ')

somador_de_A_e_B = [x + y for x, y in zip(a,b)]
print(somador_de_A_e_B)
