#Se tiene un archivo plano con las ventas decada mes durante el año para cada venededor de la compañía y 
#se requiere convertir este archivo a un formato JSON para poder ser exportado a la base de datos corporativa.

import json

with open("DatosCSV.txt","r")as FileCSV:
    Data = FileCSV.readlines()

Data.pop(0)
DataJson = {}
DataJson["Vendedores"] = []
for Seller in Data:
    LstSel = Seller.rstrip().split(",")
    DataJson["Vendedores"].append({
        "Apellido":LstSel[0],
        "Id":LstSel[1],
        "Ventas":LstSel[2:]
    })

with open("Datos.json","w")as DestFile:
    json.dump(DataJson, DestFile, indent=4)