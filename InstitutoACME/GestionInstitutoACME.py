# INSTITUO EDUCATIVO ACME - Registro e Informe de Notas
# Creado por: Diego Alejandro Mancilla Paipa

import json
import os

#***************************************** MENU Y SUBMENUS *****************************************
#Función Mostrar Menú Principal, con los submenús
def MainMenu():
    while True:
        clear()
        print("\n","=" * 40)
        print("******* INSTITUTO EDUCATIVO ACME ******** ")
        print("      MENÚ PRINCIPAL")
        print("1-   Gestión de Estudiantes")
        print("2-   Gestión de Notas")
        print("3-   Informes Institución")
        print("4-   Salir")
        try:
            Opc = int(input("\t>>Escoja una opción (1-4)? "))
            if Opc < 0 or Opc > 4:                                      #Solo valido opciones entre 1 y 4
                MsgNotify("Opción no valida")
                continue
            else:
                return Opc
        except ValueError:
            print("Error! Ingrese un numero entero valido")

#Función Mostrar SubMenú Estudiantes
def MenuStd(Ruta, DataStd):
    while True:
        clear()
        print("\n","=" * 40)
        print("|{:^38}|".format("GESTIÓN DE ESTUDIANTES"))
        print("1-   Agregar Estudiante")
        print("2-   Modificar Estudiante")
        print("3-   Buscar Estudiante")
        print("4-   Eliminar Estudiante")
        print("5-   Regresar al Menú Principal")
        try:
            Opc = LeerEntero("\t>>Escoja una opción (1-5)? ")
            if Opc == 1:
                clear()
                DataStd = AddStudent(DataStd)
                UpdateFile(Ruta, DataStd)
            elif Opc == 2:
                clear()
                DataStd = ModifyStudent(DataStd)
                UpdateFile(Ruta, DataStd)
            elif Opc == 3:
                clear()
                SearchStudent(DataStd)
                UpdateFile(Ruta, DataStd)
            elif Opc == 4:
                clear()
                DataStd = DeleteStudent(DataStd)
                UpdateFile(Ruta, DataStd)
            elif Opc == 5:
                clear()
                return DataStd
            else:
                MsgNotify("Opción no valida")
        except ValueError:
            print("Error! Ingrese un tipo de dato valido")

#Función Mostrar SubMenú Informes Institución
def MenuInf(DataStd):
    while True:
        clear()
        print("\n","=" * 40)
        print("|{:^38}|".format("MENÚ DE INFORMES"))
        print("1-   Promedio Estudiantes por Curso")
        print("2-   Tabla Excelencia por Curso")
        print("3-   Tabla Excelencia de la Institución")
        print("4-   Regresar al Menú Principal")
        Opc = LeerEntero("\t>>Escoja una opción (1-4)? ")
        try:
            if Opc == 1:
                clear()
                PromEstCurso(DataStd)
            elif Opc == 2:
                clear()
                ExcelenciaCurso(DataStd)
            elif Opc == 3:
                clear()
                ExcelenciaInst(DataStd)
            elif Opc == 4:
                clear()
                return
            else:
                MsgNotify("Opción no valida")
        except ValueError:
            print("Error! Ingrese un tipo de dato valido")

#********************************** FUNCIONES GESTIÓN ESTUDIANTE***********************************
#Función para Agregar Nuevo Estudiante a la Institución Educativa
def AddStudent(DataStd):
    print("\n\f AGREGAR NUEVO ESTUDIANTE")
    Curso = LeerString("Ingrese Curso del Estudiante: ") 
    if not Curso in DataStd.keys():
        DataStd[Curso] = {}
    Id = LeerEntero("Ingrese ID del Estudiante: ")
    if Id in DataStd[Curso].keys():
        MsgNotify("ID OCUPADO")
    else:
        Name = LeerString("Nombre del Estudiante: ")
        Name = Name.strip()
        Gender = LeerSexo("Ingrese Genero del Estudiante (M/F): ")
        DataStd[Curso][Id] = {}
        DataStd[Curso][Id]["Name"]= Name
        DataStd[Curso][Id]["Gender"] = Gender
        DataStd[Curso][Id]["Notas"] = None
        DataStd[Curso][Id]["Promedio"] = 0
        MsgNotify("ESTUDIANTE AGREGADO EXITOSAMENTE")      
    return DataStd                                                

