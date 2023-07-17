#CALCULAR VALOR DE LA COMPRA DE UN USUARIO USANDO DICCIONARIOS
# Se le solicita al usuario los datos de su compra en pares (Codigo del Articulo + Cantidad comprada)
# Luego, se accede a los diccionarios establecidos para buscar el nombre y precio.
# Todos estos datos se guardan en un nuevo Diccionario el cual tendrá todos los datos de la compra total del Usuario.  
# Compra = {Codigo : {"Nombre" : NombreArticulo,
#                     "Cantidad" : Cantidad,
#                     "ValorUnitario" : ValorUnitario,
#                     "ValorTotal" : ValorTotal}

#Función para mostrar notificaciones al usuario
def MsgNotify(msg):
    print("Notify!",msg)
    input("Presione cualquier tecla para continuar")

#Función para Leer Código -> Solo permite ingresar numero Entero entre 1 y 5
def LeerCodigo():
    while True:
        try:
            Codigo = int(input("Código del Articulo (1-5): "))
            if Codigo < 0 or Codigo >5:
                MsgNotify("Codigo de Articulo no Registrado")
                continue
            return Codigo
        except ValueError:
            MsgNotify("Ingrese un dato válido")

#Función para Leer Cantidad -> Solo permite numeros enteros positivos
def LeerCantidad():
    while True:
        try:
            Codigo = int(input("Cantidad adquirida: "))
            if Codigo <= 0:
                MsgNotify("Cantidad no válida")
                continue
            return Codigo
        except ValueError:
            MsgNotify("Ingrese un dato válido")

Articulos = {1:"Lapiz", 2:"Cuadernos", 3:"Borrador", 4:"Calculadora", 5:"Escuadra"}
Valores = {1:2500, 2:3800, 3:1200, 4:35000, 5:3700}
Compra = {}

while True:
    print("\nIngrese codigo de Articulo (0 para finalizar compra)")
    Codigo = LeerCodigo()
    if Codigo == 0:                                                                     #Para dejar de ingresar Articulos, digitar 0
        break
    Cantidad = LeerCantidad()                                                           #Lectura de cantidad del articulo
    Nombre = Articulos[Codigo]                                                          #Trae dato de nombre de Diccionario de Articulos
    VlrUni = Valores[Codigo]                                                            #Trae dato de valor de Diccionario de Valores
    VlrTotalArt = VlrUni * Cantidad                                                     #Calcula total del articulo (Cant * Valor)
    Compra[Codigo] = {}                                                                 #Crea el diccionario con el codigo del Articulo
    Compra[Codigo]["Nombre"] = Nombre
    Compra[Codigo]["Cantidad"] = Cantidad
    Compra[Codigo]["Unitario"] = VlrUni
    Compra[Codigo]["TotalArt"] = VlrTotalArt

#Impresión de Factura
SumTotal = 0
print("=" * 53)
print("*" * 17, "DETALLE DE COMPRA", "*" *17)
#Encabezado de la factura
print("|{:<12}|{:<12}|{:<12}|{:<12}|".format("ARTICULO", "CANTIDAD", "VLR UNITARIO", "VALOR TOTAL"))
print("+------------" * 4)
for i in Compra.keys():
    #Imprime con formato para simular una factura
    print("|{:<12}|{:>12}|{:>12,}|{:>12,}|".format(Compra[i]["Nombre"], Compra[i]["Cantidad"], Compra[i]["Unitario"], Compra[i]["TotalArt"]))
    print("+------------" * 4)
    SumTotal += Compra[i]["TotalArt"]                       #Acumula el valor de la compra
print("TOTAL DE LA COMPRA=","{:,}".format(SumTotal))        #Imprime Valor total de la compra
print("=" * 53)