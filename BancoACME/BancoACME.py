# INSTITUCIÓN BANCARIA ACME - Registro e Informe de Tarjeta de Credito
# Creado por: Diego Alejandro Mancilla Paipa

import json
import os

#***************************************** MENU Y SUBMENUS *****************************************
#Función Mostrar Menú Principal, con los submenús
def MainMenu():
    while True:
        clear()
        print("\n","=" * 40)
        print("******* INSTITUCIÓN BANCARIA ACME ******** ")
        print("     MENÚ PRINCIPAL")
        print("1-   Gestión de Tarjetas")
        print("2-   Informes Banco")
        print("3-   Salir")
        try:
            Opc = int(input("\t>>Escoja una opción (1-3)? "))
            if Opc < 0 or Opc > 3:                                      #Solo valido opciones entre 1 y 4
                MsgNotify("Opción no valida")
                continue
            else:
                return Opc
        except ValueError:
            print("Error! Ingrese un numero entero valido")

#Función Mostrar SubMenú Gestión de Tarjetas
def MenuCards(RtCards,DataCards):
    while True:
        UpdateFile(RtCards, DataCards)
        clear()
        print("\n","=" * 40)
        print("|{:^38}|".format("GESTIÓN DE TARJETAS"))
        print("1-   Agregar Nueva Tarjeta")
        print("2-   Modificar Tarjeta")
        print("3-   Eliminar Tarjeta")
        print("4-   Nuevo Reporte")
        print("5-   Borrar Reporte")
        print("6-   Regresar al Menú Principal")
        try:
            Opc = LeerEntero("\t>>Escoja una opción (1-6)? ")
            if Opc == 1:
                clear()
                DataCards = AddCard(DataCards)
            elif Opc == 2:
                clear()
                DataCards = ModifyCard(DataCards)
            elif Opc == 3:
                clear()
                DataCards = DeleteCard(DataCards)
            elif Opc == 4:
                clear()
                DataCards = NewReport(DataCards)
            elif Opc == 5:
                clear()
                DataCards = DeleteReport(DataCards)
            elif Opc == 6:
                clear()
                return DataCards
            else:
                MsgNotify("Opción no valida")
        except ValueError:
            print("Error! Ingrese un tipo de dato valido")

#Función Mostrar SubMenú Imprimir Reportes
def MenuInformes(DataCards):
    while True:
        clear()
        print("\n","=" * 40)
        print("|{:^38}|".format("MENÚ DE INFORMES ACME"))
        print("1-   Tarjetas de un Cliente")
        print("2-   Información de Tarjeta")
        print("3-   Listado de Tarjetas")
        print("4-   Listado de Clientes")
        print("5-   Cantidad de Tarjeta por Tipo")
        print("6-   Regresar al Menú Principal")
        try:
            Opc = LeerEntero("\t>>Escoja una opción (1-6)? ")
            if Opc == 1:
                clear()
                CardByClient(DataCards)
            elif Opc == 2:
                clear()
                InfoCard(DataCards)
            elif Opc == 3:
                clear()
                ListCards(DataCards)
            elif Opc == 4:
                clear()
                ListClients(DataCards)
            elif Opc == 5:
                clear()
                CardByType(DataCards)
            elif Opc == 6:
                clear()
                return
            else:
                MsgNotify("Opción no valida")
        except ValueError:
            print("Error! Ingrese un tipo de dato valido")     

#Función Mostrar SubMenú de Tipos de Tarjetas
def MenuType():
    Type_Cards = ("MasterCard", "Visa", "American Express")
    while True:
        print("\n","=" * 40)
        print("*** TIPO DE TARJETA ***")
        print("1-   MasterCard")
        print("2-   Visa")
        print("3-   American Express")
        try:
            Opc = int(input("\t>>Escoja una opción (1-3)? "))
            if Opc > 0 and Opc < 4:
                return Type_Cards[Opc - 1]
            MsgNotify("Opción no valida")
            continue
        except ValueError:
            print("Error! Ingrese un numero entero valido")

