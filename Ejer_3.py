import os

def MainMenu():
    while True:
        clear()
        print()
        print("*" * 12, "MENÚ PRINCIPAL", "*" * 12)
        print("\t1-   Nuevo Registro")
        print("\t2-   Eliminar Registro")
        print("\t3-   Mostrar Listado total")
        print("\t4-   Buscar y mostrar Registro")
        print("\t5-   Actualizar Registro")
        print("\t6-   Salir del Programa")
        try:
            Opc =   LeerEntero("\t>>Escoja una opción (1-6)? ")
            if Opc > 0 and Opc < 6:                                      #Solo valido opciones entre 1 y 5
                Switch = {1: IngresarDatos, 2: EliminarRegistro, 3: MostrarListado, 4: BuscarRegistro, 5: ModifyRegistro}
                Switch[Opc]()
            elif Opc == 6:
                break
            else:
                MsgNotify("Opción no valida")
                continue
        except ValueError:
            print("Error! Ingrese un numero entero valido")

#Función para Ingresar nuevo Dato
def IngresarDatos():
    clear()
    print("NUEVO REGISTRO")
    Documento = LeerEntero("Ingrese Numero de Documento: ")
    for i in range(len(Empleados)):
        if Empleados[i]["NumDoc"] == Documento:
            MsgNotify("Documento ya registrado")
            return
    Name = LeerString("Nombre del Empleado: ")
    Edad = LeerEntero("Ingrese Edad: ")
    eps = LeerString("Ingrese EPS: ")
    Dicc = {}
    Dicc["NumDoc"] = Documento
    Dicc["Nombre"] = Name
    Dicc["Edad"] = Edad
    Dicc["EPS"] = eps
    Empleados.append(Dicc)
    MsgNotify("Registro Creado exitosamente")
    return

#Función para Eliminar Registro Existente
def EliminarRegistro():
    clear()
    print("ELIMINAR REGISTRO")
    Documento = LeerEntero("Ingrese Numero de Documento: ")
    for i in range(len(Empleados)):
        if Empleados[i]["NumDoc"] == Documento:
            Elim = Empleados.pop(i)
            print("Se ha eliminado el siguiente Registro")
            print("|{:^15}|{:^15}|{:^6}|{:^20}|".format("DOCUMENTO", "NOMBRE", "EDAD", "EPS"))
            print("|{:<15}|{:<15}|{:^6}|{:^20}|".format(Elim["NumDoc"], Elim["Nombre"], Elim["Edad"], Elim["EPS"]))
            MsgNotify("Registro Eliminado exitosamente")
            return

#Función para Listar Registro
def MostrarListado():
    clear()
    print("|{:^15}|{:^15}|{:^6}|{:^20}|".format("DOCUMENTO", "NOMBRE", "EDAD", "EPS"))
    print("+", "-" * 13, "+", "-" * 13, "+", "-" * 4, "+", "-" * 18, "+")
    for Emp in Empleados:
        print("|{:<15}|{:<15}|{:^6}|{:^20}|".format(Emp["NumDoc"], Emp["Nombre"], Emp["Edad"], Emp["EPS"]))
    print("=" * 61)
    MsgNotify("Fin del Registro")
    return

#Función para Buscar un registro
def BuscarRegistro():
    clear()
    print("BUSCAR REGISTRO")
    Documento = LeerEntero("Ingrese Numero de Documento: ")
    for Emp in Empleados:
        if Emp["NumDoc"] == Documento:
            print("|{:^15}|{:^15}|{:^6}|{:^20}|".format("DOCUMENTO", "NOMBRE", "EDAD", "EPS"))
            print("+", "-" * 13, "+", "-" * 13, "+", "-" * 4, "+", "-" * 18, "+")
            print("|{:<15}|{:<15}|{:^6}|{:^20}|".format(Emp["NumDoc"], Emp["Nombre"], Emp["Edad"], Emp["EPS"]))
            MsgNotify("Empleado encontrado exitosamente")
            return
    MsgNotify("Empleado no Registrado")
    return

#FUnción para modificar un Registro
def ModifyRegistro():
    clear()
    print("MODIFICAR REGISTRO")
    Documento = LeerEntero("Ingrese Numero de Documento: ")
    for i in range(len(Empleados)):
        if Empleados[i]["NumDoc"] == Documento:
            print("\t1-   Nombre")
            print("\t2-   Edad")
            print("\t3-   EPS")
            print("\t4-   Regresar")
            Opc =   LeerEntero("\t>>Escoja una opción (1-4)? ")
            if Opc == 1:
                NewName = LeerString("Nombre del Empleado: ")
                Empleados[i]["Nombre"] == NewName
            elif Opc == 1:
                NewEdad = LeerString("Nombre del Empleado: ")
                Empleados[i]["Edad"] == NewEdad
            elif Opc == 3:
                NewEPS = LeerString("Nombre del Empleado: ")
                Empleados[i]["EPS"] == NewEPS
        return            
    MsgNotify("Empleado no Registrado")
    return

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

#Función para Limpiar consola
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def poblarIniciales(empleados):
    empleados.append({
        "NumDoc": 1,
        "Nombre": "Howard",
        "Edad": 25,
        "EPS": "Sura"
    })

    empleados.append({
        "NumDoc": 2,
        "Nombre": "Nahomi",
        "Edad": 33,
        "EPS": "Solsalud"
    })
    empleados.append({
        "NumDoc": 3,
        "Nombre": "Sarita",
        "Edad": 21,
        "EPS": "SinergiaSalud"
    })
    empleados.append({
        "NumDoc": 4,
        "Nombre": "Juliana",
        "Edad": 17,
        "EPS": "La EPS de SUBIDA"
    })

Empleados = []
poblarIniciales(Empleados)
MainMenu()