def MsgNotify(msg):
    print("\n NOTIFY!", msg)
    input(" -> Presione cualquier letra para regresar al Menú")
    print("=" * 45)

def LeerNota(msg):
    while True:
        try:
            Nota = float(input(msg))
            if Nota < 0 and Nota > 5:
                MsgNotify("Nota no Válida")
                continue
            return Nota
        except TypeError:
            print("Ingrese solo numeros")

Asignaturas = ["Matematicas", "Física", "Química", "Historia", "Lengua"]
Calificaciones = {}
for i in Asignaturas:
    Calificaciones[i] = LeerNota(f"Ingrese nota de {i}: ")
Tupla = Calificaciones.items()
print("=" * 45)
for (k,v) in Tupla:
    print(f"En {k} has sacado {v}")
print("=" * 45)