#Función para Modificar un Estudiante Existente en la Institución
def ModifyStudent(DataStd):
    print("\n\f MODIFICAR ESTUDIANTE")
    Id = LeerString("Ingrese ID del Estudiante: ")
    for i in DataStd.keys():
        if Id in DataStd[i].keys():
            while True:                                                         #SubMenú para Modificar
                print("\n","=" * 40)
                print(" DATO A MODIFICAR ")
                print("1- Nombre")                                                  
                print("2- Sexo")                                                    
                print("3- Curso")                                                   
                print("4- Regresar a Menú Principal")                                         
                try:
                    Opc = int(input("\t>>Escoja una opción (1-4)? "))       
                    if Opc > 0 or Opc < 5:
                        if Opc == 1:
                            DataStd[i][Id]["Name"] = LeerString("Ingrese nuevo nombre: ")
                            print("Nombre modificado correctamente")
                        if Opc == 2:
                            DataStd[i][Id]["Gender"] =  LeerString("Ingrese nuevo Genero: ")
                            print("Genero modificado correctamente")
                        if Opc == 3:
                            NewCurso = LeerString("Ingrese Nuevo Curso del Estudiante: ")
                            DataStd = ActualizarData(NewCurso, Id, i, DataStd)
                            print("Curso modificado correctamente")
                        if Opc == 4:
                            print("ESTUDIANTE MODIFICADO EXITOSAMENTE")
                            return DataStd
                    else:
                        MsgNotify("Opción no valida")
                        continue       
                except ValueError:
                    print("Error! Ingrese un numero entero valido")   
            else: 
                print("ESTUDIANTE NO REGISTRADO")     
    return DataStd                      

#Función para cambiar estudiante de Curso
def ActualizarData(NewCurso, Id, i, DataStd):
    DataStd[NewCurso][Id] = {}
    DataStd[NewCurso][Id]["Name"] =  DataStd[i][Id]["Name"]
    DataStd[NewCurso][Id]["Gender"] =  DataStd[i][Id]["Gender"]
    DataStd[NewCurso][Id]["Notas"] = DataStd[i][Id]["Notas"]
    DataStd[NewCurso][Id]["Promedio"] = DataStd[i][Id]["Promedio"] 
    DataStd[i].pop(Id)
    return DataStd

#Función para buscar la Info de un Estudiante, si existe
def SearchStudent(DataStd):
    print("\n\f BUSCAR ESTUDIANTE")
    Id = LeerString("Ingrese ID del Estudiante: ")
    for Curso in DataStd.keys():
        if Id in DataStd[Curso].keys():
            print(Id)                                 
            print("|{:<12}|{:<12}|{:<40}|{:<10}|{:<20}|{:>12}|".format("CURSO", "ID", "NOMBRE", "GENERO", "NOTAS", "PROMEDIO"))
            print("|{:<12}|{:<12}|{:<40}|{:<10}|{:<20}|{:>12.1f}|".format(Curso, Id, DataStd[Curso][Id]["Name"], DataStd[Curso][Id]["Gender"], str(DataStd[Curso][Id]["Notas"]), DataStd[Curso][Id]["Promedio"]))
            input("Presione cualquier tecla para continuar\n")
            return
    MsgNotify("ESTUDIANTE NO REGISTRADO")   
    return

#Función para eliminar un Estudiante, si existe
def DeleteStudent(DataStd):
    print("\n\f ELIMINAR ESTUDIANTE")
    Id = LeerString("Ingrese ID del Estudiante: ")
    for i in DataStd.keys():
        if Id in DataStd[i].keys():
            DataStd[i].pop(Id)
            MsgNotify("ESTUDIANTE ELIMINADO EXITOSAMENTE")
            return DataStd                                            
    MsgNotify("ESTUDIANTE NO REGISTRADO")
    return DataStd


