while True:
    factorial=1
    c=1
    while True:
        f=int(input("Ingrese un número entre 1 y 20: "))
        if f>=1 and f<=20:
            break
        else:
            print("Valor no aceptado")
    while c<=f:
        factorial *=c
        c+=1
    print(f"El factorial de {f}! es:", factorial)
    p=int(input("Desea continuar? 1-SI, 2-NO: "))
    if p!=1:
        print ("Ok, hasta la próxima")
        break
        
        

