lista = []
lista_modif = []

def mostrar(algo):
    print('Tarefas:')
    print(lista)
    
    
def add(resp , lista):
    lista.append(resp)

def desfazer(lista , lista_modif):
    if not lista:
        print('Nada a Desfazer')
        return
    
    ultima_lista = lista.pop()       # LISTA SUPORTE
    lista_modif.append(ultima_lista) 


def refazer(lista , lista_modif):
    if not lista_modif:
        print('Nada pra Refazer')

    ultima_lista = lista_modif.pop()    # LISTA SUPORTE
    lista.append(ultima_lista)
    

while True:
    resp = input('Digite algo pra lista, opção [df (desfazer), rf (refazer) , ls (listar)]:  ')
    print('\033[1;31m0 to exit\033[m')
    print()
    if resp == 'ls':
        mostrar(resp)
        continue
    
    if resp == 'df':
        desfazer(lista , lista_modif)
        continue
    
    if resp == 'rf':
        refazer(lista , lista_modif)
        continue
    
    if resp == '0':
        break
    
    add(resp, lista)
    print('\033[1;32mAdicionado com Sucesso! \033[m')

    
