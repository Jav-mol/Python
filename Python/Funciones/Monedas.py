menu = '''       1-JPY - USD
       2-GBP - USD
       3-CAD -USD
       4-Salir
       =>'''

def monedas(mon):
    jpy = 0.0068
    gbp = 1.147
    cad = 0.74
    if mon == '1':
        cantidad = int(input('Ingrese la cantidad de JPY: '))
        print(f'JPY: ${cantidad} equivalen a\nUSD: ${cantidad*jpy:.2f}')
        print('~'*30,'\n')
    elif mon == '2':    
        cantidad = int(input('Ingrese la cantidad de GBP: '))
        print(f'GBP: ${cantidad} equivalen a\nUSD: ${cantidad/gbp:.2f}')
        print('~'*30,'\n')
    elif mon == '3':
        cantidad = int(input('Ingrese la cantidad de CAD: '))
        print(f'CAD: ${cantidad} equivalen a\nUSD: ${cantidad*cad:.2f}')
        print('~'*30,'\n')
    elif mon == '4':
        print('~'*30,'\n')
        return False
    else:
        print('\n  ERROR; opcioin incorrecta')
        print('~'*30,'\n')
    return True   

def main():
    x = True
    while True:
        print('~'*4,'CONVERSOR DE MONEDAS','~'*4)
        moneda = input(menu)
        x = monedas(moneda)
        if x:
            pass
        else:
            break
if __name__ == '__main__':
    main()