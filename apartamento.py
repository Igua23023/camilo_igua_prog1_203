
largo=int(input("ingrese el largo en metros"))
fondo=int(input("ingrese fondo en metros"))
precio=int(input("ingre valor"))
area=largo*fondo
#print(area)
if area <=30:
    print("apartaestudio")
elif area <=70:
    print("apartamento")
else:
    print("apartamento grande")

total=area*precio
#print(f"el valor es total={total}")
print("el valor es total",total)