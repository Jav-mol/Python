def grados():
    menuGrados = '''1-Celsius a Fahrenheit
2-Fahrenheit a Celsius
=>'''
    while True:
        print('~~~ Calculadora de grados ~~~')
        grado = input(menuGrados)
        if grado == '1':
            c = float(input('\nIngrese los grandos Celsius: '))
            f = c * 1.8 + 32
            print(f'El equivalente de {c} Celsius es: {f} Fahrenheit \n')
        elif grado == '2':
            f = float(input('\nIngrese los grandos Fahrenheit: '))
            c = (f - 32) * (5/9)
            print(f'El equivalente de {f} Fahrenheit es: {c:.2f} Celsius \n')
        else:
            break

def main():
    grados()

if __name__ == '__main__':
    main()