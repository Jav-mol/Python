from Manejo_Archivos.Registros_Tienda.registro import Registro,Venta

menu = """1-Agregar Venta
2-Monto Total
3-Mostrar Registro
4-Eliminar
=>"""

def main():
    while True:
        print(''.center(30,'~'))
        print(' Registro De Ventas '.center(30,'~'))
        opcion = input(menu)
        print(''.center(30,'~'))
        if opcion == '1':
            print(' Agregando Venta '.center(30,'-'))
            fecha = input('Ingrese la fecha: ')
            monto = int(input('Ingrese el monto:$ '))
            venta = Venta(fecha,monto)
            Registro.agregar_venta(venta)
        elif opcion == '2':
            print(' Monto Final '.center(30,'-'))
            if Registro.monto_final_Int == None:
                Registro.montoCero()
            Registro.monto_total()
        elif opcion == '3':
            try:
                print(' Mostrar Registros '.center(30,'-'))
                Registro.mostar_registro()
            except:
                print(' Error '.center(30,'-'))
                print('Aun no se a agredo ningun registro')
        elif opcion == '4':
            print(' Eliminando Registros '.center(30,'-'))
            Registro.eliminar()
        else:
            break
        
if __name__ == '__main__':
    main()