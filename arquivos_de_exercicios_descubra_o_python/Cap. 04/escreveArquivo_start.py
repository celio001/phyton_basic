#
# Escrevendo arquivos com funções do Python
#
def EscreveAquivo():
    arquivo = open('NovoArquivo.txt', 'w+')

    arquivo.write('linha gerada com a funcao Escreve Arquivo \r\n')

    arquivo.close()

#EscreveAquivo()
def AlteraAquivo():
    arquivo = open('NovoArquivo.txt', 'a+')

    arquivo.write('linha gerada com a funcao Escreve Arquivo \r\n')

    arquivo.close()

AlteraAquivo()