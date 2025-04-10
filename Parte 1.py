datos_pacientes = [
    ['Maria', 58, 'M', '107/82 mmHg', 67, 59.5, 1.51, 'No', 'No'],
    ['Juan', 72, 'H', '130/88 mmHg', 78, 75.2, 1.73, 'Si', 'No'],
    ['Ana', 45, 'M', '110/75 mmHg', 55, 50.8, 1.60, 'No', 'Si'],
    ['Pedro', 65, 'H', '145/95 mmHg', 85, 82.1, 1.85, 'Si', 'No'],
    ['Laura', 38, 'M', '120/80 mmHg', 60, 55.3, 1.68, 'No', 'No'],
    ['Carlos', 80, 'H', '150/90 mmHg', 92, 88.7, 1.78, 'Si', 'Si'],
    ['Sofia', 25, 'M', '115/78 mmHg', 50, 48.5, 1.55, 'No','No'],
    ['Luis', 52, 'H', '135/85 mmHg', 70, 68.9, 1.70, 'Si', 'No'],
    ['Elena', 68, 'M', '125/82 mmHg', 75, 70.1, 1.65, 'No','Si'],
    ['Miguel', 40, 'H', '118/76 mmHg', 62, 60.5, 1.75, 'No', 'No']
]

nPaciente = 1

for paciente in datos_pacientes: 
    print(f'Paciente No. {nPaciente}')
    print(f"Nombre: {paciente[0]}")
    print(f'Edad: {paciente[1]}')
    print(f'Sexo: {paciente[2]}')
    print(f'Presión arterial: {paciente[3]}')
    print(f'Frecuencia cardiaca: {paciente[4]}')
    print(f'Peso: {paciente[5]}')
    print(f'Altura: {paciente[6]}')
    print(f'Diabetes: {paciente[7]}')
    print(f'Hipertensión: {paciente[8]}')
    print()
    nPaciente+= 1
while True:
    while True:
        buscar = int(input('Buscar:\n 1. Diabéticos. \n 2. Hipertensos.\n 3. Tercera edad.\n'))
        if buscar==1 or buscar==2 or buscar==3:
            break
        else:
            print('Valor inválido, intente nuevamente\n')
    if buscar==1:
        print('Los pacientes diabéticos son los siguientes: \n')
        c=0
        for indice, paciente in enumerate(datos_pacientes, start=1): 
            if paciente[7]=='Si':
                print(f'Paciente No. {indice}')
                print(f"Nombre: {paciente[0]}")
                print(f'Edad: {paciente[1]}')
                print(f'Sexo: {paciente[2]}')
                print(f'Presión arterial: {paciente[3]}')
                print(f'Frecuencia cardiaca: {paciente[4]}')
                print(f'Peso: {paciente[5]}')
                print(f'Altura: {paciente[6]}')
                print(f'Diabetes: {paciente[7]}')
                print(f'Hipertensión: {paciente[8]}')
                print()
                c+=1
        print(f"El total de pacientes diabéticos es {c}")
    elif buscar==2:
        print('Los pacientes Hipertensos son los siguientes: \n')
        d=0
        for indice, paciente in enumerate(datos_pacientes, start=1):
            if paciente[8]=='Si':
                print(f'Paciente No. {indice}')
                print(f"Nombre: {paciente[0]}")
                print(f'Edad: {paciente[1]}')
                print(f'Sexo: {paciente[2]}')
                print(f'Presión arterial: {paciente[3]}')
                print(f'Frecuencia cardiaca: {paciente[4]}')
                print(f'Peso: {paciente[5]}')
                print(f'Altura: {paciente[6]}')
                print(f'Diabetes: {paciente[7]}')
                print(f'Hipertensión: {paciente[8]}')
                print()
                d+=1
        print(f"El total de pacientes hipertensos es {d}")
    elif buscar==3:
        print('Los pacientes de tercera edad son los siguientes:')
        e=0
        for indice, paciente in enumerate(datos_pacientes, start=1):
            if paciente[1]>=60:
                print(f'Paciente No. {indice}')
                print(f"Nombre: {paciente[0]}")
                print(f'Edad: {paciente[1]}')
                print(f'Sexo: {paciente[2]}')
                print(f'Presión arterial: {paciente[3]}')
                print(f'Frecuencia cardiaca: {paciente[4]}')
                print(f'Peso: {paciente[5]}')
                print(f'Altura: {paciente[6]}')
                print(f'Diabetes: {paciente[7]}')
                print(f'Hipertensión: {paciente[8]}')
                print()
                e+=1
        print(f"El total de pacientes de tercera edad es {e}\n")
    continuar=int(input("¿Desea continuar? 1. Si 2. No \n"))
    if continuar==2:
        print ("Hasta la próxima")
        break
        
            
        
        
    ...