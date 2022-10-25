dados = [
    {'nome': 'Jorge' , 'idade': 18 , 'cep': 60540120 , 'altura' : 1.85},
    {'nome': 'Jonatha' , 'idade': 19 , 'cep': 34343120 , 'altura' : 1.70},
    {'nome': 'Arthur' , 'idade': 30 , 'cep': 60540127 , 'altura' : 1.65},
    {'nome': 'Levy' , 'idade': 28 , 'cep': 60540120 , 'altura' : 1.80},
    {'nome': 'Barros' , 'idade': 17 , 'cep': 89940891 , 'altura' : 1.99},
    {'nome': 'Isabel' , 'idade': 15 , 'cep': 50640120 , 'altura' : 1.70},
    {'nome': 'Felipe' , 'idade': 78 , 'cep': 40840905 , 'altura' : 1.7},
    {'nome': 'Abel' , 'idade': 56 , 'cep':   21054013 , 'altura' : 1.68},
    {'nome': 'Diogo' , 'idade': 98 , 'cep': 658740780 , 'altura' : 1.75},
    {'nome': 'Ellen' , 'idade': 25 , 'cep': 21070328 , 'altura' : 2.10},   
]

def linha():
    print()
    print()    
    print()

print('-=' * 16)
print('Organizado de acordo com a Idade: \n')

a = [x for x in dados]
dados2 = [sorted(a,key = lambda x: x['idade'])]

for x in dados2:
    for c in x:
        print(c)
            
linha()


print('Organizado de acordo com altura maior que 1.75: ')
org_altura = filter(lambda x: x['altura'] > 1.75, dados)

lista_altura = list(org_altura)
print()
for c in lista_altura:
    print(c)

linha()


print('Organizando de acordo com CEP ímpar e Crescente: ')
cep_organizado = filter(lambda x: x['cep'] % 2 != 0, dados)
sort = sorted(cep_organizado, key = lambda x: x['cep'] )
for c in sort:
    print(c)


linha()


print('Organizado de acordo com Ordem Alfabética e Nome com mais de 5 letras: ')
org_od = filter(lambda x:len(x['nome']) > 5, dados)
sort = sorted(org_od, key = lambda x: x['nome'])

for x in sort:
    print(x)



