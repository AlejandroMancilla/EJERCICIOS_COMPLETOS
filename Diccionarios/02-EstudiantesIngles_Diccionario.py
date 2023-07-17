#REVISAR EL NUMERO DE ESTUDIANTES SUSCRITOS A EL PERIODICO DE INGLES UNICAMENTE
# La primera linea indica el numero de estudiantes suscritos al periodico de Ingles
# La segunda linea es una lista de estudiantes separadas por coma
# La tercera linea indica el numero de estudiantes suscritos al periodico de Frances
# La cuarta  linea es una lista de estudiantes separadas por coma

#Función para leer cantidad entera positiva
def LeerCantidad(msg):
    while True:
        try:
            Codigo = int(input(msg))
            if Codigo <= 0:
                MsgNotify("Cantidad no válida")
                continue
            return Codigo
        except ValueError:
            MsgNotify("Ingrese un dato válido")

#Crear SET de estudiantes suscritos al periodico de Ingles
NumIngles = LeerCantidad("Numeros de Estudiantes de Ingles: ")
EstIngles = input("Listado de Estudiantes suscritos a periodico Ingles:\n")
SetIngles = set(EstIngles.split())

#Crear SET de estudiantes suscritos al periodico de Frances
NumFrances = LeerCantidad("Numeros de Estudiantes de Frances: ")
EstFrances = input("Listado de Estudiantes suscritos a periodico Frances:\n")
SetFrances = set(EstFrances.split())

#Imprimir la diferencia de los SET
print("-" * 20)
print(len(SetIngles - SetFrances))
print("-" * 20)