from Registros.registro import Trade, RegistrosTrading

menu = """1-Agragar un Trade
2-Listar Registros
3-Ganacia/Perdida Total
4-Eliminar
=>"""

elim = '''1-Si
2-No
=>'''

def main():
    while True:
        print(''.center(35,'='))    
        print(' Registros de Trading '.center(35,'~'))
        opcion = input(menu)
        print(''.center(35,'~'))
        print(''.center(35,'='))
        print()
        if opcion == '1':
            print(' Agregar un Trade '.center(35,'='))
            en = input('Derivado del trade: ')
            tipo = input('LONG/SHORT: ')
            margen = float(input('Ingrese el margen: $'))
            apalancamiento = input('Ingrese el apalancamiento: X')
            apertura = input('Ingrese la fecha de apertura: ')
            cierre = input('Ingrese la fecha de cierre: ')
            tarifa = float(input('Ingrese la tarifa: $'))
            gan_per = float(input('Ingrese la Ganacia/Perdida: $'))
            trade = Trade(en,tipo,margen,apertura,cierre,tarifa,gan_per,apalancamiento)
            RegistrosTrading.agregar_trades(trade)
            print(''.center(35,'='))
            print()
        elif opcion == '2':
            print(''.center(35,'='))
            print(' Listar Trades '.center(35,'='))
            RegistrosTrading.mostrar_trades()
            print(''.center(35,'~'))
            print(''.center(35,'='),'\n')
        elif opcion == '3':
            print(' Ganancias/Perdidas '.center(35,'='))
            RegistrosTrading.recuento_ganacias()
            print(''.center(35,'='))
            print()
        elif opcion == '4':
            print(' Eliminar Registros '.center(35,'='))
            print('Seguro que desea eliminar todos los trades?')
            x = input(elim)
            if x == '1':
                RegistrosTrading.eliminar()
                print(''.center(35,'='))
            else:
                continue
        else:
            break

if __name__ == '__main__':
    main()