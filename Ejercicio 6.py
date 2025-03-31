n=int(input("Ingrese el número de términos n: "))
while True:
    a=float(input("Ingrese el valor de a: "))
    if a!=0:
        break
    else:
        print("Número inválido, ingrese un número diferente de 0")
suma=0
i=1
while i<=n:
    suma+=(1/a)**i
    i+=1
print(f"El resultado de la suma es: {suma}")
