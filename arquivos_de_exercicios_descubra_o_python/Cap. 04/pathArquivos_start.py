#
# Arquivo com exemplos de como trabalhar com paths
#

from os  import path
import time

def DadosArquivos():
    ArquivoExiste = path.exists('NovoArquivo.txt')
    ehDiretorio = path.isdir('NovoArquivo.txt')
    pathArquivi = path.realpath('NovoArquivo.txt')
    pathRelativo = path.realpath('NovoArquivo.txt')
    dataCriacao = time.ctime(path.getctime('NovoArquivo.txt'))
    dataModificacao = time.ctime(path.getmtime('NovoArquivo.txt'))

    print(ArquivoExiste)
    print(ehDiretorio)
    print(pathArquivi)
    print(pathRelativo)
    print(dataCriacao)
    print(dataModificacao)

DadosArquivos()