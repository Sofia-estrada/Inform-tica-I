a=int(input("¿Cuántas notas desea ingresar? "))
sumanotas=0
c=0
while c<a:
    while True:
        b=float(input(f'Ingrese la nota {c+1}: '))
        if b>=0 and b<=5:
            break
        else:
            print("Valor inválido, debe ingresar valores entre 0 y 5")
    c+=1
    sumanotas+=b
promedio=(sumanotas/a)
print(f'El promedio de las notas es {promedio}')

    
    
