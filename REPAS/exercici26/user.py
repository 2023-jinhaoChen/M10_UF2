import json
class User:
    def __init__(self, nombre, apellido, edad, altura, email, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.email = email
        self.dni = dni
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellido(self):
        return self.apellido
    
    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad):
        self.edad = edad

    def get_altura(self):
        return self.altura
    
    def set_altura(self, altura):
        self.altura = altura

    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email

    def get_dni(self):
        return self.dni
    
    def set_dni(self, dni):
        self.dni = dni

    def saludacio(self):
        print(f'nombre: {self.nombre}, apellido: {self.apellido}, edad: {self.edad}, altura: {self.altura}, email: {self.email}, dni: {self.dni}')
        
    def to_dict(self):
        data = {
                    "nombre" : self.nombre,
                    "apellido" : self.apellido,
                    "edad" : self.edad,
                    "altura" : self.altura,
                    "email" : self.email,
                    "dni" : self.dni
                }
        
        return data
    
user1 = User("Jinhao", "Chen", 27, "1.65m", "jinhaochen1996@gmail.com", "X1234567")
user1.saludacio()
print(user1.to_dict())