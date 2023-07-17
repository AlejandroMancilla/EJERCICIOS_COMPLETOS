#ENCONTRAR LOS 3 MAS COMUNES CARACTERES DE UN STRING

def ValidarEntrada(msg):
    while True:
        Letras = {}
        Numeros = []
        Name = input(msg)
        Name = Name.strip()
        for i in range(0, len(Name)):
            Letras[Name[i]] = 0
        if len(Letras) < 3:
            print("La entrada contiene menos de 3 caracteres diferentes")
            continue
        if len(Name) < 3 or len(Name) > 10 ** 4:
            print("La entrada no cumple con los limites de longitud")
            continue
        for i in range(0, len(Name)):
            Letras[Name[i]] += 1
        return Letras

def BuscarMayor(Dicc):
    Numeros = list(Dicc.values())
    return sorted(Numeros, reverse=True)[:3]

Letras = {}
Letras = ValidarEntrada("Ingrese el nombre de la compañia: ")
Claves = list(Letras.keys())
Valores = list(Letras.values())
ClavesOrden = sorted(Claves)
LetrasOrden = {}
for i in ClavesOrden:
    LetrasOrden[i] = Letras[i] 
TresMayores = BuscarMayor(LetrasOrden)
for i in TresMayores:
    Claves = list(LetrasOrden.keys())
    Valores = list(LetrasOrden.values())
    print(Claves[Valores.index(i)], i)
    LetrasOrden.pop(Claves[Valores.index(i)])