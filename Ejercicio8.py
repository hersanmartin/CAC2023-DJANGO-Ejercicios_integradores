# 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
# CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
# además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
# tanto por ciento. Crear los siguientes métodos para la clase:
#  Un constructor.
#  Los setters y getters para el nuevo atributo.
#  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo 
# tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es 
# mayor de edad pero menor de 25 años y falso en caso contrario.
#  Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
#  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la 
# cuenta.


class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
    
    def get_dni(self):
        return self.__dni
    
    def set_dni(self, nuevo_dni):
        if len(nuevo_dni) == 8:  # Validación básica de longitud de DNI
            self.__dni = nuevo_dni

    def es_mayor_de_edad(self):
        return self.__edad >= 18


class CuentaJoven(Persona):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular)
        self.__cantidad = cantidad
        self.__bonificacion = bonificacion

    def get_titular(self):
        return self.__titular
    
    def set_titular(self, nuevo_titular):
        self.__titular = nuevo_titular
        
    def get_cantidad(self):
        return self.__cantidad
    
    def set_cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad
        
    def get_bonificacion(self):
        return self.__bonificacion
    
    def set_bonificacion(self, nueva_bonificacion):
        self.__bonificacion = nueva_bonificacion

    def es_titular_valido(self):
        return self.es_mayor_de_edad() and self.get_edad() < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)

    def mostrar(self):
        super().mostrar()
        print(f"Cuenta Joven\nBonificación: {self.__bonificacion}%")

# Ejemplo de uso
titular_joven = "María Gómez"
cuenta_joven = CuentaJoven(titular_joven, bonificacion=10.0)

cuenta_joven.set_edad(20)
cuenta_joven.mostrar()

cuenta_joven.ingresar(1000)
cuenta_joven.retirar(200)
cuenta_joven.mostrar()








