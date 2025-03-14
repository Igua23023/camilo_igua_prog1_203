
n = int(input("Ingrese un número: "))
if n <= 1:
    print(f"{n} no es un número primo.")
else:
    for i in range(2, n):  
        if n % i == 0:
            print(f"{n} no es un número primo.")
    else:
        print(f"{n} es un número primo.")
