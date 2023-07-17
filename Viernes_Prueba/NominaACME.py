# NOMINA DE EMPRESA ACME
# El programa almacena todos los datos de los empleados en un Diccionario
# Para hacer cualquier operación del menú que requiera un empleado, el programa solicita el codigo y entra 
# a la función correspondiente para buscar en Diccionario al empleado y hacer el proceso debido.

#Función Leer String -> Evita que se ingresen Nombres Vacios
def LeerString(msg):
    while True:
        try:
            Name = input(msg)
            if Name.strip() == "":
                MsgNotify("Error! Ingrese un nombre no Vacio")
                continue
            return Name
        except Exception as e:
            print("Error al ingresar el nombre.", e.message)

#Función Mensaje Error -> Se utiliza para imprimir diferentes Notificaciones durante el proceso.
def MsgNotify(msg):
    print("\n NOTIFY!", msg)
    input(" -> Presione cualquier letra para regresar al Menú")
    print("=" * 45)

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
            print("Error! Ingrese un numero de codigo valido")

#Función Validar Valor Hora -> Valido el valor de la hora dentro del rango solicitado
def LeerValor(msg): 
    while True:
        try:
            n = float(input(msg))
            if n < 8000 or n > 150000:                                  #Rango de tarifa de hora (8.000 - 150.000)
                MsgNotify("Error! Dato no valido")
                continue
            return n
        except ValueError:
            print("Error! Ingrese un numero de codigo valido")

#Funcion Menú -> Menú principal para navegar por el programa (8 Opciones)
def MainMenu():
    while True:
        print("\n","=" * 40)
        print("*** NOMINA ACME *** ")
        print("      MENÚ ")
        print("1- Agregar Empleado")
        print("2- Modificar Empleado")
        print("3- Buscar Empleado")
        print("4- Eliminar Empleados")
        print("5- Listar Empleados")
        print("6- Listar nómina de un empleado")
        print("7- Listar nómina de todos los epleados")
        print("8- Salir")
        try:
            Opc = int(input("\t>>Escoja una opción (1-8)? "))
            if Opc < 0 or Opc > 8:                                      #Solo valido opciones entre 1 y 8
                MsgNotify("Opción no valida")
                continue
            else:
                return Opc
        except ValueError:
            print("Error! Ingrese un numero entero valido")

#Función para Agregar un nuevo empleado -> Solicita los datos, los adiciona a un Diccionario con clave el ID
def AgregarEmpleado(Dicc):
    print("\n\f AGREGAR NUEVO EMPLEADO")
    Id = LeerEntero("Ingrese ID del Empleado: ")
    if Id in Dicc:
        MsgNotify("ID OCUPADO")
    else:
        Name = LeerString("Nombre del Empleado: ")
        Name = Name.strip()
        Horas = LeerEntero("Ingrese Horas trabajadas del Empleado: ")
        ValorHora = LeerValor("Ingrese Valor de la hora del Empleado: ")
        Dicc[Id] = {}
        Dicc[Id]["Nombre"] = Name
        Dicc[Id]["Hours"] = Horas
        Dicc[Id]["Value"] = ValorHora    
        MsgNotify("EMPLEADO AGREGADO EXITOSAMENTE")
    return Dicc                                                   #Retorna una lista con los datos del nuevo empleado

