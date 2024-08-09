import json
from datetime import datetime

def registrar_compra():
    compra = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "proveedor": {
            "nombre": input("Nombre del proveedor: "),
            "contacto": input("Contacto del proveedor: ")
        },
        "productos": []
    }

    while True:
        producto = input("Nombre del producto comprado (o 'fin' para terminar): ")
        if producto == 'fin':
            break
        cantidad = int(input(f"Cantidad de {producto}: "))
        precio_compra = float(input(f"Precio de compra de {producto}: "))
        
        compra["productos"].append({
            "nombre": producto,
            "cantidad": cantidad,
            "precio_compra": precio_compra
        })
    
    with open('compras.json', 'a') as file:
        json.dump(compra, file, indent=4)
        file.write("\n")

    print("Compra registrada exitosamente.")
