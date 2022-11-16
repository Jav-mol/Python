import random

letrasMayu = ['J','A','V','I','E','R','A','D','G','D','S','E','G','H','D','E','R']
letrasMin = ['j','a','v','i','e','r','q','w','e','r','g','s','d','f','g','s','z','c']
numeros = ['1','2','3','4','5','6','7','8','9','0']
simbolos = ['°','#','$','%','&','','=']
contras = []
contraseñaFinal = ''


def contraseña(num):
    global contraseñaFinal
    for i in range(0,num):
        aleat = random.randint(0,3)
        if aleat == 0:
            caracter = random.choice(letrasMayu)
            contras.append(caracter)
        elif aleat == 1:
            caracter = random.choice(letrasMin)
            contras.append(caracter)
        elif aleat == 2:
            caracter = random.choice(numeros)
            contras.append(caracter)
        elif aleat == 3:
            caracter = random.choice(simbolos)
            contras.append(caracter)
    for i in contras:
        contraseñaFinal += i
    #contras = "".join(contras)
    
def main():
    print('~'*8,'Generador de Contraseñas','~'*8)
    numero = int(input('Ingrese el largo de la contraseña: '))
    contraseña(numero)
    print(f'Una contraseña segura puede ser: {contraseñaFinal}')
    print('~'*42)
    
if __name__ == '__main__':
    main()