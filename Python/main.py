from Funciones.CalculadoraDeImpuestos import main as CalculadoraImpuestos
from Funciones.Grados import main as Grados
from Funciones.Monedas import main as CalculadoraMonedas
from Funciones.SumarMultiplicar import main as SumarMultiplicar
from Funciones.Contraseña import main as Contraseñas
from Funciones.adivinaElNumero import main as AdivinaElNumero

iniciofin = '='*30
menuInicio = f"""{iniciofin}\n{'-'*12} MENU {'-'*12}
1-Ejercicio I
2-Ejercicio II
3-Ejercicio III 
4-Ejercicio IV
5-Ejercicio V
6-Ejercicio VI
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
    
    
