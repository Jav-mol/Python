from POO.FigurasGeometricas.figuras import *
#from figuras import Rectangulo, Circulo, probar_figuras
menu = '''1-Rectangulo
2-Circulo
3-Salir
=>'''

def main():
    print('='*30,'\n')
    while True: 
        print('~'*30)
        print('~'*4,'Figuras Geometricas','~'*5)
        opcion = input(menu)
        if opcion == '1':
            print('='*30)
            print('~'*9,'RECTANGULO','~'*9)
            nombre = input('Ingrese el nombre del reactangulo: ')
            perimetro = int(input('Ingrese el perimetro: '))
            base = int(input('Ingrese la base: '))
            rectangulo1 = Rectangulo(nombre,base,perimetro)
            print('~'*30)
            probar_figuras(rectangulo1)
            print('~'*30)
            print('='*30,'\n')
        elif opcion == '2':
            print('='*30)
            print('~'*10,'CIRCULO','~'*11)
            nombre = input('Ingrese el nombre del Circulo: ')
            radio = int(input('Ingrese el radio: '))
            circulo1 = Circulo(nombre,radio)
            print('~'*30)
            probar_figuras(circulo1)
            print('~'*30)
            print('='*30,'\n')
        elif opcion == '3':
            return
        else:
            print('Error')
            
if __name__ == '__main__':
    main()