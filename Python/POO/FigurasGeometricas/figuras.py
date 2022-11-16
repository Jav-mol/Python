class Figuras:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    
    def area(self):
        pass
    
    def perimetro(self):
        pass
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}'
    
class Rectangulo(Figuras):
    def __init__(self, nombre, base, altura) -> None:
        super().__init__(nombre)
        self.base = base
        self.altura = altura
    
    def area(self):
        area = self.altura * self.base
        return f'{area:.2f}'
    
    def perimetro(self):
        perimetro = 2*(self.base + self.altura)
        return f'{perimetro:.2f}'

    def __str__(self) -> str:
        return super().__str__() + f'\nArea: {self.area()}\nPerimetro: {self.perimetro()}'
    
class Circulo(Figuras):
    def __init__(self, nombre, radio) -> None:
        super().__init__(nombre)
        self.radio = radio 
    
    def area(self):
        area = 3.14 * (self.radio**2)
        return f'{area:.2f}'
    
    def perimetro(self):
        perimetro = 2*(3.14*self.radio)
        return f'{perimetro:.2f}'
    
    def __str__(self) -> str:
        return super().__str__() + f'\nPerimetro: {self.perimetro()} \nArea: {self.area()}'
    

def probar_figuras(objeto):
    print(objeto)