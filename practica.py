lista_pacientes=[]
lista_gatos=[]
lista_perros=[]
contador_gatos=0
contador_perros=0
print ("BIENVENIDO A LA BASE DE DATOS CLINICA\n".center(60))
while True:
    salirprograma=False
    opcion=int(input("""\nQue desea realizar?
                     \n1. Ingresar paciente
                     \n2. Cantidad de pacientes
                     \n3. Promedio edades de pacientes
                     \n4. Pacientes graves y en estado crítico
                     \n5. Buscar paciente
                     \n6. Mostrar pacientes
                     \n7. Salir\n"""))
    if opcion==1:

            nombre=input("Nombre: ")
            edad=int(input("Edad: "))
            tipo=int(input("Seleccione 1. Felino 2. Canino: "))
            estado=int(input("Seleccione 1. Grave 2. Estado crítico: "))
            
            if tipo==1:
                ID=(f"{contador_gatos:03d}Felino")
                contador_gatos+=1
            if tipo==2:
                ID=(f"{contador_perros:03d}Canino")
                contador_perros+=1
            pacientes=[ID, nombre, edad, tipo, estado]
            lista_pacientes.append(pacientes)
            if tipo==1:
                lista_gatos.append(pacientes)
            else:
                lista_perros.append(pacientes)
            print(f"Paciente registrado con ID; {ID}")
    if opcion==2:
        print(f"Cantidad de perros: {len(lista_perros)}")
        print(f"Cantidad de gatos: {len(lista_gatos)}")
    if opcion==3:
        resultado=0
        cantidad=0
        for pacientes in lista_pacientes:
            resultado+=pacientes[2]
            cantidad+=1
        if cantidad>0:
            print(f"El promedio de las edades ingresadas es: {resultado/cantidad} ")
        else:
            ("No se han ingresado edades")
    if opcion==4:
        critico=0
        grave=0
        for pacientes in lista_pacientes:
            if pacientes[4]==1:
                grave+=1
            if pacientes[4]==2:
                critico+=1
        print (f"Cantidad de pacientes graves: {grave}")
        print (f"Cantidad de pacientes criticos: {critico}")
    if opcion==5:
        ident=input("Ingrese la identificación del paciente: ")
        repetido=False
        for paciente in lista_pacientes:
            if ident==paciente[0]:
                repetido=True
            if repetido==True:
                print(f"Nombre: {paciente[1]}")
                print(f"Edad: {paciente[2]}")
                if tipo==1:
                    print("Tipo: Felino")
                if tipo==2:
                    print("Tipo: canino")
                if estado==1:
                    print("Estado: Grave")
                if estado==2:
                    print("Estado: Estado crítico")
            else:
                repetido=False
        if repetido==False:
            print("El paciente no se encuentra en el sistema")
    if opcion==6:
        print("Pacientes ingresados hasta el momento")
        for paciente in lista_pacientes:
            print(f"Nombre: {paciente[1]}")
            print(f"Edad: {paciente[2]}")
            if tipo==1:
                print("Tipo: Felino")
            if tipo==2:
                print("Tipo: canino")
            if estado==1:
                print("Estado: Grave")
            if estado==2:
                print("Estado: Estado crítico")
    if opcion==7:
        c=0
        while True:
            salirprograma=False
            salir=int(input("""\n1. Confirmar salidad
                            \n2.Rechazar salida
                            \n3. Ingrese la opción correcta """))
            if salir==1:
                salirprograma=True
                print("Saliendo")
                break
            if salirprograma==True:
                break
            if salir==2:
                break
            else:
                c+=1
                print(f"Ingrese una opción válida {c}/3")
                if c>=3:
                    break
                
    if salirprograma==True:
        break
     
                
                
                
            
            
            
        