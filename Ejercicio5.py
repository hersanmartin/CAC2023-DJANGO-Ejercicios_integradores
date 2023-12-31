# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una 
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero 
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el 
# ejercicio tanto de manera iterativa como recursiva

def get_int():
    while True:
        try:
            valor = int(input("Ingrese un valor entero: "))
            return valor
        except ValueError:
            print("Error: Ingrese un valor entero válido.")

# Ejemplo de uso
valor_entero = get_int()
print("Valor entero ingresado:", valor_entero)






