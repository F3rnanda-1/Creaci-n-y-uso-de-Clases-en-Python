class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        if precio <= 0 or cantidad <= 0:
            print("El precio y la cantidad deben ser positivos.")
            return
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                producto["cantidad"] += cantidad
                producto["precio"] = precio
                print(f"Producto '{nombre}' actualizado en el inventario.")
                return
        nuevo_producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        self.productos.append(nuevo_producto)
        print(f"Producto '{nombre}' agregado al inventario.")

    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                if cantidad <= 0:
                    print("La cantidad a vender debe ser positiva.")
                    return
                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    print(f"Venta realizada: {cantidad} unidades de '{nombre}'.")
                    if producto["cantidad"] == 0:
                        print(f"El producto '{nombre}' se ha agotado.")
                    return
                else:
                    print(f"Stock insuficiente. Solo hay {producto['cantidad']} unidades.")
                    return
        print("El producto no se encuentra en el inventario.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return
        print(f"\nInventario de {self.nombre_tienda}:")
        for producto in self.productos:
            print(f"- {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
        print("")

    def producto_mas_caro(self):
        if not self.productos:
            print("No hay productos en el inventario.")
            return
        producto_caro = max(self.productos, key=lambda p: p["precio"])
        print(f"El producto más caro es '{producto_caro['nombre']}' con un precio de ${producto_caro['precio']}.")


def main():
    tienda = InventarioTienda("Papelería Toby")

    while True:
        print("MENÚ DE LA PAPELERÍA")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Ver inventario")
        print("4. Consultar el producto más caro")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad del producto: "))
                tienda.agregar_producto(nombre, precio, cantidad)
            except ValueError:
                print("Opción inválida. El precio y cantidad deben ser numéricos.")

        elif opcion == "2":
            nombre = input("Nombre del producto a vender: ")
            try:
                cantidad = int(input("Cantidad a vender: "))
                tienda.vender_producto(nombre, cantidad)
            except ValueError:
                print("Opción inválida. La cantidad debe ser un número entero.")

        elif opcion == "3":
            tienda.mostrar_inventario()

        elif opcion == "4":
            tienda.producto_mas_caro()

        elif opcion == "5":
            print("Gracias por usar el sistema de la Papelería.")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