#***************************** FUNCIONES INGRESO Y CALCULO DE NOTAS *******************************
#Función para Calificar a todos los estudiantes de un curso, ordenados en Orden Alfabetico
def CalificarStudent(DataStd):
    print("|{:^38}|".format("CALIFICACIÓN DE CURSO"))
    Curso = LeerString("Ingrese Curso a Calificar (0 para Regresar): ")
    if Curso == "0":
        return DataStd
    Values = []
    Values.extend(list(DataStd[Curso].values()))
    Values.sort(key=ReturnName)
    for i in range(0, len(Values)):
        print(Values[i]["Name"])
        Notas = LeerNotas()
        for Id in DataStd[Curso].keys():
            if Values[i]["Name"] == DataStd[Curso][Id]["Name"]:
                DataStd[Curso][Id]["Notas"] = Notas
                DataStd[Curso][Id]["Promedio"] = CalcularPromedio(Id, Curso, DataStd)
    return DataStd

#Función para Recibir las notas de un Estudiante
def LeerNotas():
    Cont = 1
    Notas = []
    while True:
        Nota = LeerNota(f"\tNota {Cont}: ")
        Notas.append(Nota)
        Cont += 1
        print("\t¿Agregar Otra Nota?")
        print("\t\t1- Sí")
        print("\t\t2- No")
        while True:
            try:
                Opc = int(input("\t>>Escoja una opción (1-2)? "))
                if Opc == 1 :
                    break
                elif Opc == 2:
                    return Notas
                else:
                    MsgNotify("Opción no valida")
                    continue
            except ValueError:
                print("Error! Ingrese un numero entero valido")

#Función para Calcular Promedio de un Estudiante
def CalcularPromedio(Id, Curso, DataStd):
    Suma = sum(DataStd[Curso][Id]["Notas"])
    Cant = len(DataStd[Curso][Id]["Notas"])
    Prom = Suma / Cant
    return Prom


#**************************** FUNCIONES PARA CREAR REPORTES E IMPRIMIR ****************************
#Función para listar Estudiantes en orden Alfabetico y mostrar su promedio
def PromEstCurso(DataStd):
    print("\n\f PROMEDIOS DE ESTUDIANTES POR CURSO")
    Curso = LeerString("Ingrese Curso a Calificar: ")
    Values = []
    Values.extend(list(DataStd[Curso].values()))
    Values.sort(key=ReturnName)
    print("|{:^50}|".format("PROMEDIOS CURSO: "+ Curso))
    print("|{:^40}|{:>10}|".format("ESTUDIANTE", "PROMEDIO"))
    print("+", "-" * 38, "+", "-" * 8, "+")
    for i in range(0, len(Values)):
        for Id in DataStd[Curso].keys():
            if Values[i]["Name"] == DataStd[Curso][Id]["Name"]:
                print("|{:<40}|{:>10.1f}|".format(Values[i]["Name"], DataStd[Curso][Id]["Promedio"]))
                print("+", "-" * 38, "+", "-" * 8, "+")
    MsgNotify("FIN DEL CURSO")
    return

#Función para Mostrar Tabla de Excelencia de un curso, ordenados de mayor a menor Promedio
def ExcelenciaCurso(DataStd):
    print("\n\f CUADRO DE HONOR POR CURSO")
    Curso = LeerString("Ingrese Curso a Obtener Tabla de Excelencia: ")
    Values = (list(DataStd[Curso].values()))
    Values.sort(key=ReturnProm, reverse = True)
    Puesto = 1
    print("|{:^56}|".format("CUADRO DE HONOR CURSO: "+ Curso))
    print("|{:^6}|{:^40}|{:^10}|".format("PUESTO", "ESTUDIANTE", "PROMEDIO"))
    print("+", "-" * 4, "+", "-" * 38, "+", "-" * 8, "+")  
    for i in range(0, len(Values)):
        if Puesto == 6:
            break
        for Id in DataStd[Curso].keys():
            if Values[i]["Name"] == DataStd[Curso][Id]["Name"]:
                print("|{:^6}|{:<40}|{:>10.1f}|".format(Puesto, Values[i]["Name"], DataStd[Curso][Id]["Promedio"]))
        Puesto += 1
    MsgNotify("")
    return

