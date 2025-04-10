lista_pacientes=[]
print ("Bienvenido al sistema de clasificacion de pacientes con enfermedad renal".center(50))
while True:
    opcion=int(input("""\n ¿Qué desea hacer?
                     \n1. Ingresar paciente
                     \n2. Eliminar paciente
                     \n3. Editar paciente
                     \n4. Mostrar pacientes\n"""))
    if opcion==1:
        print("\nIngrese los siguientes datos\n")
        ID=int(input("Identificación: "))
        repetido=False
        for paciente in lista_pacientes:
            if ID==paciente[0]:
                repetido=True
                print("Identificación repetida, el paciente ya se encuentra en el sistema\n")
        if repetido==True:
            continue
        else:
            nombre=input("Nombre: ")
            edad=int(input("Edad: "))
            sexo=int(input("Sexo 1. M 2. H: "))
            creatina=float(input("Creatinina en suero: "))
            afro=int(input("¿Es el paciente afrodescendiente? 1.Si 2.No: "))
            pacientes=[ID, nombre, edad, sexo, creatina, afro]
            lista_pacientes.append(pacientes)
    if opcion==2:
        while True:
            eliminar=int(input("\nIngrese la identificiación del paciente que desea eliminar: "))
            encontrado=False
            for pacientes in lista_pacientes:
                if eliminar==pacientes[0]:
                    encontrado=True
                    lista_pacientes.remove(pacientes)
                    print("Paciente eliminado exitosamente")
            if encontrado==True:
                break
            if encontrado==False:
                decidir=int(input("El paciente no se encuentra en el sistema, volver a intentar? 1. SI 2. NO: "))
                if decidir==1:
                    continue
                if decidir==2:
                    print("Saliendo...")
                    break
    if opcion==3:
        editar=int(input("\nIngrese la identificaciÃ³n del paciente que desea editar: "))
        repetido=False
        for pacientes in lista_pacientes:
            if editar==pacientes[0]:
                while True:
                    repetido=True
                    que=int(input("""\n¿Qué desea editar?
                                  \n1. Identificación
                                  \n2. Nombre
                                  \n3. Edad
                                  \n4. Sexo
                                  \n5. Creatinina
                                  \n6. Raza\n"""))
                    if que==1:
                        IDN=int(input("Identificación nueva: "))
                        pacientes[0]=IDN
                    if que==2:
                        nombren=input("Nombre nuevo: ")
                        pacientes[1]=nombren
                    if que==3:
                        edadn=int(input("Edad nueva: "))
                        pacientes[2]=edadn
                    if que==4:
                        sexon=int(input("Sexo 1.M 2.H: "))
                        pacientes[3]=sexon
                    if que==5:
                        creatinan=int(input("Creatinina nueva: "))
                        pacientes[4]=creatinan
                    if que==6:
                        razan=int(input("¿Es el paciente afrodescendiente? 1.SI 2.NO: "))
                        pacientes[5]=razan
                    print("Cambio realizado exitosamente")
                    pregunta=int(input("\n¿Desea editar algo más? 1.SI 2.NO: "))
                    if pregunta==1:
                        continue
                    if pregunta==2:
                        break
                break
        else:
            repetido=False
            if repetido==False:
                print("El paciente no se encuentra en el sistema")
                    
                    
    if opcion==4:
        for pacientes in lista_pacientes:
            print(f"\nId= {pacientes[0]}")
            print(f"Nombre= {pacientes[1]}")
            print(f"Edad= {pacientes[2]}")
            if pacientes[3]==1:
                print("Sexo= Mujer")
            if pacientes[3]==2:
                print("Sexo= Hombre")
            print(f"Creatinina= {pacientes[4]}")
            if pacientes[5]==1:
                print("Afrodescendiente= Si")
            if pacientes[5]==2:
                print("Afrodescendiente= No")
            if pacientes[3]==1 and pacientes[5]==1:
                eGFR=(175*(pacientes[4]**-1.154)*(pacientes[2]**-0.203)*0.742*1.212)
                print (f"Nivel de eGFR es: {eGFR}")
            if pacientes[3]==1 and pacientes[5]==2:
                eGFR=(175*(pacientes[4]**-1.154)*(pacientes[2]**-0.203)*0.742)
                print (f"Nivel de eGFR es: {eGFR}")
            if pacientes[3]==2 and pacientes[5]==1:
                eGFR=(175*(pacientes[4]**-1.154)*(pacientes[2]**-0.203)*1.212)
                print (f"Nivel de eGFR es: {eGFR}")
            if pacientes[3]==2 and pacientes[5]==2:
                eGFR=(175*(pacientes[4]**-1.154)*(pacientes[2]**-0.203))
                print (f"Nivel de eGFR es: {eGFR}")
            if eGFR>=90:
                print("CategorÃ­a G1. Normal a alta función renal")
            if eGFR>=60 and eGFR<=89.9:
                print("CategorÃ­a G2. Función renal levemente disminuida")
            if eGFR>=45 and eGFR<=59.9:
                print("CategorÃ­a G3a. Disminución leve a moderada de la función renal")
            if eGFR>=30 and eGFR<=44.9:
                print("CategorÃ­a G3b. Disminución moderada a severa de la función renal")
            if eGFR>=15 and eGFR<=29.9:
                print("CategorÃ­a G4. Disminución severa de la función renal")   
            if eGFR<15:
                print("Categorí­a G5. Insuficiencia renal (Etapa terminal de la ERC)")
            print()
    
                             
                
    
       
                
                
            
            
        
        
