#MINI CALCULADORA - MENÚ

#Función Mensaje Error
def MsgError(msg):
    print(" ERROR!", msg)
    input(" Presione cualquier letra para regresar al Menú")

#Funcion Menú
def Menu():
    while True:
        print("\n*********")
        print(" MENÚ ")
        print("\t1. Sumar")
        print("\t2. Restar")
        print("\t3. Multiplicar")
        print("\t4. Dividir")
        print("\t5. Potencia")
        print("\t6. Factorial")
        print("\t7. Salir")
        try:
            Opc = int(input("Elija una operación: "))
            if Opc < 0 or Opc > 7:
                MsgError("Opción no valida")
                continue
            else:
                return Opc
        except ValueError:
            print("Error! Ingrese un numero entero valido")

#Función Validar Entero
def LeerInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Error! Ingrese un numero entero valido")

#Funcion Ler Entero Diferente de 0
def LeerIntNo0(msg):
    while True:
        n = int(input(msg))
        if n != 0:
            return n
        else:
            MsgError("No puede dividirse por 0")
        
#Funcion Sumar
def Suma2():
    print("-" * 45)
    print(" SUMA")
    Num1 = LeerInt("\nIngrese un Sumando: ")
    Num2 = LeerInt("Ingrese otro Sumando: ")
    Suma = Num1 + Num2
    print(f"Resultado de la suma = {Suma}")
    input(" Presione cualquier letra para regresar al Menú")

#Funcion Restar
def Resta2():
    print("-" * 45)
    print(" RESTA")
    Num1 = LeerInt("\nIngrese Minuendo: ")
    Num2 = LeerInt("Ingrese Sustraendo: ")
    Resta = Num1 - Num2
    print(f"Resultado de la resta = {Resta}")
    input(" Presione cualquier letra para regresar al Menú")

#Funcion Multiplicar
def Produc2():
    print("-" * 45)
    print(" MULTIPLICACIÓN")
    Num1 = LeerInt("\nIngrese Multiplicando: ")
    Num2 = LeerInt("Ingrese Multiplicador: ")
    Producto = Num1 * Num2
    print(f"Resultado de la multiplicación = {Producto}")
    input(" Presione cualquier letra para regresar al Menú")

#Funcion Dividir
def Div2():
    print("-" * 45)
    print(" DIVISIÓN")
    Num1 = LeerInt("\nIngrese Dividendo: ")
    Num2 = LeerIntNo0("Ingrese Divisor: ")
    Division = Num1 / Num2
    print(f"Resultado de la división = {Division}")
    input(" Presione cualquier letra para regresar al Menú")

#Funcion Potencia
def Pot2():
    print("-" * 45)
    print(" POTENCIACIÓN")
    Num1 = LeerInt("\nIngrese la Base: ")
    Num2 = LeerInt("Ingrese el Exponente: ")
    Potencia = Num1 ** Num2
    print(f"Resultado de la Potenciación = {Potencia}")
    input(" Presione cualquier letra para regresar al Menú")

#Funcion Factorial
def Fact():
    print("-" * 45)
    print(" FACTORIAL")
    Num1 = LeerInt("Ingrese numero: ")
    Facto = 1
    for i in range(1, n1 + 1):
        Facto *= i
    print(f"Resultado del Factorial = {Facto}")
    input(" Presione cualquier letra para regresar al Menú")

#Codigo Principal
while True:
    Opc = Menu()
    if Opc == 1:
        Suma2()
    elif Opc == 2:
        Resta2()
    elif Opc == 3:
        Produc2()
    elif Opc == 4:
        Div2()
    elif Opc == 5:
        Pot2()
    elif Opc == 6:
        Fact()
    elif Opc == 7:
        print("-" * 45)
        print("GRACIAS POR USAR LA MINI CALCULADORA")
        print("-" * 45)
        break