# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los 
# siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de 
# datos.
#  mostrar(): Muestra los datos de la persona.
#  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.


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
        
    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"DNI: {self.__dni}")
        
    def es_mayor_de_edad(self):
        if self.__edad >= 18:
            return "Si"
        else:
            return "No"

# Ejemplo de uso
nombre = "Juan Roman"
edad = 44
dni = "23276566"

persona = Persona(nombre, edad, dni)
persona.mostrar()

nueva_edad = 17
persona.set_edad(nueva_edad)
persona.mostrar()

nuevo_dni = "24123321"
persona.set_dni(nuevo_dni)
persona.mostrar()

print("¿Es mayor de edad?", persona.es_mayor_de_edad())