#Función para Modificar un nuevo empleado -> Modifica los datos del Diccionario con clave ID
def ModificarEmpleado(ID, Dicc):
    print("\n\f MODIFICAR EMPLEADO")
    while True:                                                         #SubMenú para Modificar
        print("\n","=" * 40)
        print(" DATO A MODIFICAR ")
        print("1- Nombre")                                              #1 Modificar el Nombre
        print("2- Horas Trabajadas")                                    #2 Modificar las Horas trabajadas
        print("3- Valor Hora")                                          #3 Modificar Valor de la hora
        print("4- Return Menu")                                         #4 Volver al Menú principal
        try:
            Opc = int(input("\t>>Escoja una opción (1-4)? "))           
            if ID in Dicc:
                if Opc > 0 or Opc < 5:
                    if Opc == 1:
                        Name = LeerString("Ingrese nuevo nombre: ")
                        Dicc[ID]["Nombre"] = Name
                        print("Nombre modificado correctamente")
                    if Opc == 2:
                        Hora = LeerString("Ingrese nuevo numero de Horas trabajadas: ")
                        Dicc[ID]["Hours"] = Hora
                        print("Horas trabajadas modificado correctamente")
                    if Opc == 3:
                        Valor = LeerString("Ingrese nuevo valor de Hora: ")
                        Dicc[ID]["Value"] = Valor
                        print("Valor de la Hora modificado correctamente")
                    if Opc == 4:
                        print("EMPLEADO MODIFICADO EXITOSAMENTE")
                        break
                else:
                    MsgNotify("Opción no valida")
                    continue       
            else:
                MsgNotify("EMPLEADO NO REGISTRADO")
                break
        except ValueError:
            print("Error! Ingrese un numero entero valido")        
    return Dicc                                                     #Retorna el Diccionario de empleados modificado

#Función para buscar la Info de un empleado -> Busca si el codigo existe, saca los datos del empleado a una lista y los imprime
def BuscarEmpleado(ID, Dicc):
    print("\n\f BUSCAR EMPLEADO")
    if ID in Dicc:                                                  #Si el empleado existe, imprime los datos
        print("|{:<12}|{:<18}|{:>12}|{:>12}|".format("ID", "NOMBRE", "HORAS", "VALOR"))
        print("|{:<12}|{:<18}|{:>12}|{:>12,}|".format(ID, Dicc[ID]["Nombre"], Dicc[ID]["Hours"], Dicc[ID]["Value"]))
        input("Presione cualquier tecla para continuar")
    else:
        MsgNotify("EMPLEADO NO REGISTRADO")   
    return

#Función para eliminar un empleado -> Busca el ID en la lista completa de empleados, modifica la lista y retorna la nueva lista.
def EliminarEmpleado(ID, Dicc):
    print("\n\f ELIMINAR EMPLEADO")
    if ID in Dicc:
        Dicc.pop(ID)
        MsgNotify("EMPLEADO ELIMINADO EXITOSAMENTE")
        return Dicc                                              #Retorna una nueva lista de empleados
    MsgNotify("EMPLEADO NO REGISTRADO")

#Función para Listar los empleados de 5 en 5 -> Recorro la lista de empleados e imprime los datos en el orden preestablecido
def ListarEmpleados(Dicc):
    Opc = 0
    Cont = 1
    print("*" * 14, "LISTADO DE EMPLEADOS - ACME", "*" * 14)
    print("|{:<10}|{:<18}|{:>12}|{:>12}|".format("ID", "NOMBRE", "HORAS", "VALOR"))
    for ID in Dicc.keys():
        print("|{:<10}|{:<18}|{:>12}|{:>12,}|".format(ID, Dicc[ID]["Nombre"], Dicc[ID]["Hours"], Dicc[ID]["Value"]))
        print("+----------+------------------+------------+------------+")
        if Cont > 0 and Cont % 5 == 0:                                        #Cada 5 impresiones, pregunta si desea continuar
            while True:
                print("-" * 40)                                         #SubMenú para continuar listado
                print("¿Continuar Listado?")
                print("1- Sí")
                print("2- No")
                try:
                    Opc = int(input("\t>>Escoja una opción (1-2)? "))
                    if Opc == 1 or Opc == 2:
                        break
                    else:
                        MsgNotify("Opción no valida")
                    continue
                except ValueError:
                    print("Error! Ingrese un numero entero valido")    
        if Opc == 2:                                                    #Si eligió Opción 2, retorna al Menú principal
            return
        Cont += 1
    input("Presione cualquier tecla para volver al Menú principal")

