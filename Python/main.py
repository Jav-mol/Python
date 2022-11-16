from modulos import *

iniciofin = '='*30
menuInicio = f"""{iniciofin}\n{'-'*12} MENU {'-'*12}
1-Calculadora de Impuestos
2-Convertidor de Grados
3-Convertidor de Monedas
4-Sumar-Multiplicar Listas
5-Generador de Contraseñas
6-Adivina El Numero
=>"""

def ejercicios(menu):
        global x
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
            print(iniciofin)  
            return False
        return True

def main():
    x = True
    while True:
        if x:
            menu = input(menuInicio)
            x = ejercicios(menu)
        else:
            break

if __name__ == '__main__':    
    main()
    
    
