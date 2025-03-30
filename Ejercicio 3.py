while True:
    n=int(input("Ingrese un valor para n de máximo 9: "))
    if n<=9:
        break
    else:
        print("Valor ingresado mayor a 9, vuelva a intentar")
while True:
    x=int(input("Ingrese un valor para x de máximo 9: "))
    if x<=9:
        break
    else:
        print("Valor ingresado mayor a 9, vuelva a intentar")
c=0
while c<=x:
    r=n**c
    print (f'Los resultados son {r}')
    c+=1
    