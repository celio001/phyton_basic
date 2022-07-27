
# Declarando e inicializando uma variável
f = 0 
print(f)

# declarando a mesma variável novamente
f = 'abc'
print(f)
a = 'ghi'
print(a)

# Gerando um erro, tentando unir variáveis de tipos diferentes
print('Isto é uma string' + str(123))

# Variável Global X Variável local 
def AlgumaFuncao():
    global f
    global a
    f = 'def'
    a = 'hij'
    print(f)

AlgumaFuncao()
print(f)
print(a) 