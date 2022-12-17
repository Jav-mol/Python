import os

class Trade():
    contador = 'Manejo_Archivos/Registros_Trading/Registros/Contador.txt'
    contador_id = 0
    
    @classmethod
    def contador_trade(cls):
        with open(cls.contador, 'a') as contador:
            contador.write(f'{1}\n')
        with open(cls.contador, 'r') as contador:
            for line in contador:
                line = int(line)
                cls.contador_id += line
            return cls.contador_id
            
    def __init__(self,en, tipo, margen, apertura, cierre, tarifa, gan_per,apalancamiento) -> None:
        self.en = en
        self.tipo = tipo
        self.margen = float(margen)
        self.apertura = apertura
        self.cierre = cierre
        self.tarifa = -(float(tarifa))
        self.gan_per = float(gan_per)
        self.apalancamiento = int(apalancamiento)
        self.id = Trade.contador_trade()
        
    def __str__(self) -> str:
        return f'Trade_id: {self.id} \nEn: {self.en} \nTipo: {self.tipo} \nMargen: ${self.margen} \nTarifa: ${self.tarifa} \nGanan/Perd: ${self.gan_per} \nApalancamiento: X{self.apalancamiento} \nFecha de apertura: {self.apertura} \nFecha de cierre: {self.cierre}' 

class RegistrosTrading():
    registros = 'Manejo_Archivos/Registros_Trading/Registros/Trades.txt'
    ganancias = 'Manejo_Archivos/Registros_Trading/Registros/Gana_Perd.txt'
    gananciaTotal = 0
    @classmethod
    def agregar_trades(cls, trade):
        with open(cls.registros, 'a') as trades:
            trades.write(f'\n{trade.__str__()}\n')
        with open(cls.ganancias, 'a') as total:
            total.write(f'{trade.gan_per} \n{trade.tarifa} \n')
            
    @classmethod
    def mostrar_trades(cls):
        with open(cls.registros, 'r') as trades:
            print(trades.read())
    
    @classmethod
    
    def recuento_ganacias(cls):
        cls.gananciaTotal = 0
        with open(cls.ganancias, 'r') as ganancia:
            for line in ganancia:
                line = float(line)
                cls.gananciaTotal += line
            print(f'Las ganacias acumuladas son: ${(cls.gananciaTotal):.2f}')
    
    @classmethod 
    def eliminar(cls):
        os.remove(cls.registros)
        os.remove(cls.ganancias)
        os.remove(Trade.contador)
        

    