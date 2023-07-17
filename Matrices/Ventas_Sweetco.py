def ProdMayorVentaSem(Mat, Prec):
    VSumProd = []
    for f in range(len(Mat)):
        Sum = 0
        for c in range(len(Mat[f])):
            Sum += Mat[f][c]
        VSumProd.append(Sum * Prec[f])
    print(VSumProd)
    return [VSumProd.index(max(VSumProd)) + 1, max(VSumProd)]

def DiaSemanaMayorVenta(Mat, Prec):
    VSumDia = []
    for c in range(len(Mat[1])):
        Sum = 0
        for f in range(len(Mat)):
            Sum += Mat[f][c] * Prec[f]
        VSumDia.append(Sum)
    return [VSumDia.index(max(VSumDia)) + 1, max(VSumDia)]

MVentas= [[100, 88, 92, 94, 85, 110, 118],
        [30, 42, 31, 32, 38, 40, 37],
        [23, 35, 39, 45, 55, 60, 61],
        [45, 50, 56, 65, 45, 57, 68],
        [18, 25, 31, 21, 22, 28, 32]]
Precios = (1500, 5000, 6500, 2500 ,22500)

MayorVentaSem = ProdMayorVentaSem(MVentas, Precios)
print("El productos que mas vende a la semana es el", MayorVentaSem[0], "con", MayorVentaSem[1])
MayorDiaVentas = DiaSemanaMayorVenta(MVentas, Precios)
print("El Día que mas se vende a la semana es el", MayorDiaVentas[0], "con", MayorDiaVentas[1])