#Función para Mostrar Tabla de Excelencia de toda la Institución, 5 mejores promedios de todo ACME, en orden descendente
def ExcelenciaInst(DataStd):
    print("\n\f CUADRO DE HONOR DE LA INSTITUCIÓN ACME")
    Values = []
    for Curso in DataStd.keys():
        Values.extend(list(DataStd[Curso].values()))
    Values.sort(key=ReturnProm, reverse = True)
    Puesto = 1
    print("|{:^56}|".format("MEJORES 5 ESTUDIANTES DE LA INSTITUCIÓN ACME"))
    print("|{:^6}|{:^40}|{:^10}|{:^12}|".format("PUESTO", "ESTUDIANTE", "PROMEDIO", "CURSO"))
    print("+", "-" * 4, "+", "-" * 38, "+", "-" * 8, "+", "-" * 10, "+")
    for i in range(0, len(Values)):
        if Puesto == 6:
            break
        for Curso in DataStd.keys():
            for Id in DataStd[Curso].keys():
                if Values[i]["Name"] == DataStd[Curso][Id]["Name"]:
                    print("|{:^6}|{:<40}|{:>10.1f}|{:>12}|".format(Puesto, Values[i]["Name"], DataStd[Curso][Id]["Promedio"], Curso))
        Puesto += 1
    MsgNotify("")
    return

#Función para Retornar el promedio de la lista de datos de cada Estudiante
def ReturnProm(Values):
    return Values["Promedio"] 

#Función para Retornar el Nombre de la lista de datos de cada Estudiante
def ReturnName(Values):
    return Values["Name"] 

#****************************** FUNCIONES VALIDACIÓN Y NOTIFICACIÓN *******************************
#Función Mensaje Error -> Se utiliza para imprimir diferentes Notificaciones durante el proceso.
def MsgNotify(msg):
    print("\n NOTIFY!", msg)
    input(" -> Presione cualquier letra para regresar al Menú")
    print("=" * 45, "\n")

#Función Validar Entero -> Los datos numericos que se requieren deben ser todos Positivos y mayores que 0
def LeerEntero(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 0:
                MsgNotify("Error! Dato no valido")
                continue
            return n
        except ValueError:
            print("Error! Ingrese un numero Entero")

#Función para Validar una Nota entre 0.0 y 5.0
def LeerNota(msg):
    while True:
        try:
            n = float(input(msg))
            if n < 0.0 or n > 5.0:
                MsgNotify("Error! Nota no valido")
                continue
            return n
        except ValueError:
            print("Error! Ingrese un numero dentro del rango")


#Función Leer String -> Evita que se ingresen Nombres Vacios
def LeerString(msg):
    while True:
        try:
            Name = input(msg)
            Name = Name.strip()
            Name = Name.upper()
            if Name == "":
                MsgNotify("Error! Ingrese un nombre no Vacio")
                continue
            return Name
        except Exception as e:
            print("Error al ingresar el nombre.", e.message)

def LeerSexo(msg):
    while True:
        try:
            Name = input(msg)
            Name = Name.strip()
            Name = Name.upper()
            if Name == "M" or Name == "F":
                return Name
            MsgNotify("Error! Ingrese un Sexo valido")
            continue             
        except Exception as e:
            print("Error al ingresar el nombre.", e.message)

#Función para Cargar Archivo en Disco
def LoadFile(Ruta, Stud):
    with open(Ruta, "a+") as OpenFile:
        OpenFile.seek(0)
        try:
            Stud = json.load(OpenFile)
        except Exception as e:
            Stud = {}
    return Stud

#Función para Actualizar Archivo en Disco
def UpdateFile(Ruta, Std):
    with open(Ruta, "w") as ProductsFile:
        json.dump(Std, ProductsFile)

#Función para Limpiar consola
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


#***************************************** MAIN CODE *****************************************
StdData = {}
Ruta = "InstitutoACME\Instituto.json"
StdData = LoadFile(Ruta, StdData)
print("=" * 31)
print("  INSTITUTO ACME - BIENVENIDO ")
print("=" * 31)
while True:
    Opc = MainMenu()
    if Opc == 1:
        clear()
        StdData = MenuStd(Ruta, StdData)
    elif Opc == 2:
        clear()
        StdData = CalificarStudent(StdData)
        UpdateFile(Ruta, StdData)
    elif Opc == 3:
        clear()
        MenuInf(StdData)
    elif Opc == 4:
        clear()
        UpdateFile(Ruta, StdData)
        print("=" * 30)
        print("   INSTITUTO ACME - GRACIAS")
        print("=" * 30)
        break