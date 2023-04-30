
def multiplicacao(*args):
    total = 1
    for numero in args:
        total = numero * total
    return total

def inicio():
    lista = []
    x = input('Digite um número para a lista de multiplicação: ')
    x = int(x)
    lista.append(x)
    print(lista)
    continuacao = input('Deseja adicionar mais um número? [S]IM / [N]ÃO: ')
    continuacao = continuacao.upper()
    if continuacao == 'S':
        inicio()
    else:
        lista = tuple(lista)
        multiplicacao1 = multiplicacao(*lista)
        print(f'O valor dos números multiplicados é {multiplicacao1}')
while True:
    inicio()
