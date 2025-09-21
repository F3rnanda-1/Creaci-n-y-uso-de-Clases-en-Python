# Creaci-n-y-uso-de-Clases-en-Python
Inventario de Tienda
Fernanda Estefania Ramirez Uribe
24150896
1. Crea una clase llamada InventarioTienda que maneje productos de una tienda.
Atributos: nombre de la tienda, lista de productos (vacía al inicio).
Cada producto será un diccionario con: nombre, precio y cantidad.
Constructor: que inicialice el nombre y la lista vacía.
Métodos:
agregar_producto(nombre, precio, cantidad) → agrega un nuevo producto al inventario.
vender_producto(nombre, cantidad) → reduce la cantidad de un producto si hay suficiente stock.
mostrar_inventario() → muestra todos los productos con su precio y cantidad.
producto_mas_caro() → devuelve el nombre y precio del producto más caro.
2. En el programa principal:
Crea un objeto de tipo InventarioTienda.
Usa un ciclo while con menú para que el usuario pueda:
Agregar productos.
Vender productos.
Ver el inventario.
Consultar el producto más caro.
Salir del programa.
3. Valida con condicionales:
Que no se vendan productos inexistentes.
Que no se vendan más unidades de las que hay en stock.
Que el precio y la cantidad sean valores positivos.
