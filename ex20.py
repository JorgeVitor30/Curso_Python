import os

caminho_procura = 'C:/Users/I5 11400F/Desktop/TERMOS'
termo_procura = '18'

# OS.WALK FAZ O PROGRAMA ANDAR PELOS ARQUIVOS

def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3 
    tera = base ** 4
    peta = base ** 5
    
    if tamanho < kilo:
        tamanho = tamanho
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'  
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'  
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'   
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'
        
    tamanho = round(tamanho,2)
    return f'{tamanho}{texto}'


conta = 0
for raiz, diretorios , arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:    
            try: 
                conta +=1
                caminho_completo = os.path.join(raiz, arquivo)          
                nome_arquivo , ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo) # PEGAR TAMANHO
                print()
                
                print('Encontrei o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Ext:', ext_arquivo)
                print('Tamanho:', tamanho)
                print('Tamanho fortamatado',formata_tamanho(tamanho))
                
            except PermissionError as e:
                print('Sem Permissões')
            except  FileNotFoundError as e:
                print('Arquivo nao encontrado')
            except Exception as e:
                print('Erro n conhecido!', e)    
                
print()       
print(f'{conta} arquivo(s) encontrado')      
