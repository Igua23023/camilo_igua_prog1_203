# Pedir el número al usuario
n = int(input("Ingrese un número: "))

suma = 0  # Inicializar suma

# Extraer dígitos y sumarlos
while n > 0:
    suma += n % 10  # Obtener el último dígito y sumarlo
    n //= 10  # Eliminar el último dígito

print(f"La suma de los dígitos es: {suma}")
