from itertools import count
nome = []
media = []
indice = count()

for x in range(0,2):
    nome.append(str(input('Digite o seu nome: ')).title())
    media.append(float(input('Sua média: ')))

lista = list(zip(indice,nome,media))
    
    
a = 'ID'
b = 'NOME'
c = 'MÉDIA'

print('-='*15)
print(f'{a:<10} {b:>7} {c:>11}')
for ind , nome , media in lista:
    print(f'{ind:<10} {nome:>8} {media:>8}')
print('-='*16)  
