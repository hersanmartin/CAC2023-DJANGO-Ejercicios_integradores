# 1. Escribir una función que calcule el máximo común divisor entre dos números.

def MCD(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(18)
num2 = int(24)

resultado = MCD(num1, num2)
print("El máximo común divisor entre", num1, "y", num2, "es:", resultado)


