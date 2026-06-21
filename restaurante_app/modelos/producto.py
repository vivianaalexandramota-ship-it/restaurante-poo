class Producto:
    """Representa un producto disponible en el restaurante."""

    def __init__(self, nombre, categoria, precio):
        # Atributos principales del producto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        """Calcula el precio final luego de aplicar un descuento."""
        descuento = self.precio * porcentaje / 100
        return self.precio - descuento

    def __str__(self):
        """Permite mostrar el producto como texto organizado."""
        return f"Producto: {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f}"
