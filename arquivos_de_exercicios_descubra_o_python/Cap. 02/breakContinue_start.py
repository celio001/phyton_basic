#
# Exemplo de como usar os comando Break e Continue
#
def lookbreak():
    for x in range(5,10):
        if x == 7:
            break
        print('O valor de x é: ', x)

#lookbreak()

def loopContinue():
    for x in range(5,10):
        if x == 7:
            continue
        print('Valor de x é: ', x)

loopContinue()