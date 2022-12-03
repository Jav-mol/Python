import os

class Venta():  
    def __init__(self, fecha, monto) -> None:
        self.monto = monto
        self.fecha = fecha
    
    def __str__(self) -> str:
        return f'Fecha: {self.fecha} \nMonto: {self.monto}\n'
            
class Registro():
    contador = 'contador.txt'
    archivo = 'Registro.txt'
    monto_final = 'Monto.txt'
    monto_final_Int = None
    contador_id = None
    sumaMonto = 0
    
    @classmethod
    def suma_contador(cls):
        cls.contador_id = 0
        with open(cls.contador, 'a') as contador:
            contador.write(f'{1}\n')
        with open(cls.contador, 'r') as contador:
            for linea in contador:
                linea = int(linea)
                cls.contador_id += linea
    @classmethod
    def agregar_venta(cls, venta):
        cls.suma_contador()
        with open(cls.archivo, 'a') as archivo:
            archivo.write(f'Id Venta: {cls.contador_id} \n{venta.__str__()} \n')
        
        with open(cls.monto_final,'a') as monto:
            monto.write(f'{venta.monto}\n')
        
        cls.monto_final_Int = 0
        with open(cls.monto_final, 'r') as monto:
            for linea in monto:
                linea = int(linea)
                cls.monto_final_Int += linea 
    @staticmethod
    def montoCero():
        Registro.monto_final_Int = 0
        with open(Registro.monto_final, 'r') as monto:
            for line in monto:
                line = int(line)
                Registro.monto_final_Int += line
                
                
    @classmethod
    def monto_total(cls):
        print(f'El monto total es:$ {cls.monto_final_Int}')
    
    @classmethod
    def mostar_registro(cls) -> str:
        with open(cls.archivo, 'r') as archivo:
           print (f'{archivo.read()}')
    
    @classmethod
    def eliminar(cls):
        os.remove(cls.archivo)
        os.remove(cls.contador)
        os.remove(cls.monto_final)