from modulos import *

iniciofin = '='*30

menuInicio = '''1-Funciones
2-POO
=>'''

menuFunciones = f"""{iniciofin}\n{'-'*7} MENU FUNCIONES {'-'*7}
1-Calculadora de Impuestos
2-Convertidor de Grados
3-Convertidor de Monedas
4-Sumar-Multiplicar Listas
5-Generador de Contraseñas
6-Adivina El Numero
=>"""

menuPoo = f"""{iniciofin}\n{'-'*10} MENU POO {'-'*10}
1-Figuras Geometricas
=>""" 

def funciones(menu):
        if menu == '1':
            print(iniciofin,'\n')
            CalculadoraImpuestos()
        elif menu == '2':      
            print(iniciofin,'\n')
            print(iniciofin) 
            Grados()
            print(iniciofin,'\n')               
        elif menu == '3':
            print()
            print(iniciofin) 
            CalculadoraMonedas()
        elif menu == '4':
            print(iniciofin,'\n')
            print(iniciofin) 
            SumarMultiplicar()
            print(iniciofin,'\n')
        elif menu == '5':
            print(iniciofin,'\n')
            Contraseñas()
            print()
        elif menu == '6':
            print(iniciofin,'\n') 
            AdivinaElNumero()
        else:
            print(iniciofin,'\n')      
            return

def poo(menu):
    if menu == '1':
        FigurasGeometricas()
    else:
        print(iniciofin,'\n')      
        return


def main():
    while True:
        print(iniciofin)
        print('~'*5,'Ejercicios Python','~'*6)
        menu = input(menuInicio)
        print('~'*30)
        if menu == '1':
            print(iniciofin,'\n')
            opcion = input(menuFunciones)
            funciones(opcion)
        elif menu == '2':
            print(iniciofin,'\n')
            opcion = input(menuPoo)
            poo(opcion)
        else:
            print(iniciofin)
            break

if __name__ == '__main__':    
    main()
    
    
