# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números

def MCD(a, b):
    while b:
        a, b = b, a % b
    return a

def mcm(a, b):
    return (a * b) // MCD(a, b)

num1 = int(12)
num2 = int(8)

resultado = mcm(num1, num2)
print(f"El mínimo común múltiplo entre {num1} y {num2} es {resultado}")

