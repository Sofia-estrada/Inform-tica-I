import datetime
base_datos=[]
def edadcalcular(fecha):
    hoy=datetime.date.today()
    edad=hoy.year-fecha.year-((hoy.month,hoy.year)<(fecha.month,fecha.year))
    return edad
def crearpaciente():
        print("\nIngrese los siguientes datos\n")
        nombre= input("Nombre: ")
        ID=int(input("Identificación: "))
        fechai=input("Fecha de nacimiento (DD/MM/YYYY): ")
        fecha= datetime.datetime.strptime(fechai, "%d/%m/%Y").date()
        edad= edadcalcular(fecha)
        eps=input("EPS: ")
        paciente=[nombre,ID,fecha,edad,eps]
        return paciente
def guardarpaciente(paciente):
    base_datos.append(paciente)
def buscarpaciente():
    iD=int(input("\nIngrese la identificación del paciente: "))
    encontrado=False
    for paciente in base_datos:
        if iD in paciente:
            print("\nDatos del paciente\n")
            print(f"Nombre: {paciente[0]}")
            print(f"Identificación: {paciente[1]}")
            print(f"Fecha de nacimiento: {paciente[2]}")
            print(f"Edad: {paciente[3]} años")
            print(f"EPS: {paciente[4]}")
            encontrado=True
            break
        if not encontrado:
            print("Paciente no encontrado")
def menu():
    while True:
        print("HISTORIA CLÍNICA\n".center(90))
        opcion=int(input("""\nMenú
                         \n1. Ingresar paciente
                         \n2. Buscar paciente
                         \n3. Salir\n"""))
        if opcion==1:
            paciente=crearpaciente()
            guardarpaciente(paciente)
        if opcion==2:
            buscarpaciente()
        if opcion==3:
            print("\nPacientes registrados\n")
            for paciente in base_datos:
                print(f"Nombre: {paciente[0]}")
                print(f"Identificación: {paciente[1]}")
                print(f"Fecha de nacimiento: {paciente[2]}")
                print(f"Edad: {paciente[3]} años")
                print(f"EPS: {paciente[4]}\n")
            break

menu()
        