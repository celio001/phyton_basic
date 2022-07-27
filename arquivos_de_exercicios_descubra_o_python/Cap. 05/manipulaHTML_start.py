# 
# Exemplo de processamento e parse de HTML
#
from html.parser import HTMLParser

class MeuParse(HTMLParser):
    def handle_starttag (self, tag, attrs):
        print('Tag de abertura encontrada!')
        if attrs.__len__() > 0:
            for a in attrs:
                print('  Valores encontrados  ', a[0], ' = ', a[1])
    
    def handle_endtag(self, tag):
        print('Tag de fechamento encontrada')
    
    def handle_comment(self, data):
        print('Comentario encontrado.')

    def handle_comment(self, data):
        print('Valores encontrados.')
        if data.isspace():
            print('O valor encontrado é um espaço')
        
        else:
            print('O valor encontrado é: ', data)

def MeuObjeto():
    MeuParse1 = MeuParse()
    arquivo = open('C:\\Users\\User\\Documents\\ESTUDOS LINKEDIN\\arquivos_de_exercicios_descubra_o_python\\Cap. 05\\exemplohtml.html', 'r')
    dados = arquivo.read()
    MeuParse1.feed(dados)

MeuObjeto()