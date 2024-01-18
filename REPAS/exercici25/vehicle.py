import json
class Vehicle:
    def __init__(self, modelo, marca, color, altura, anchura, longitud):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.altura = altura
        self.anchura = anchura
        self.longitud = longitud
    
    def get_modelo(self):
        return self.modelo
    
    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_marca(self):
        return self.marca
    
    def set_marca(self, marca):
        self.marca = marca

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    def get_altura(self):
        return self.altura
    
    def set_altura(self, altura):
        self.altura = altura

    def get_anchura(self):
        return self.anchura
    
    def set_anchura(self, anchura):
        self.anchura = anchura

    def get_longitud(self):
        return self.longitud
    
    def set_longitud(self, longitud):
        self.longitud = longitud

    def parts(self):
        print(f'modelo: {self.modelo}, marca: {self.marca}, color: {self.color}, altura: {self.altura}, anchura: {self.anchura}, longitud: {self.longitud}')
        
    def to_dict(self):
        data = {
                    "modelo" : self.modelo,
                    "marca" : self.marca,
                    "color" : self.color,
                    "altura" : self.altura,
                    "anchura" : self.anchura,
                    "longitud" : self.longitud
                }
        
        return data

vehicle1 = Vehicle("model 3", "Tesla", "blanco", "1.50m", "2.1m", "4.5m")
vehicle1.parts()
print(vehicle1.to_dict())