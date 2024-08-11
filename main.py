from gestion_ventas import registrar_Ventas
from gestion_compras import registrar_compra
from gestion_informes import generar_informe_ventas, generar_informe_stock

#Menu principal
def main():
    while True:
        print("\nSistema de Gestión PanCamp")
        print("1. Registrar Venta")
        print("2. Registrar Compra")
        print("3. Generar Informe de Ventas")
        print("4. Generar Informe de Stock")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_Ventas()
        elif opcion == '2':
            registrar_compra()
        elif opcion == '3':
            generar_informe_ventas()
        elif opcion == '4':
            generar_informe_stock()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