#Función para Ingresar Mes del Año
def MenuMes(msg):
    Meses = ("Enero", "Febrero" , "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    while True:
        Mes = 1
        for i in Meses:
            print(f"{Mes})\t{i}")
            Mes += 1
        try:
            Opc = LeerEntero("\t>>Escoja una opción (1-12)? ")
            if Opc > 0 and Opc < 13:
                return Meses[Opc - 1]
            else:
                MsgNotify("Opción no valida")
        except ValueError:
            print("Error! Ingrese un tipo de dato valido")

#********************************** FUNCIONES GESTIÓN TARJETAS***********************************
#Función para Añadir nueva tarjeta con todos sus datos correspondientes
def AddCard(Data):
    print("\n\fAGREGAR NUEVO TARJETA")
    NumCard = LeerString("Ingrese Numero de Tarjeta: ") 
    if not NumCard in Data["Cards"].keys():
        Data["Cards"][NumCard] = {}
    else:
        MsgNotify("TARJETA YA EXISTENTE")
        return Data
    Id = LeerEntero("Ingrese Cedula del Cliente: ")
    Id = str(Id)
    if Id in Data["Clientes"].keys():
        print("CLIENTE REGISTRADO")
        Data["Cards"][NumCard]["IdCliente"] = Id
    else:
        print("CLIENTE NO REGISTRADO")
        Data = RegistrarCliente(Id, Data)
    CardType = MenuType()
    MesVig = MenuMes("Ingrese Mes de Vigencia: ")
    YrVig = LeerYear("Ingrese Año de Vigencia: ")
    Clave = LeerClave("Ingrese Clave de Tarjeta: ")
    Data["Cards"][NumCard]["Type"] = CardType
    Data["Cards"][NumCard]["MesVig"] = MesVig
    Data["Cards"][NumCard]["YearVig"] = YrVig
    Data["Cards"][NumCard]["Clave"] = Clave
    Data["Cards"][NumCard]["Cliente"] = Id
    Data["Cards"][NumCard]["Reportes"] = []
    MsgNotify("TARJETA AGREGADA EXITOSAMENTE")      
    return Data

#Función para registrar cliente si no existe en la base de Datos
def RegistrarCliente(Id, Data):
    print("\n\fREGISTRO DE CLIENTE")
    Name = LeerString("Ingrese Nombre: ")
    Telefono = LeerString("Ingrese Numero de Telefono: ")
    Genero = LeerSexo("Ingrese Genero (M/F): ")
    Data["Clientes"][Id] = {}
    Data["Clientes"][Id]["Name"] = Name
    Data["Clientes"][Id]["Telefono"] = Telefono
    Data["Clientes"][Id]["Genero"] = Genero
    return Data

#Función para Modificar Tarjeta ya existente
def ModifyCard(Data):
    print("\n\fMODIFICAR TARJETA")
    NumCard = LeerString("Ingrese Numero de Tarjeta: ")
    if not NumCard in Data["Cards"].keys():
        MsgNotify("TARJETA NO EXISTENTE")
    else:                                                       #SubMenú para Modificar
        key = int(input("Ingrese Clave para confirmar: "))
        if key == Data["Cards"][NumCard]["Clave"]:
            while True:  
                print("\n","=" * 40)
                print(" DATO A MODIFICAR ")
                print("1- Tipo de Tarjeta")                                                  
                print("2- Mes de Vigencia")                                                    
                print("3- Año de Vigencia")
                print("4- Clave")                                                   
                print("5- Regresar a Menú Principal")                                   
                try:
                    Opc = int(input("\t>>Escoja una opción (1-5)? "))       
                    if Opc > 0 or Opc < 6:
                        if Opc == 1:
                            Data["Cards"][NumCard]["Type"] = MenuType()
                            print("Tipo de Tarjeta modificado correctamente")
                        elif Opc == 2:
                            Data["Cards"][NumCard]["MesVig"] =  MenuMes("Ingrese nuevo Mes de Vigencia: ")
                            print("Mes de Vigencia modificado correctamente")
                        elif Opc == 3:
                            Data["Cards"][NumCard]["MesVig"] =  LeerYear("Ingrese nuevo Año de Vigencia: ")
                            print("Año de Vigencia modificado correctamente")
                        elif Opc == 4:
                            Data["Cards"][NumCard]["Clave"] =  LeerClave("Ingrese nueva Clave: ")
                            print("Clave modificada correctamente")
                        elif Opc == 5:
                            print("TARJETA MODIFICADA EXITOSAMENTE")
                            return Data
                    else:
                        MsgNotify("Opción no valida")
                        continue       
                except ValueError:
                    print("Error! Ingrese un numero entero valido")
        else:
            MsgNotify("CLAVE INCORRECTA")
            return Data  

#Función para Eliminar Tarjeta
def DeleteCard(Data):
    print("\n\fELIMINAR TARJETA")
    NumCard = LeerString("Ingrese Numero de Tarjeta: ")
    if not NumCard in Data["Cards"].keys():
        MsgNotify("TARJETA NO EXISTENTE")
    else:                                                       #SubMenú para Modificar
        Id = Data["Cards"][NumCard]["Cliente"]
        key = int(input("Ingrese Clave para confirmar: "))
        if key == Data["Cards"][NumCard]["Clave"]:
            Data["Cards"].pop(NumCard)
            MsgNotify("TARJETA ELIMINADA EXITOSAMENTE")
            Cont = 0
            for Card in Data["Cards"].keys():
                if Id == Data["Cards"][Card]["Cliente"]:
                    Cont += 1
            if not Cont > 0:
                Data["Clientes"].pop(Id)
        else:
            MsgNotify("CLAVE INCORRECTA")
        return Data                                          

#Función para Crear nuevo reporte de Tarjeta
def NewReport(Data):
    print("\n\fELIMINAR TARJETA")
    NumCard = LeerString("Ingrese Numero de Tarjeta: ")
    if not NumCard in Data["Cards"].keys():
        MsgNotify("TARJETA NO REGISTRADA")
    else:                            
        Report = LeerString("Ingrese Nuevo reporte: ")
        Data["Cards"][NumCard]["Reportes"].append(Report)
        MsgNotify("REPORTE REALIZADO")
    return Data

#Función para Eliminar reporte de Tarjeta
def DeleteReport(Data):
    print("\n\fELIMINAR TARJETA")
    NumCard = LeerString("Ingrese Numero de Tarjeta: ")
    if not NumCard in Data["Cards"].keys():
        MsgNotify("TARJETA NO REGISTRADA")
    else:  
        LstRepo = Data["Cards"][NumCard]["Reportes"]
        if len(LstRepo) == 0:
            MsgNotify("TARJETA NO CONTIENE REPORTES")
        else:
            print(f"LISTA DE REPORTES - TARJETA No. {NumCard}")           
            for i in range(0, len(LstRepo)):
                print(f"\t{i+1}) {LstRepo[i]}")
            Select = int(input("Numero de Reporte a borrar: "))
            while True:
                if Select > 0 and Select <= len(LstRepo):
                    LstRepo.pop(Select-1)
                    Data["Cards"][NumCard]["Reportes"] = LstRepo
                    MsgNotify("REPORTE BORRADO")
                    return Data
                else:
                    print("No. de reporte no valido")
                    continue
    return Data

#**************************** FUNCIONES PARA CREAR REPORTES E IMPRIMIR ****************************
#Función para imprimir Tarjetas que tenga un cliente ingresado
def CardByClient(Data):
    print("\n\fINFORMACIÓN TARJETAS DE CLIENTE")
    Id = LeerString("Ingrese Numero de Cedula: ")
    if not Id in Data["Clientes"].keys():
         MsgNotify("CLIENTE NO EXISTENTE")
    else:
        print("\n|{:^59}|".format("LISTADO DE TARJETAS DEL CLIENTE"))
        print("+", "-" * 57, "+")
        print("|{:<7}: {:<50}|".format("CEDULA", Id))
        print("|{:<7}: {:<50}|".format("NOMBRE", Data["Clientes"][Id]["Name"]))
        print("+", "-" * 5, "+")
        print("|{:^16}|{:^7}|{:^18}|{:^15}|".format("No TARJETA", "CLAVE", "TIPO TARJETA", "FECHA VENC."))
        print("+", "-" * 14, "+", "-----", "+", "-" * 16, "+", "-" * 13, "+")
        for Card in Data["Cards"].keys():
            if Id == Data["Cards"][Card]["Cliente"]:
                print("|{:<16}|{:^7}|{:^18}|{:>10}/{:<4}|".format(Card, Data["Cards"][Card]["Clave"], Data["Cards"][Card]["Type"], Data["Cards"][Card]["MesVig"], Data["Cards"][Card]["YearVig"]))
                print("+", "-" * 14, "+", "-----", "+", "-" * 16, "+", "-" * 13, "+")
        MsgNotify("\nLISTADO FINALIZADO")
    return

#Función para imprimir Informacion de un numero de tarjeta Ingresado
def InfoCard(Data):
    print("\n\fINFORMACIÓN DE TARJETA")
    NumCard = LeerString("Ingrese Numero de Tarjeta: ")
    if not NumCard in Data["Cards"].keys():
        MsgNotify("TARJETA NO EXISTENTE")
    else:
        print(f"\nTARJETA No. {NumCard}")
        print("\tTipo de Tarjeta: {}".format(Data["Cards"][NumCard]["Type"]))
        print("\tMes/Año de Vigencia: {}/{}".format(Data["Cards"][NumCard]["MesVig"], Data["Cards"][NumCard]["YearVig"]))
        print("\tClave: {}".format(Data["Cards"][NumCard]["Clave"]))
        print("\tTitular de Tarjeta:")
        Id = Data["Cards"][NumCard]["Cliente"]
        print("\t\tCedula: {}".format(Id))
        print("\t\tNombre: {}".format(Data["Clientes"][Id]["Name"]))
        print("\t\tTelefono: {}".format(Data["Clientes"][Id]["Telefono"]))
        print("\t\tGenero: {}".format(Data["Clientes"][Id]["Genero"]))
        print("\tReportes de Tarjeta:")
        LstRepo = Data["Cards"][NumCard]["Reportes"]
        if len(LstRepo) == 0:
            print("\t\tNo hay reportes para mostrar")
        else:       
            for i in range(0, len(LstRepo)):
                print(f"\t\t{i+1}) {LstRepo[i]}")
        MsgNotify("INFORMACIÓN FINALIZADA")
    return

#Función para Listar todas las tarjetas del banco
def ListCards(Data):
    print("|{:^106}|".format("TARJETAS REGISTRADAS"))
    print("+","-" * 104, "+")
    print("|{:^14}|{:^17}|{:^16}|{:^16}|{:^40}|".format("No. TARJETA", " FECHA VENC.", "TIPO TARJETA", "CEDULA TITULAR", "TITULAR"))
    for Card in Data["Cards"].keys():
        Id = Data["Cards"][Card]["Cliente"]
        print("|{:^14}|{:>1}{:>10}/{:<5}|{:<16}|{:<16}|{:<40}|".format(Card, " ", Data["Cards"][Card]["MesVig"], Data["Cards"][Card]["YearVig"], Data["Cards"][Card]["Type"], Id, Data["Clientes"][Id]["Name"]))
    print("+","-" * 104, "+")
    MsgNotify("FIN DEL LISTADO")
    return

#Función para Listar todos los clientes del banco
def ListClients(Data):
    print("|{:^72}|".format("CLIENTES REGISTRADOS"))
    print("+","-" * 70, "+")
    print("|{:^14}|{:^40}|{:^16}|".format("CEDULA", "NOMBRE", "TELEFONO"))
    for Cliente in Data["Clientes"].keys():
        print("|{:<14}|{:<40}|{:^16}|".format(Cliente, Data["Clientes"][Cliente]["Name"], Data["Clientes"][Cliente]["Telefono"]))
    print("+","-" * 70, "+")
    MsgNotify("FIN LISTADO DE CLIENTES")
    return

#Función para Imprimir cantidad de tarjetas por Tipo
def CardByType(Data):
    print("CANTIDAD DE TARJETAS REGISTRADAS")
    Visa = 0
    American = 0
    Master = 0
    for Card in Data["Cards"].keys():
        if Data["Cards"][Card]["Type"] == "Visa":   
            Visa += 1
        elif Data["Cards"][Card]["Type"] == "American Express": 
            American += 1
        elif Data["Cards"][Card]["Type"] == "MasterCard": 
            Master += 1 
    print(f"Visa: {Visa}")
    print(f"American Express: {American}")
    print(f"MasterCard: {Master}")
    MsgNotify("FINAL DE CUENTA")

#****************************** FUNCIONES VALIDACIÓN Y NOTIFICACIÓN *******************************
#Función Mensaje Error -> Se utiliza para imprimir diferentes Notificaciones durante el proceso.
def MsgNotify(msg):
    print("\n", msg)
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

#Función para validar Clave entre 100 y 999
def LeerClave(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 100 and n > 999:
                MsgNotify("CLAVE NO VALIDA")
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

#Función para leer Año  (Mayor a 2023)
def LeerYear(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 2023:
                MsgNotify("AÑO DE VIGENCIA NO VALIDO")
                continue
            return n
        except ValueError:
            print("Error! Ingrese un numero Entero")

#Función para Leer Genero del cliente(Solo M o F)
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
def LoadFile(Ruta):
    with open(Ruta, "a+") as OpenFile:
        OpenFile.seek(0)
        try:
            Data = json.load(OpenFile)
        except Exception as e:
            Data = {}
            Data["Cards"] = {}
            Data["Clientes"] = {}
    return Data

#Función para Actualizar Archivo en Disco
def UpdateFile(Ruta, Data):
    with open(Ruta, "w") as OpenFile:
        json.dump(Data, OpenFile)

#Función para Limpiar consola
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#***************************************** MAIN CODE *****************************************
CardsData = {}
RutaCards = "CardData.json"
CardsData = LoadFile(RutaCards)
print("=" * 44)
print("  INSTITUCIÓN BANCARIA ACME - BIENVENIDO ")
print("=" * 44)
while True:
    Opc = MainMenu()
    if Opc == 1:
        clear()
        CardsData = MenuCards(RutaCards,CardsData)
        UpdateFile(RutaCards, CardsData)
    elif Opc == 2:
        clear()
        MenuInformes(CardsData)
    elif Opc == 3:
        clear()
        UpdateFile(RutaCards, CardsData)
        print("=" * 39)
        print("  INSTITUCIÓN BANCARIA ACME - GRACIAS")
        print("=" * 39)
        break