# Pedir número al usuario
n = int(input("Ingrese un número entero positivo: "))

# Generar la secuencia de Collatz
while n != 1:
    print(n)  # Imprimir el número en una línea nueva
    if n % 2 == 0:  # Si es par, dividir entre 2
        n //= 2
    else:  # Si es impar, multiplicar por 3 y sumar 1
        n = 3 * n + 1

print(n)  # Imprimir el último número (siempre será 1)
