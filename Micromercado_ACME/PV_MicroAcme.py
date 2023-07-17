#MICROMERCADO ACME
# Punto de Venta para el Micromercado ACME con capacidad para gestionar productos y registrar ventas.
# Todos los productos quedan registrados en un Archivo y pueden ser modificados o eliminados según criterio de Gerencia.
# Todas las ventas quedan registradas en un Archivo, unico para cada día. Ventas pueden ser moficadas o elimindas por si se cometen 
# errores humanos al momento de registrarlas o si se tiene algún problema con el cliente.
# Cada día el Sistema crea un nuevo Archivo en blanco para registrar todas las ventas diarias.
# El sistema cuenta con un apartado de Detalle donde se muestra en consola las ventas totales del Día detalladas.
# Si el sistema se cierra inesperadamente sin finalizar el día, se posee la capacidad de recuperar los datos hasta el breakpoint.
# El sistema debe ser lo más intuitivo para facilitar la labor al Cajero al momento de usarlo.

import json
from datetime import date

#Función Mostrar Menú Principal, con los submenús
def MainMenu():
    while True:
        print("\n","=" * 40)
        print("*** MICROMERCADO ACME *** ")
        print("      MENÚ PRINCIPAL")
        print("1-   Ventas")
        print("2-   Productos")
        print("3-   Detalle")
        print("4-   Cerrar Caja")
        try:
            Opc = int(input("\t>>Escoja una opción (1-4)? "))
            if Opc < 0 or Opc > 4:                                      #Solo valido opciones entre 1 y 4
                MsgNotify("Opción no valida")
                continue
            else:
                return Opc
        except ValueError:
            print("Error! Ingrese un numero entero valido")

#******************************* FUNCIONES APARTADO DE VENTAS ********************************
#Función Mostrar SubMenú de Ventas
def SalesMenu(Sales, Products):
    while True:
        print("\n","=" * 40)
        print("*** SUBMENÚ DE VENTAS *** ")
        print("1-   Nueva Venta")
        print("2-   Modificar Venta")
        print("3-   Eliminar Venta")
        print("4-   Regresar a Menú Principal")
        try:
            Opc = int(input("\t>>Escoja una opción (1-4)? "))
            if Opc == 1:
                Sales = NuevaVenta(Sales)
                TirillaPago()
            if Opc == 2:
                Sales = ModificarVenta(Sales)
                TirillaPago()
            if Opc == 3:
                Sales = ElminarVenta(Sales)
            if Opc == 4:
                UpdateProducts(Products)
                return Sales
        except ValueError:
            print("Error! Ingrese un numero entero valido")

#Función para Registrar nueva venta a cliente
def NuevaVenta(Sales, Products):
    IDCliente = LeerString("Identificación del Cliente: ")
    if not IDCliente in Sales:
        Sales[IDCliente] = {}
    Cod = LeerString("Producto Comprado (0 - Finalizar Compra): ")
    if Cod != "0":
        Sales[IDCliente][Cod] = {}
        Cant = LeerEntero("Cantidad Comprada: ")
        Sales[IDCliente][Cod]["Cant"] = Cant
    else:
        Sales = CalcularVenta(IDCliente, Sales, Products)
        return Sales

#Función para Modificar venta registrada (Error Humano al ingresar dato)
def ModificarVenta(Sales):
    IDCliente = LeerString("Identificación del Cliente: ")
    if IDCliente in Sales:
        Cod = LeerString("Producto a Modificar: ")
        if Cod in Sales[IDCliente]:
            New_Cod = LeerString("Nuevo Codigo: ")
            Cant = LeerString("Leer Cantidad: ")
            if Cant == 0:
                Sales[IDCliente].pop(Cod)
                MsgNotify("VENTA MODIFICADA EXITOSAMENTE")
                return Sales
            Sales[IDCliente][New_Cod] = Cant
            MsgNotify("VENTA MODIFICADA EXITOSAMENTE")
            return Sales
        else:
            MsgNotify("Producto no registrado en Factura")
    else:
        MsgNotify("VENTA NO REGISTRADA")
    return Sales

