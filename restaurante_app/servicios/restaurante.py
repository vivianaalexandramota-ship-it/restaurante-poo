class Restaurante:
    """Gestiona los productos y clientes registrados en el restaurante."""

    def __init__(self, nombre):
        # El restaurante inicia con listas vacías para guardar objetos
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        """Agrega un producto a la lista del restaurante."""
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        """Agrega un cliente a la lista del restaurante."""
        self.clientes.append(cliente)

    def mostrar_productos(self):
        """Muestra todos los productos registrados."""
        print("\nPRODUCTOS REGISTRADOS")
        print("-" * 30)
        for producto in self.productos:
            print(producto)

    def mostrar_clientes(self):
        """Muestra todos los clientes registrados."""
        print("\nCLIENTES REGISTRADOS")
        print("-" * 30)
        for cliente in self.clientes:
            print(cliente)

    def mostrar_resumen(self):
        """Muestra un resumen general del sistema."""
        print("\nRESUMEN DEL RESTAURANTE")
        print("-" * 30)
        print(f"Nombre del restaurante: {self.nombre}")
        print(f"Total de productos: {len(self.productos)}")
        print(f"Total de clientes: {len(self.clientes)}")
