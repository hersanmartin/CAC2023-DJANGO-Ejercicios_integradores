# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).


def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    
    for palabra in palabras:
        palabra = palabra.lower()  # Convertir la palabra a minúsculas para considerar mayúsculas y minúsculas iguales
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
            
    return frecuencia

# Ejemplo de uso
cadena_ejemplo = "Nos los representantes del pueblo de la Nación Argentina, reunidos en Congreso General Constituyente por voluntad y elección de las provincias que la componen, en cumplimiento de pactos preexistentes, con el objeto de constituir la unión nacional, afianzar la justicia, consolidar la paz interior, proveer a la defensa común, promover el bienestar general, y asegurar los beneficios de la libertad, para nosotros, para nuestra posteridad, y para todos los hombres del mundo que quieran habitar en el suelo argentino: invocando la protección de Dios, fuente de toda razón y justicia: ordenamos, decretamos y establecemos esta Constitución, para la Nación Argentina."

# Llamar a la función para contar las palabras y obtener el diccionario de frecuencias
resultado = contar_palabras(cadena_ejemplo)

# Imprimir el diccionario de frecuencias
for palabra, frecuencia in resultado.items():
    print(f"'{palabra}': {frecuencia}")



