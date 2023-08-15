# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una 
# persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
# opcional. Crear los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
# directamente, sólo ingresando o retirando dinero.
#  mostrar(): Muestra los datos de la cuenta.
#  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
# negativa, no se hará nada.
#  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números 
# rojos.


class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    def get_titular(self):
        return self.__titular
    
    def set_titular(self, nuevo_titular):
        self.__titular = nuevo_titular
        
    def get_cantidad(self):
        return self.__cantidad
    
    def set_cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad
    
    def mostrar(self):
        print(f"Titular: {self.__titular}")
        print(f"Cantidad: {self.__cantidad}")
        
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad

# Ejemplo de uso
titular = "Juan Roman"
cuenta = Cuenta(titular)

cuenta.ingresar(1000)
cuenta.mostrar()

cuenta.retirar(300)
cuenta.mostrar()

nuevo_titular = "Luz Casal"
cuenta.set_titular(nuevo_titular)
cuenta.mostrar()
