from POO.FigurasGeometricas.figuras import *
#from figuras import Rectangulo, Circulo, probar_figuras
menu = '''1-Rectangulo
2-Circulo
3-Salir
=>'''

def main():
    while True:
        opcion = input(menu)
        if opcion == '1':
            nombre = input('Ingrese el nombre del reactangulo: ')
            perimetro = int(input('Ingrese el perimetro: '))
            base = int(input('Ingrese la base: '))
            rectangulo1 = Rectangulo(nombre,base,perimetro)
            probar_figuras(rectangulo1)
        elif opcion == '2':
            nombre = input('Ingrese el nombre del Circulo: ')
            radio = int(input('Ingrese el radio: '))
            circulo1 = Circulo(nombre,radio)
            probar_figuras(circulo1)
        elif opcion == '3':
            return
        else:
            print('Error')
            
if __name__ == '__main__':
    main()