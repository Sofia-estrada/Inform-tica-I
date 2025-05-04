import datetime
import random

pacientes= {}
IDs= set() #un conjunto para que no se repitan los numeros de los codigos

def generar_id(tipo:str) -> str:
    """
    Genera la ID de cada paciente ingresado de manera aleatoria en un formato de 001 a 999
    """
    while True:
        numero= random.randint(1, 999)
        id_paciente= f"{tipo}{numero:03d}"
        if id_paciente not in IDs:
            IDs.add(id_paciente)
            return id_paciente
def validar_edad() -> int:
    """
    Cuando se ingresa un string en edad marca error, se usa try/except para no romper el código
    y que el usuario ingrese de nuevo

    """
    while True:
     try:
         edad= int(input("Edad: "))
         return edad
     except ValueError:
         print("Error, debe ser un número entero")
         
def ingresar_paciente() -> None:
    """
    Contiene los datos que el usario debe ingresar, los organiza en formato
    dividido por / y los guarda en el diccionario pacientes, asignándoles la llave (la ID)

    """
    tipo= input("Tipo de paciente (P. Perros, G. Gatos, A. Aves, T. Tortugas): ").upper()
    if tipo not in ('P', 'G', 'A', 'T'):
        print("Tipo no válido.")
        return
    nombre= input("Nombre: ")
    edad= validar_edad()
    razon= input("Razón de visita: ")
    hora= datetime.datetime.now().strftime("%H:%M:%S")
    diagnostico= input("Diagnóstico: ")
    info= f"{nombre}/{edad}/{razon}/{hora}/{diagnostico}"
    id_paciente= generar_id(tipo)
    pacientes[id_paciente]= info
    print(f"Paciente ingresado con ID: {id_paciente}")

def editar_paciente() -> None:
    """
    Primero verifiva que el ID exista y luego convierte el string en una lista
    separando los elementos después del /, edita las variables de acuerdo a las
    posiciones de la lista creada
    """
    try:
        id_paciente= input("Ingrese el ID del paciente a editar: ")
        h= pacientes[id_paciente].split("/")
    except KeyError:
        print("ID no encontrado.")
        return

    h= pacientes[id_paciente].split("/")
    print(f"\nInformación actual de {id_paciente}:")
    print(f"1. Nombre: {h[0]}")
    print(f"2. Edad: {h[1]}")
    print(f"3. Razón de visita: {h[2]}")
    print(f"4. Diagnóstico: {h[4]}")

    opcion= input("\n¿Qué desea editar? (1-4): ")

    if opcion== "1":
        h[0]= input("Nuevo nombre: ")
    elif opcion== "2":
        nueva_edad= validar_edad()
        h[1]=str(nueva_edad)
    elif opcion== "3":
        h[2]= input("Nueva razón de visita: ")
    elif opcion == "4":
        h[4]= input("Nuevo diagnóstico: ")
    else:
        print("Opción no válida.")
        return

    h[3]= datetime.datetime.now().strftime("%H:%M:%S")
    pacientes[id_paciente]= "/".join(h)
    print("Información actualizada correctamente.")

def eliminar_paciente() -> None:
    """
    Elimina al paciente del diccionario y del conjunto con la clave (ID)
    """
    id_paciente = input("Ingrese el ID del paciente a eliminar: ")
    if id_paciente in pacientes:
        pacientes.pop(id_paciente)      
        IDs.remove(id_paciente)
        print("Paciente eliminado.")
    else:
        print("ID no encontrado.")

def mostrar_pacientes() -> None:
    """
    Muestra los datos ingresados conviertiendo los elementos asociados a cada clave
    en una lista para mostrar cada elemento según su posición

    """
    if not pacientes:
        print("No hay pacientes registrados.")
        return

    print("\n--- Lista de Pacientes ---")
    for idp, info in pacientes.items():
        h= info.split("/")
        print(f"\nID: {idp}")
        print(f"Nombre: {h[0]}")
        print(f"Edad: {h[1]}")
        print(f"Razón de visita: {h[2]}")
        print(f"Hora de visita: {h[3]}")
        print(f"Diagnóstico: {h[4]}")
        print("-" * 30)
        
def buscar_paciente() -> None: 
    """
    Convierte cualquier letra que se ingrese en minúscula, así como al elemento que
    corresponde a nombre del diccionario, los compara y muestra los pacientes
    que corresponden

    """
    letra= input("Ingrese la letra inicial del nombre: ").lower()
    resultados= list(filter(lambda item: item[1].split("/")[0].lower().startswith(letra), pacientes.items()))

    if resultados:
        print(f"\nPacientes cuyos nombres comienzan con '{letra.upper()}':")
        for idp, info in resultados:
            h= info.split("/")
            print(f"\nID: {idp}")
            print(f"Nombre: {h[0]}")
            print(f"Edad: {h[1]}")
            print(f"Razón de visita: {h[2]}")
            print(f"Hora de visita: {h[3]}")
            print(f"Diagnóstico: {h[4]}")
            print("-" * 30)
    else:
        print("No se encontraron pacientes con esa letra inicial.")

def menu() -> None:
    """
    Define el menú y llama a cada función creada para que se ejecute según el 
    usuario desee

    """
    while True:
        print("\n--- Sistema de Gestión de Pacientes ---")
        print("1. Ingresar paciente")
        print("2. Editar paciente")
        print("3. Eliminar paciente")
        print("4. Mostrar pacientes")
        print("5. Buscar paciente")
        print("6. Salir")
        opcion= input("Seleccione una opción: ")
        if opcion== "1":
            ingresar_paciente()
        elif opcion== "2":
            editar_paciente()
        elif opcion== "3":
            eliminar_paciente()
        elif opcion== "4":
            mostrar_pacientes()
        elif opcion=="5":
            buscar_paciente()
        elif opcion== "6":
            break
        else:
            print("Opción no válida.")

menu()