#Función para Eliminar venta registrada (Problemas con el cliente)
def EliminarVenta(Sales):
    IDCliente = LeerString("Identificación del Cliente: ")
    if IDCliente in Sales:
        Sales.pop(IDCliente)
        MsgNotify("VENTA ELIMINADA EXITOSAMENTE")

#Función para Calcular valores de Venta
def CalcularVenta(Cliente, Sales, Products):
    TotalPagar = 0
    for Cod in Sales[Cliente].keys():
        Sales[Cliente][Cod]["VlrProd"] = Sales[Cliente][Cod]["Cant"] * Products[Cod]["VlrUni"]
        sales[Cliente][Cod]["VlrIVA"] = Sales[Cliente][Cod]["VlrProd"] * Products[Cod]["IVA"]
        Sales[Cliente][Cod]["VlrTotal"] = Sales[Cliente][Cod]["VlrProd"] + sales[Cliente][Cod]["VlrIVA"]
        TotalPagar += Sales[Cliente]["VlrTotal"]
    Sales[Cliente]["TotalPagar"] = TotalPagar
    return Sales

#Función para Imprimir Tirilla de Pago
def TirillaPago(Sales):
    pas

#******************************** FUNCIONES APARTADO DE PRODUCTOS ********************************
#Función Mostrar SubMenú de Productos
def ProductsMenu(Products):
    while True:
        print("\n","=" * 40)
        print("*** SUBMENÚ DE PRODUCTOS *** ")
        print("1-   Agregar Producto")
        print("2-   Modificar Producto")
        print("3-   Eliminar Producto")
        print("4-   Regresar a Menú Principal")
        try:
            Opc = int(input("\t>>Escoja una opción (1-4)? "))
            if Opc == 1:
                Products = AgregarProducto(Products)
            if Opc == 2:
                Products = ModificarProducto(Products)
            if Opc == 3:
                Products = EliminarEmpleado(Products)
            if Opc == 4:
                UpdateProducts(Products)
                return Products
        except ValueError:
            print("Error! Ingrese un numero entero valido")

#Función para Agregar un nuevo Producto
def AgregarProducto(Products):
    print("\n","=" * 40)
    print("\n\f AGREGAR PRODUCTO")
    Cod = LeerString("Ingrese codigo del Producto")
    if Cod in Products:
        MsgNotify("CODIGO OCUPADO")
    else:
        Name = LeerString("Nombre del Producto: ")
        VlrUni = LeerEntero("Ingrese Valor Unitario del Producto: ")
        TypeIVA = MenuIVA()       
        Products[Cod] = {}
        Products[Cod]["Name"] = Name
        Products[Cod]["VlrUni"] = VlrUni
        Products[Cod]["IVA"] = TypeIVA  
    return Products

#Función para Modificar Producto Existente
def ModificarProducto(Products):
    print("\n","=" * 40)
    print("\n\f MODIFICAR PRODUCTO")
    Cod = LeerString("Ingrese codigo del Producto")
    if Cod in Products:
        while True:                                                         #SubMenú para Modificar Producto
            print(" DATO A MODIFICAR ")
            print("1- Nombre")                                              #1 Modificar el Nombre
            print("2- Valor Unitario")                                      #2 Modificar el valor Unitario
            print("3- Tipo de Iva")                                         #3 Modificar tipo de IVA
            print("4- Return Menu")  
            try:
                Opc = int(input("\t>>Escoja una opción (1-4)? "))
                if Opc == 1:
                    Product[Cod]["Nombre"] = LeerString("Ingrese nuevo nombre: ")
                    print("Nombre modificado correctamente")
                if Opc == 2:
                    Product[Cod]["VlrUni"] = LeerEntero("Ingrese nuevo Valor Unitario: ")
                    print("Valor Unitario modificado correctamente")
                if Opc == 3:
                    Product[Cod]["IVA"] = LeerEntero("Ingrese nuevo valor de Hora: ")
                    Dicc[ID]["Value"] = Valor
                    print("Tipo de IVA modificado correctamente")
                if Opc == 4:
                    MsgNotify("PRODUCTO MODIFICADO EXITOSAMENTE")
                    return Products
                MsgNotify("Opción no valida")
                continue
            except ValueError:
                print("Error! Ingrese un numero entero valido")
    else:
        MsgNotify("EMPLEADO NO REGISTRADO")
        break

