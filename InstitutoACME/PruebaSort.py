def ReturnName(Values):
    return Values['Name'] 

Dicc = {
        "Primero": {
            "5": {
                "Name": "Juan Perez",
                "Sexo": "M",
                "Promedio": 3.2
                    },
            "1": {
                "Name": "Jose Sanches",
                "Sexo": "M",
                "Promedio": 3.7
                    },
            "4": {
                "Name": "Diego Perez",
                "Sexo": "M",
                "Promedio": 4.9
                    },
            "2": {
                "Name": "Silvia Jaimes",
                "Sexo": "M",
                "Promedio": 4.2
                    }
                },
        "Segundo": {
            "8": {
                "Name": "Danna Mancilla",
                "Sexo": "M",
                "Promedio": 2.5
                    },
            "3": {
                "Name": "Samuel Mancilla",
                "Sexo": "M",
                "Promedio": 3.8
                    },
            "7": {
                "Name": "Lilia Paipa",
                "Sexo": "M",
                "Promedio": 5.0
                    },
            "6": {
                "Name": "Joe Mancilla",
                "Sexo": "M",
                "Promedio": 3.8
                    }
                },
        "Tercero": {
            "12": {
                "Name": "Diana Mancilla",
                "Sexo": "M",
                "Promedio": 2.5
                    },
            "9": {
                "Name": "Alejandro Mancilla",
                "Sexo": "M",
                "Promedio": 3.8
                    },
            "11": {
                "Name": "Angelica Paipa",
                "Sexo": "M",
                "Promedio": 5.0
                    },
            "10": {
                "Name": "Jose Guevara",
                "Sexo": "M",
                "Promedio": 3.8
                    }
            }
        }

Values = []
Values.extend(list(Dicc["Primero"].values()))
Values.sort(key=ReturnName)
print(Values)
for i in range(0, len(Values)):
    print(Values[i]["Name"])
    prom = float(input("PROMEDIO:"))
    for Id in Dicc["Primero"].keys():
        if Values[i]["Name"] == Dicc["Primero"][Id]["Name"]:
            Dicc["Primero"][Id]["Promedio"] = prom
for i in range(0, len(Values)):
    print(Values[i]["Name"])
    for Id in Dicc["Primero"].keys():
        if Values[i]["Name"] == Dicc["Primero"][Id]["Name"]:
            print(Dicc["Primero"][Id]["Promedio"])

