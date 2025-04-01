contperros=0
contfelinos=0
listaperros=[]
listagatos=[]
print(f"Bienvenido al sistema de clinica veterinaria UdeA".upper().center(90))
while True:
    opcion=int(input("""Ingrese: \n
                     \r1- Ingresar nuevo paciente
                     \r2- Ver cantidad de pacientes
                     \r3- Mostrar promedio de edades
                     \r4- Cantidad de pacientes críticos y graves
                     \r5- Ver paciente
                     \r6- ver todos los pacientes
                     \r7- Salir\n"""))
    if opcion==1:
        mas=[]
        mas.append(input("Ingrese el nombre del animal: "))
        mas.append(int/input("Ingrese \n0 - Si es perro \n1- Si es gato\n"))
        mas.append(int(input("Ingrese la edad del paciente: ")))
        while True:
            est=int(input("Ingrese: \n0- Si es grave \n1- Si es crítico\n"))
            if est==0:
                print("Grave")
                break
            elif est==1:
                print("Crítico")
                break
            else:
                print("Ingrese una opción correcta")
    
        if mas[1]==0:
            mas[1]="Perro"
            contperros+=1
            codigo=f"Can{contperros:03d}"
            mas.append(codigo)
            listaperros.append(mas)
        elif mas[1]==1:
            mas[1]="Gato"
            contfelinos+=1
            codigo="Felinos%03d" % contfelinos
            mas.append(codigo)
            listagatos.append(mas)
    elif opcion==2:
        op=int(input("Ingrese para ver \n1- Cantidad de perros \n2- Cantidad de gatos"))
        if op==1:
            print(len(listaperros))
        elif op==2:
            print(len(listagatos))
    elif opcion==3:
        sum_ages=0
        for i in listagatos:
            sum_ages+=i[2]
        for i in listaperros:
            sum_ages+=i[2]
        print(f"El promedio de edad es: {(sum_ages/len(sum_ages))}")
    elif opcion==3:
        
    elif opción==4:
        
        
            