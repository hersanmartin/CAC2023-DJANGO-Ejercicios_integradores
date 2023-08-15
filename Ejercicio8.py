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



class Titular:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        

class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
    
    def mostrar(self):
        return f"Titular: {self.titular}\nCantidad: {self.cantidad}"


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
    
    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self.bonificacion
    
    def es_titular_valido(self):
        edad = self.titular.edad # Supongamos que la clase Titular tiene un atributo "edad"
        return 18 <= edad < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido() and self.cantidad >= cantidad:
            self.cantidad -= cantidad
            return True
        return False
    
    def mostrar(self):
        return f"Cuenta Joven\n{super().mostrar()}\nBonificación: {self.bonificacion}%"




# Ejemplo de uso
titular_joven = Titular("Juan", 20)
cuenta_joven = CuentaJoven(titular_joven, 1000, 5)

print(cuenta_joven.mostrar())
print("Es titular válido:", cuenta_joven.es_titular_valido())
print("Retiro exitoso:", cuenta_joven.retirar(200))






