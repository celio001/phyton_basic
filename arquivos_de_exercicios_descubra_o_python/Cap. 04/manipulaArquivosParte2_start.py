#
# Exemplos de como trabalhar com arquivos
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def CriaZipModo1():
    #Criou um ponto zip do arquivo cap.4
    shutil.make_archive('ArquivoCompactado', 'zip', 'C:\\Users\\User\\Documents\\ESTUDOS LINKEDIN\\arquivos_de_exercicios_descubra_o_python\\Cap. 04')

#CriaZipModo1()

#determinamos o que queremos dentro do nossos arquivos
def CriaZipModo2():
    with ZipFile('ArquivoZipModo2.zip', 'w') as novoZip:
        novoZip.write("NovoArquivo.bkp")
        novoZip.write("NovoArquivo.txt")
        novoZip.write("zipModo1.zip.zip")

#CriaZipModo2()

def DeletarArquivo():
    os.remove("ArquivoZipModo2.zip")

DeletarArquivo()
