import time
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    time.sleep(0.5)
    c = 1
    for items in lista:
        print(f'{c} - {items}')
        c+=1
    print(linha())
    opc = leiaInt('Sua resposta: ')
    while opc<1 or opc > len(lista):
        print('Erro, digite um valor válido')
        opc = leiaInt('Sua resposta: ')
    return opc


def retornar(lista, texto=''):
    cabeçalho(texto)
    c = 1
    for items in lista:
        print(f'{c} - {items}')
        c+=1
    print(linha())
    opc = leiaInt('Sua resposta: ')
    while opc<1 or opc > len(lista):
        print('Erro, digite um valor válido')
        opc = leiaInt('Sua resposta: ')
    return opc


def linha(tam=42):
    return '~' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def formatarCPF(cpf):
    cpf = str(cpf).zfill(11)  # garante 11 dígitos com zeros à esquerda
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

def formatarTelefone(tel):
    tel = str(tel).zfill(11)  # 11 dígitos com DDD
    return f'({tel[:2]}) {tel[2:7]}-{tel[7:]}'


def leiaDinheiro(valor):
    ok = False
    while not ok:
        n = str(input(valor)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'ERRO,{n} NÃO É UM PREÇO VÁLIDO.')
        else:
            ok = True
            return float(n)


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg)) 
        except ValueError as erro:
            print(f'Erro. Digite apenas números inteiros.')
        else:
            return n
            
    
def leiafloat(msg):
    while True:
        try:
            n = input(msg).replace(',', '.')
            n = float(n)
        except ValueError as erro:
            print(f'ERRO. Digite apenas números reais.')
        else:
            return n