#Función para Eliminar de lista un producto Existente
def EliminarProducto(Products):
    print("\n","=" * 40)
    print("\n\f ELIMINAR PRODUCTO")
    Cod = LeerString("Ingrese codigo del Producto")
    if Cod in Products:
        Products.pop(ID)
        MsgNotify("PRODUCTO ELIMINADO EXITOSAMENTE")
        return Products                                            #Retorna una nueva lista de Productos
    MsgNotify("PRODUCTO NO REGISTRADO")

#Función para Establecer Porcentaje de IVA a un Producto
def MenuIVA():
    Iva_Porc = (0, 0.05, 0.19)
    while True:
        print("\n","=" * 40)
        print("*** TIPO DE IVA ***")
        print("1-   Exento")
        print("2-   Bienes")
        print("3-   General")
        try:
            Opc = int(input("\t>>Escoja una opción (1-3)? "))
            if Opc > 0 and Opc < 4:
                return Iva_Porc[Opc - 1]
            MsgNotify("Opción no valida")
            continue
        except ValueError:
            print("Error! Ingrese un numero entero valido")

#Función Imprimir Detalle de ventas del Día
def DetailsACME():
    pass


#******************************** FUNCIONES VALIDACIÓN Y NOTIFICACIÓN ********************************
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

#Función Leer String -> Evita que se ingresen Nombres Vacios
def LeerString(msg):
    while True:
        try:
            Name = input(msg)
            Name = Name.strip()
            if Name == "":
                MsgNotify("Error! Ingrese un nombre no Vacio")
                continue
            return Name
        except Exception as e:
            print("Error al ingresar el nombre.", e.message)

#Función para Actualizar Archivo de Productos
def UpdateProducts(Dicc):
    with open("Micromercado_ACME\Products.json", "w") as ProductsFile:
        json.dump(Dicc, ProductsFile)

#Función para Actualizar Archivo de Ventas
def UpdateSales(Dicc):
    Dia = date.today()
    with open(f"Micromercado_ACME\{Dia}.json", "w") as ProductsFile:
        json.dump(Dicc, ProductsFile)

#******************************** MAIN CODE ********************************
#Creación de Diccionarios para almacenar en Memoria
Sales = {}
Products = {}
#Fecha del Día para crear Archivo de ventas
Dia = date.today()
#Cargar Archivo de Ventas del día
try:
    SalesFile = open(f"Micromercado_ACME\{Dia}.json", "r")
    Sales = json.load(SalesFile)
    SalesFile.close()
except FileNotFoundError:
    SalesFile = open(f"Micromercado_ACME\{Dia}.json", "w")
    SalesFile.close()
#Cargar Archivo de Productos
try:
    ProductsFile = open("Micromercado_ACME\Products.json", "r")
    Products = json.load(ProductsFile)
    ProductsFile.close()
except FileNotFoundError:
    ProductsFile = open("Micromercado_ACME\Products.json", "w")
    ProductsFile.close()

#Enseñar Menú Principal
Opc = MainMenu()
if Opc == 1:
    Sales = SalesMenu(Sales, Products)
elif Opc == 2:
    Products = ProductsMenu(Products)
elif Opc == 3:
    pass
elif Opc == 4:
    UpdateProducts()
    UpdateSales()
    print("-" * 14)
    print(" CAJA CERRADA")
    print("-" * 14)
    break
        