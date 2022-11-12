import random
numero = random.randint(0,25)
menu = '''Eliga el nivel de dificultad:
1-Facil: 10 intentos
2-Medio: 5 intentos
3-Dificil: 3 intentos
=>'''

def adivina(num):
    global intentos
    intentos = 0
    if num == '1':
        intentos = 10
    elif num == '2':
        intentos = 5
    elif num == '3':
        intentos = 3
    else:
        print('Error')
        return
    
    print('~'*29)
    print('Adivine un numero al azar entre 0 y 25')
    for i in range(0,intentos):
        intento = int(input('\nIngrese el numero: '))
        if numero > intento:
            intentos -= 1
            print('El numero es mas grande')
            print(f'Te quedan {intentos} vidas')
        elif numero < intento:
            intentos -= 1
            print('El numero es mas chico')
            print(f'Te quedan {intentos} vidas')
        elif numero == intento:
            return True
    return False

def main():
    while True:
        print('~'*5,'ADIVINA EL NUMERO','~'*5)
        dificultad = input(menu)
        final = adivina(dificultad)
        if final:
            print(f'El numero era "{numero}", te quedaron {intentos} vidas \nGANASTE ;)')
            print('~'*29,'\n')
            break
        else:
            print(f'\nPERDISTE :(\nEl numero era "{numero}"')
            print('~'*29,'\n')
            break
if __name__ == '__main__':
    main()