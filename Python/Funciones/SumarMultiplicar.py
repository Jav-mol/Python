def sumarMultiplicar():
    while True:
        ejercicio = input('1-Sumar \n2-Multiplicar\n>')
        if ejercicio == '1':
            while True:
                numero = input('Ingrese los numero a sumar: ')
                if numero == '':
                    break
                else:
                    numero = int(numero)
                    numeros.append(numero)
            
            print(F'\nEl resultado de la suma de {numeros} es: {sumar(*numeros)}') 
            break
        elif ejercicio == '2':
            while True:
                numero = input('Ingrese los numero a multiplicar: ')
                if numero == '':
                    break
                else:
                    numero = int(numero)
                    numeros.append(numero)
            print(F'\nEl resultado de la multiplicacion de {numeros} es: {multiplicar(numeros)}') 
            break            
def main():
    global numeros
    global sumar
    global multiplicar

    numeros = []
    def sumar(*args):
        resultado = 0
        for num in args:
            resultado += num
        return resultado
    def multiplicar(args):
        resultado = 1
        for num in args:
            resultado *= num
        return resultado
    sumarMultiplicar()

if __name__ == '__main__':
    main()