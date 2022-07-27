# 
# Arquivo com exemplo de tratamento de XML
#

import xml.dom.minidom 

def ManipulaXML():
    doc = xml.dom.minidom.parse('C:\\Users\\User\\Documents\\ESTUDOS LINKEDIN\\arquivos_de_exercicios_descubra_o_python\\Cap. 05\\exemploXML.xml')

    print('Nome da primeira tag: ', str(doc.firstChild.tagName))
    primeiroNome = doc.getElementsByTagName('firstname')
    print('O Primeiro nome é: ', primeiroNome[0].firstChild.nodeValue)

    for skill in doc.getElementsByTagName('skill'):
        print('Skill encontrada: ', skill.getAttribute('name'))

ManipulaXML()
