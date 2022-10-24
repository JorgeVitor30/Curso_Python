import os
import shutil

caminho_original = r'C:\Users\I5 11400F\Desktop\TESTE'
caminho_novo = r'C:\Users\I5 11400F\Desktop\TESTE2'

'''
try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
   print('Pasta Ja existe ')
'''
    
for root ,dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path =os.path.join(caminho_novo,file)
        print(new_file_path)
        
        shutil.move(old_file_path, new_file_path)
