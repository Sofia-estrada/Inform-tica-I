suma=0
c=1
while True:
    n=int(input("Ingrese un número entre 1 y N (positivo): "))
    if n>=1:
        break
    else:
        print("Valor incorrector, vuelva a intentar")
while c<=n:
    suma+=c
    c+=2
print (f'La suma entre los números impares entre 1 y {n} es: ', suma)
    
