import csv
from datetime import datetime

ventas = [
    {"fecha": "2024-08-01", "producto": "Pan", "cantidad": 10, "precio": 20},
]

stock = [
    {"producto": "Pan", "cantidad": 50},
]

def generar_informe_ventas():
    """Genera un informe de ventas y lo guarda en un archivo CSV."""
    fecha = datetime.now().strftime("%Y-%m-%d")
    archivo = f"informe_ventas_{fecha}.csv"
    
    with open(archivo, 'w', newline='') as csvfile:
        fieldnames = ["fecha", "producto", "cantidad", "precio"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for venta in ventas:
            writer.writerow(venta)
    
    print(f"Informe de ventas generado: {archivo}")

def generar_informe_stock():
    """Genera un informe de stock y lo guarda en un archivo CSV."""
    fecha = datetime.now().strftime("%Y-%m-%d")
    archivo = f"informe_stock_{fecha}.csv"
    
    with open(archivo, 'w', newline='') as csvfile:
        fieldnames = ["producto", "cantidad"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for item in stock:
            writer.writerow(item)
    
    print(f"Informe de stock generado: {archivo}")

import csv
from datetime import datetime

stock = [
    {"producto": "Pan", "cantidad": 50},
    {"producto": "Pan de Bono", "cantidad": 80},
    {"producto": "Pan de Queso", "cantidad": 70},
    {"producto": "Pan Cascarita", "cantidad": 20},
    {"producto": "Pan de Yuca", "cantidad": 100},
    {"producto": "Calentano", "cantidad": 90},
    {"producto": "Rollito de Sal", "cantidad": 75},
    {"producto": "Pan Integral", "cantidad": 45},
    {"producto": "Pan relleno de Arequipe", "cantidad": 85},
    {"producto": "Pan con Salchicha", "cantidad": 35},
    {"producto": "Pan recubierto de Chocolate", "cantidad": 55},
    {"producto": "Pastel de Vainilla", "cantidad": 50},
    {"producto": "Pastel de Chocolate", "cantidad": 85},
    {"producto": "Pastel de bodas", "cantidad": 96},
    {"producto": "Glaseado de Vainilla", "cantidad": 20},
    {"producto": "Glaseado de Chocolate", "cantidad": 75},
    {"producto": "Pastel de Arequipe", "cantidad": 60},
    {"producto": "Pastel de Oreo", "cantidad": 28},
    {"producto": "Postre de Limón", "cantidad": 95},
    {"producto": "Postre de Vainilla", "cantidad": 60},
    {"producto": "Postre de Tres Leches", "cantidad": 40},
    {"producto": "Coca-Cola", "cantidad": 45},
    {"producto": "Pepsi", "cantidad": 85},
    {"producto": "Red-Bull", "cantidad": 70},
    {"producto": "Gatorade", "cantidad": 35},
    {"producto": "Budweiser", "cantidad": 55},
    {"producto": "Hit", "cantidad": 30},
    {"producto": "Pony-Malta", "cantidad": 45},
    {"producto": "Sprite", "cantidad": 70},
    {"producto": "Monster", "cantidad": 60},
    {"producto": "Tropicana", "cantidad": 45},
    {"producto": "Panes Integrales", "cantidad": 63},
    {"producto": "Panes recubiertos de Chocolate", "cantidad": 30},
    {"producto": "Pasteles de Vainilla", "cantidad": 40},
    {"producto": "Postres de Oreo", "cantidad": 20},
    {"producto": "Pan con Salchicha y 1 Pony Malta", "cantidad": 10},
    {"producto": "Postre de Oreo y 1 Budweiser", "cantidad": 15},

]

def generar_informe_stock():
    """Genera un informe de stock y lo guarda en un archivo CSV."""
    fecha = datetime.now().strftime("%Y-%m-%d")
    archivo = f"informe_stock_{fecha}.csv"
    
    with open(archivo, 'w', newline='') as csvfile:
        fieldnames = ["producto", "cantidad"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for item in stock:
            writer.writerow(item)
    
    print(f"Informe de stock generado: {archivo}")

if __name__ == "__main__":
    generar_informe_stock()
