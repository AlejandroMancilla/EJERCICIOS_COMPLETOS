import json
import os

#-------------------PRINCIPAL FUNCTIONS------------------------
def MainMenu():
    print("\n","=" * 40)
    print("******* PET SHOP ACME ******** ")
    print("     MAIN MENU")
    print("1-   General List of Pets availables")
    print("2-   List of Pets By Tipe")
    print("3-   Register New Pet")
    print("4-   Update Pet")
    print("5-   Delete Pet")
    print("6-   Exit")
    Opc = ReadInt("\t>>Choose an Option (1-6): ")
    if Opc > 7:                                   
        MsgNotify("Invalid Option")
        return
    else:
        return Opc

def Continue():
    while True:
        print("     Continue?")
        print("1-   Yes")
        print("2-   No")
        Opc = ReadInt("\tChoose an Option (1-2): ")
        if Opc > 2:
            MsgNotify("Invalid Option")
            continue
        else:
            break
    return Opc

def MenuSize():
    Sizes = ["SMALL", "MEDIUM", "LARGE"]
    while True:
        print("     Sizes")
        print("1-   Small")
        print("2-   Medium")
        print("3-   Large")
        Opc = ReadInt("\tChoose an Option (1-3): ")
        if Opc > 3:
            MsgNotify("Invalid Option")
            continue
        else:
            break
    return Sizes[Opc-1]

def MenuModify():
    while True:
        print("\t     Data to Modify")
        print("\t1-   Size")
        print("\t2-   Price")
        print("\t3-   Services")
        print("\t4-   Return")
        Opc = ReadInt("\tChoose an Option (1-3): ")
        if Opc > 4:
            MsgNotify("Invalid Option")
            continue
        else:
            break
    return Opc

def ModifyServices(Data):
    pass

def IndexList(Data):
    print("*" * 30,"LIST OF PETS", "*" * 30)
    print("|{:^8}|{:^18}|{:^18}|{:^18}|".format("INDEX","PET TYPE", "BREED", "PRICE"))
    print("+","-"*6,"+","-"*16,"+","-"*16,"+","-"*16,"+")
    Index = 1
    for Type in Data["Pets"].keys():
        for Pet in Data["Pets"][Type]:
            print("|{:^8}|{:^18}|{:^18}|{:^18}|".format(Index, Type, Pet["Breed"], Pet["Price"]))
            Index += 1

def ListPets(Data):
    print("*" * 48,"GENERAL LIST OF PETS", "*" * 48)
    print("|{:^18}|{:^18}|{:^18}|{:^18}|{:<40}|".format("PET TYPE", "BREED", "SIZE", "PRICE", "SERVICES"))
    print("+","-"*16,"+","-"*16,"+","-"*16,"+","-"*16,"+","-"*38,"+")
    for Type in Data["Pets"].keys():
        for Pet in Data["Pets"][Type]:
            print("|{:^18}|{:^18}|{:^18}|{:^18}|{:<40}|".format(Type, Pet["Breed"], Pet["Size"], Pet["Price"], str(Pet["Services"])))
    MsgNotify("END OF LIST")

def ListbyType(Data):
    while True:
        Types = list(Data["Pets"].keys())
        for i in range(1, len(Types)+1):
            print(f"{i} - {Types[i-1]}")
        Opc = ReadInt(f"Choose a Pet's Type (1 - {len(Types)+1}): ")
        if Opc < len(Types)+1:
            print("*" * 48,"LIST OF PETS BY TYPE", "*" * 48)
            Type = Types[Opc-1]
            print(f"TYPE = {Type}")
            print("|{:^18}|{:^18}|{:^18}|{:<40}|".format("BREED", "SIZE", "PRICE", "SERVICES"))
            print("+","-"*16,"+","-"*16,"+","-"*16,"+","-"*38,"+")
            for Pet in Data["Pets"][Type]:
                print("|{:^18}|{:^18}|{:^18}|{:<40}|".format(Pet["Breed"], Pet["Size"], Pet["Price"], str(Pet["Services"])))
            MsgNotify("END OF LIST")
            break
        else:
            MsgNotify("Invalid Option")
            continue

def NewPet(Data):
    Types = list(Data["Pets"].keys())
    if len(Types) == 0:
        print("Create new Type")
        Type = ReadString("Pet Type: ")
        Data["Pets"][Type] = []
    else:
        for i in range(1, len(Types)+1):
            print(f"{i} - {Types[i-1]}")
        print(f"{len(Types)+1} - Create New Type")
        Opc = ReadInt(f"\t>>Choose an Option (1-{len(Types) + 1}): ")
        if Opc == len(Types)+1:
            Type = ReadString("Pet Type: ")
            Data["Pets"][Type] = []
        else:
            Type = Types[Opc-1]
    Breed = ReadString(f"Breed of {Type}: ")
    Size = MenuSize()
    Price = ReadFloat("Pet Price: ")
    Services = []
    while True:
        Services.append(ReadString("New Service: "))
        Opc = Continue()
        if Opc == 2:
            break
    Data["Pets"][Type].append({
        "Breed":Breed,
        "Size":Size,
        "Price":Price,
        "Services":Services
    })
    MsgNotify("PET REGISTERED SUCCESFULLY")
    return Data

def UpdatePet(Data):
    IndexList(Data)
    Opc = MenuModify()
    if Opc == 1:
        NewSize = MenuSize()
    elif Opc == 2:
        NewPrice = ReadFloat("New Pet Price: ")
    elif Opc == 3:
        NewServices = ModifyServices(Data)
    else:
        return Data
    
    MsgNotify("PET UPDATED SUCCESFULLY")
    return Data

def DeletePet(Data):
    IndexList(Data)
    MsgNotify("PET DELETED SUCCESFULLY")
    return Data

#---------------------FUNCIONES MISCELANEA-----------------------
def MsgNotify(msg):
    print("\n", msg)
    input(" -> Presione cualquier letra para regresar al Menú")
    print("=" * 45, "\n")

def ReadInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 0:
                MsgNotify("Error! Dato no valido")
                continue
            return n
        except ValueError:
            print("Error! Ingrese un numero Entero")

def ReadFloat(msg):
    while True:
        try:
            n = float(input(msg))
            if n < 0:
                MsgNotify("Error! Dato no valido")
                continue
            return n
        except ValueError:
            print("Error! Ingrese un numero Entero")

def ReadString(msg):
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

def LoadFile(Ruta):
    with open(Ruta, "a+") as OpenFile:
        OpenFile.seek(0)
        try:
            Data = json.load(OpenFile)
        except Exception as e:
            Data = {}
            Data["Pets"] = {}
    return Data

def UpdateFile(Ruta, Data):
    with open(Ruta, "w") as OpenFile:
        json.dump(Data, OpenFile, indent=4)

def Clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#---------------------------MAIN CODE-----------------------------
PetsData = {}
Ruta = "PetShopping.json"
PetsData = LoadFile(Ruta)
print(PetsData)
while True:
    Clear()
    Opc = MainMenu()
    Clear()
    if Opc == 1:
        ListPets(PetsData)
    elif Opc == 2:
        ListbyType(PetsData)
    elif Opc == 3:
        PetsData = NewPet(PetsData)
    elif Opc == 4:
        PetsData = UpdatePet(PetsData)
    elif Opc == 5:
        PetsData = DeletePet(PetsData)
    elif Opc == 6:
        UpdateFile(Ruta, PetsData)
        print("=" * 39)
        print("  PET SHOP ACME - GRACIAS")
        print("=" * 39)
        break