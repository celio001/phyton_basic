# 
# Arquivo com exemplos para manipulação de dados na Internet
#

import urllib.request


def conectaInternet():
    objUrl =   urllib.request.urlopen('http://www.google.com')

    if objUrl.getcode() == 200:
        dados = objUrl.read()
        print(dados)

conectaInternet()
