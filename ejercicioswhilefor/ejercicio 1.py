n= int(input("Ingrese un número: "))
for i in range(1, n + 1):  
    if n % i == 0:  
        print(i)
print(f"Los divisores de {n} son:")