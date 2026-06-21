# Importaciones de las clases ubicadas en otros módulos del proyecto
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


# main.py es el punto de arranque del programa
if __name__ == "__main__":
    # Creación del servicio principal
    restaurante = Restaurante("Sabor Criollo")

    # Creación de objetos de tipo Producto
    producto1 = Producto("Arroz con pollo", "Plato fuerte", 3.50)
    producto2 = Producto("Jugo natural", "Bebida", 1.25)
    producto3 = Producto("Ensalada mixta", "Entrada", 2.00)

    # Creación de objetos de tipo Cliente
    cliente1 = Cliente("Geovanny Velasco", "0923456789", "0991112222")
    cliente2 = Cliente("Viviana Mota", "0912345678", "0983334444")

    # Registro de productos y clientes en el restaurante
    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)
    restaurante.agregar_producto(producto3)

    restaurante.agregar_cliente(cliente1)
    restaurante.agregar_cliente(cliente2)

    # Presentación de la información en consola
    print("SISTEMA BÁSICO DE GESTIÓN DE RESTAURANTE")
    print("=" * 45)
    restaurante.mostrar_resumen()
    restaurante.mostrar_productos()
    restaurante.mostrar_clientes()

    # Ejemplo de uso de un método propio de Producto
    precio_descuento = producto1.aplicar_descuento(10)
    print("\nEJEMPLO DE DESCUENTO")
    print("-" * 30)
    print(f"{producto1.nombre} con 10% de descuento cuesta: ${precio_descuento:.2f}")
