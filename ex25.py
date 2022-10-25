import PyPDF2
import os


caminho_dos_pdfs = r'C:\Users\I5 11400F\Desktop\trabalhandopdf\pdf'


novo_pdf = PyPDF2.PdfFileMerger()
for root, dirs , files in os.walk(caminho_dos_pdfs):
    for file in files:
        caminho_completo_arquivo = os.path.join(root , file)
        
        arquivo_pdf = open(caminho_completo_arquivo, 'rb') #rb = LEITURA EM BY
        novo_pdf.append(arquivo_pdf)
        

with open(f'{caminho_dos_pdfs}/novo_arquivo.pdf', 'wb') as meu_novo_pdf: #wb  WRITE EM BY
    novo_pdf.write(meu_novo_pdf)
  


#with open(r'C:\Users\I5 11400F\Desktop\trabalhandopdf\novo_arquivo.pdf' , 'rb') as arquivo_pdf:
   #leitor = PyPDF2.PdfFileReader(arquivo_pdf)
   #num_paginas = leitor.getNumPages()
    
