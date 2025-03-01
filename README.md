# Sistema de Gestión PanCamp

### Descripción
El **Sistema de Gestión PanCamp** es una aplicación de gestión para una panadería que permite registrar ventas, compras y generar informes de ventas y stock. Está diseñado para facilitar la administración de productos, proveedores, clientes y empleados en una panadería.

### Funcionalidades
- **Registrar Venta:** Permite registrar las ventas realizadas, incluyendo detalles del cliente, empleado y los productos vendidos.
- **Registrar Compra:** Permite registrar las compras realizadas a proveedores, incluyendo los productos comprados y sus precios.
- **Generar Informe de Ventas:** Genera un informe de ventas en formato CSV.
- **Generar Informe de Stock:** Genera un informe de stock en formato CSV.

### Estructura del Proyecto
El proyecto está compuesto por varios módulos:

- **gestion_ventas.py:** Módulo para registrar ventas.
- **gestion_compras.py:** Módulo para registrar compras.
- **gestion_informes.py:** Módulo para generar informes de ventas y stock.
- **main.py:** Script principal que ejecuta el sistema de gestión.

### Detalles de Implementación

#### registrar_venta()
Registra una venta incluyendo información del cliente, empleado y productos vendidos. La información se guarda en un archivo `ventas.json`.

#### registrar_compra()
Registra una compra incluyendo información del proveedor y los productos comprados. La información se guarda en un archivo `compras.json`.

#### generar_informe_ventas()
Genera un informe de ventas en formato CSV y lo guarda en un archivo `informe_ventas_<fecha>.csv`.

#### generar_informe_stock()
Genera un informe de stock en formato CSV y lo guarda en un archivo `informe_stock_<fecha>.csv`.

### Estructura de Datos

#### Productos
Se han definido varias categorías de productos en el sistema:

- **Panaderia**
- **Pasteleria**
- **Bebidas**
- **Apartado de promociones**

Cada categoría tiene productos asociados con sus respectivos precios.

#### Stock
El stock de productos se mantiene actualizado y es utilizado para generar el informe de stock.

____
### 📬 Contacto
- 📧 Correo electrónico: cristanchodayana062017@gmail.com

- 💼 LinkedIn: [Elidallana Cristancho Caceres](https://www.linkedin.com/in/elidallanacristancho/)

¡Gracias por ser parte de esta aventura! 🚀✨