#Función para calcular la nomina de un empleado -> Busca los datos de Horas y el Precio del empleado, luego calcula la nomina y añado datos al Diccionario
def NominaEmpleado(ID, Dicc):
    if ID in Dicc:
        SueldoBruto = Dicc[ID]["Hours"] * Dicc[ID]["Value"]
        DescPension = SueldoBruto * 0.04
        DescEps = SueldoBruto * 0.04
        if SueldoBruto < 1160000:
            SubTrans = 140606
        else:
            SubTrans = 0
        SueldoNeto = SueldoBruto + SubTrans - DescEps - DescPension
        Dicc[ID]["Bruto"] = SueldoBruto
        Dicc[ID]["Aux"] = SubTrans
        Dicc[ID]["EPS"] = DescEps * (-1)
        Dicc[ID]["Pension"] =  DescPension * (-1)
        Dicc[ID]["Neto"] = SueldoNeto
    else:
        MsgNotify("EMPLEADO NO REGISTRADO")     
    return Dicc

#Función para listar la nomina de todos los empleados de 5 en 5 -> Imprimo Datos de la nómina de cada empleado, en formato tabla
def ListarNominaTotal(Dicc):
    Opc = 0
    Cont = 1
    print("*" * 33, "NOMINA COMPLETA - ACME", "*" * 32)
    print("|{:<10}|{:<18}|{:>12}|{:>12}|{:>12}|{:>18}|".format("ID", "SUELDO BRUTO", "AUX. TRANS", "EPS", "PENSIÓN", "SUELDO NETO"))
    for ID in Dicc.keys():
        Dicc = NominaEmpleado(ID, Dicc)
        print("|{:<10}|{:<18,}|{:>12,}|{:>12,}|{:>12,}|{:>18,}|".format(ID, Dicc[ID]["Bruto"], Dicc[ID]["Aux"], Dicc[ID]["EPS"], Dicc[ID]["Pension"], Dicc[ID]["Neto"]))
        print("+----------+------------------+------------+------------+------------+------------------+")
        if Cont > 0 and Cont % 5 == 0:                                        #Cada 5 impresiones, pregunta si desea continuar
            while True:
                print("-" * 40)                                         #SubMenú para continuar listado
                print("¿Continuar Listado?")
                print("1- Sí")
                print("2- No")
                try:
                    Opc = int(input("\t>>Escoja una opción (1-2)? "))
                    if Opc == 1 or Opc == 2:
                        break
                    else:
                        MsgNotify("Opción no valida")
                    continue
                except ValueError:
                    print("Error! Ingrese un numero entero valido") 
        if Opc ==2:
            return
        Cont += 1
    input("Presione cualquier tecla para volver al Menú principal")

#Main Code
DatosEmpleados = {}
while True:
    Opc = MainMenu()
    if Opc == 1:
        DatosEmpleados = AgregarEmpleado(DatosEmpleados)
    elif Opc == 2:
        ID = LeerEntero("Ingrese ID del empleado a modificar: ")
        DatosEmpleados = ModificarEmpleado(ID, DatosEmpleados)
    elif Opc == 3:
        ID = LeerEntero("Ingrese ID del empleado a buscar: ")
        BuscarEmpleado(ID, DatosEmpleados)
    elif Opc == 4:
        ID = LeerEntero("Ingrese ID del empleado a Eliminar: ")
        DatosEmpleados = EliminarEmpleado(ID, DatosEmpleados)
    elif Opc == 5:
        ListarEmpleados(DatosEmpleados)
    elif Opc == 6:
        ID = LeerEntero("Ingrese ID del empleado a buscar nómina: ")
        DatosEmpleados = NominaEmpleado(ID, DatosEmpleados)
        print("*" * 36, "NOMINA EMPLEADO", "*" * 36)
        print("|{:<10}|{:<18}|{:>12}|{:>12}|{:>12}|{:>18}|".format("ID", "SUELDO BRUTO", "AUX. TRANS", "EPS", "PENSIÓN", "SUELDO NETO"))
        print("|{:<10}|{:<18,}|{:>12,}|{:>12,}|{:>12,}|{:>18,}".format(ID, DatosEmpleados[ID]["Bruto"], DatosEmpleados[ID]["Aux"], DatosEmpleados[ID]["EPS"], DatosEmpleados[ID]["Pension"], DatosEmpleados[ID]["Neto"]))
        input(" -> Presione cualquier letra para regresar al Menú")
    elif Opc == 7:
        ListarNominaTotal(DatosEmpleados)
    elif Opc == 8:
        print("-" * 33)
        print("GRACIAS POR USAR ESTE MENÚ - ACME")
        print("-" * 33)
        break