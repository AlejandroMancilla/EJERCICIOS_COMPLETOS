import os

def MsgNotify(msg):
    print("\n NOTIFY!", msg)
    input(" -> Presione cualquier letra para regresar al Menú")
    print("=" * 45)

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

def MenuContinue():
    while True:
        print("-" * 40)                                         #SubMenú para continuar listado
        print("¿Continuar Listado?")
        print("1- Sí")
        print("2- No")
        try:
            Opc = int(input("\t>>Escoja una opción (1-2)? "))
            if Opc == 1 or Opc == 2:
                return Opc
            else:
                MsgNotify("Opción no valida")
            continue
        except ValueError:
            print("Error! Ingrese un numero entero valido")

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

Diccionario = {}
while True:
    clear()
    Nombre = LeerString("Ingrese Nombre del Usuario: ")
    Nombre = Nombre.upper()
    if Nombre not in Diccionario.keys():
        Telefono = LeerEntero("Ingrese numero de Telefono: ")
        Diccionario[Nombre] = Telefono
    else:
        MsgNotify("Nombre ya registrado")
    Continue = MenuContinue()
    if Continue == 1:
        continue
    elif Continue == 2:
        clear()
        print("|{:^15}|{:^15}|".format("NOMBRE", "TELEFONO"))
        print("+","-" * 13, "+","-" * 13, "+")
        for i in Diccionario.keys():
            print("|{:<15}|{:<15}|".format(i, Diccionario[i]))
        break
