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
        print("\t     Sizes")
        print("\t1-   Small")
        print("\t2-   Medium")
        print("\t3-   Large")
        Opc = ReadInt("\tChoose an Option (1-3): ")
        if Opc > 3:
            MsgNotify("Invalid Option")
            continue
        else:
            break
    return Sizes[Opc-1]

def IndexList(Data, Msg):
    print("*" * 20,"LIST OF PETS", "*" * 20)
    print("|{:^8}|{:^18}|{:^18}|".format("INDEX","PET TYPE", "BREED"))
    print("+","-"*6,"+","-"*16,"+","-"*16,"+")
    Index = 1
    for Pet in Data["Pets"]:
        print("|{:^8}|{:^18}|{:^18}|".format(Index, Pet["Type"], Pet["Breed"]))
        Index += 1
    while True:
        Opc = ReadInt(Msg)
        if Opc <= Index:
            return Opc
        else:
            MsgNotify("Index out of list")

def ListPets(Data):
    print("*" * 48,"GENERAL LIST OF PETS", "*" * 48)
    print("|{:^18}|{:^18}|{:^18}|{:^18}|{:<40}|".format("PET TYPE", "BREED", "SIZE", "PRICE", "SERVICES"))
    print("+","-"*16,"+","-"*16,"+","-"*16,"+","-"*16,"+","-"*38,"+")
    for Pet in Data["Pets"]:
        print("|{:^18}|{:^18}|{:^18}|{:^18}|{:<40}|".format(Pet["Type"], Pet["Breed"], Pet["Size"], Pet["Price"], str(Pet["Services"])))
    MsgNotify("END OF LIST")

def ListbyType(Data):
    while True:
        Types = []
        for Pet in Data["Pets"]:
            if not Pet["Type"] in Types:
                Types.append(Pet["Type"])
        for i in range(1, len(Types)+1):
            print(f"{i} - {Types[i-1]}")
        Opc = ReadInt(f"Choose a Pet's Type (1 - {len(Types)+1}): ")
        if Opc < len(Types)+1:
            print("*" * 38,"LIST OF PETS BY TYPE", "*" * 38)
            Type = Types[Opc-1]
            print(f"TYPE = {Type}")
            print("-" * 98)
            print("|{:^18}|{:^18}|{:^18}|{:<40}|".format("BREED", "SIZE", "PRICE", "SERVICES"))
            print("+","-"*16,"+","-"*16,"+","-"*16,"+","-"*38,"+")
            for Pet in Data["Pets"]:
                if Pet["Type"] == Type:
                    print("|{:^18}|{:^18}|{:^18}|{:<40}|".format(Pet["Breed"], Pet["Size"], Pet["Price"], str(Pet["Services"])))
            MsgNotify("END OF LIST")
            break
        else:
            MsgNotify("Invalid Option")
            continue

def NewPet(Data):
    Types = []
    for Pet in Data["Pets"]:
        if not Pet["Type"] in Types:
            Types.append(Pet["Type"])
    if len(Types) == 0:
        print("Create new Type")
        Type = ReadString("Pet Type: ")
    else:
        for i in range(1, len(Types)+1):
            print(f"{i} - {Types[i-1]}")
        print(f"{len(Types)+1} - CREATE NEW TYPE")
        print(f"{len(Types)+2} - RETURN")
        Opc = ReadInt(f"\t>>Choose an Option (1-{len(Types) + 1}): ")
        if Opc == len(Types)+1:
            Type = ReadString("Pet Type: ")
        elif Opc == len(Types)+2:
            return Data
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
    Data["Pets"].append({
        "Type": Type,
        "Breed":Breed,
        "Size":Size,
        "Price":Price,
        "Services":Services
    })
    MsgNotify("PET REGISTERED SUCCESFULLY")
    return Data

def UpdatePet(Data):
    Ind = IndexList(Data, "\nEnter Index of Pet to Update: ")
    Pet = Data["Pets"][Ind-1]
    while True:
        print("-" * 99)
        print("|{:^18}|{:^18}|{:^18}|{:<40}|".format("BREED", "SIZE", "PRICE", "SERVICES"))
        print("|{:^18}|{:^18}|{:^18}|{:<40}|".format(Pet["Breed"], Pet["Size"], Pet["Price"], str(Pet["Services"])))
        Opc = MenuModify()
        if Opc == 1:
            NewSize = MenuSize()
            Data["Pets"][Ind-1]["Size"] = NewSize
        elif Opc == 2:
            NewPrice = ReadFloat("New Pet Price: ")
            Data["Pets"][Ind-1]["Price"] = NewPrice
        elif Opc == 3:
            NewServices = ModifyServices(Data, Ind)
            Data["Pets"][Ind-1]["Services"] = NewServices
        else:
            MsgNotify("PET UPDATED SUCCESFULLY")
            return Data

def MenuModify():
    while True:
        print("\n     MODIFY MENU")
        print("1-   Size")
        print("2-   Price")
        print("3-   Services")
        print("4-   Return to Menu")
        Opc = ReadInt("\tChoose an Option (1-4): ")
        if Opc > 4:
            MsgNotify("Invalid Option")
            continue
        else:
            break
    return Opc

def ModifyServices(Data, Ind):
    Services = []
    Services = list(Data["Pets"][Ind-1]["Services"])
    while True:
        print("\n\t1 - Add Service")
        print("\t2 - Remove Service")
        print("\t3 - Return to Modify Menu")
        Opc = ReadInt("\tChoose an Option(1-2): ")
        for i in range(1, len(Services)+1):
                print(f"{i} - {Services[i-1]}")
        if Opc == 1:
            NewService = ReadString("Enter a new Service: ")            
            if NewService in Services:
                MsgNotify("Existing Service")
            else:
                Services.append(NewService)
        elif Opc == 2:
            Del = ReadInt("\tChoose Service to remove: ")
            if Del < len(Services) + 1:
                Services.pop(Del - 1)
            else:
                MsgNotify("Invalid Option")
        elif Opc == 3:
            return Services
        else:
            MsgNotify("Invalid Option")

def DeletePet(Data):
    Opc = IndexList(Data, "Enter Index of Pet to Delete: ")
    Delete = Data["Pets"].pop(Opc-1)
    print("\nPet Deleted:")
    print(f"\tType = {Delete['Type']}")
    print(f"\tType = {Delete['Breed']}")
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
            Data["Pets"] = []
    return Data

def UpdateFile(Ruta, Data):
    with open(Ruta, "w") as OpenFile:
        json.dump(Data, OpenFile, ensure_ascii=False, indent=4)

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