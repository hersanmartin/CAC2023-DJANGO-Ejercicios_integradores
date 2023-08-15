# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada 
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función 
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la 
# palabra más repetida y su frecuencia.

def contar_palabras(cadena):
    # Dividir la cadena en palabras
    palabras = cadena.split()
    
    # Crear un diccionario para almacenar las frecuencias
    frecuencias = {}
    
    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    
    return frecuencias

def palabra_mas_repetida(diccionario):
    if not diccionario:
        return None, 0
    
    palabra_max = max(diccionario, key=diccionario.get)
    frecuencia_max = diccionario[palabra_max]
    
    return palabra_max, frecuencia_max

# Ejemplo de uso
cadena_ejemplo = "Nos los representantes del pueblo de la Nación Argentina, reunidos en Congreso General Constituyente por voluntad y elección de las provincias que la componen, en cumplimiento de pactos preexistentes, con el objeto de constituir la unión nacional, afianzar la justicia, consolidar la paz interior, proveer a la defensa común, promover el bienestar general, y asegurar los beneficios de la libertad, para nosotros, para nuestra posteridad, y para todos los hombres del mundo que quieran habitar en el suelo argentino: invocando la protección de Dios, fuente de toda razón y justicia: ordenamos, decretamos y establecemos esta Constitución, para la Nación Argentina."

frecuencias = contar_palabras(cadena_ejemplo)
tpalab_frec_max = palabra_mas_repetida(frecuencias)

print("Palabra más repetida:", tpalab_frec_max[0])
print("Frecuencia de la palabra más repetida:", tpalab_frec_max[1])
