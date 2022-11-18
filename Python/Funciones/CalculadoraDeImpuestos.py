def calculadora():
    monto = int(input("        Ingrese el ($) monto: $"))
    impuesto = (int(input("        Ingrese el '%' de impuesto: %")))/100
    total = monto + (monto*impuesto)
    print(f'        El monto total a pagar es: {total}') 
    print('~'*42,'\n')
    
def main():
    print('~'*7,'Calculadora De Impuestos;','~'*8)
    calculadora()

if __name__ == '__main__':
    main()