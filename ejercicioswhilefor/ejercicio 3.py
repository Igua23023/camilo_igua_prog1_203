n = int(input("Ingrese un número: "))
suma = 0 
for i in range(1, n):
    if n % i == 0:
        suma += i 
if suma == n:
    print(f"{n} es un número perfecto.")
else:
    print(f"{n} no es un número perfecto.")
