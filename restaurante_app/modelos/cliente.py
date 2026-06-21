class Cliente:
    """Representa a un cliente que consume o realiza un pedido."""

    def __init__(self, nombre, cedula, telefono):
        # Datos básicos del cliente
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def actualizar_telefono(self, nuevo_telefono):
        """Actualiza el número de teléfono del cliente."""
        self.telefono = nuevo_telefono

    def __str__(self):
        """Permite mostrar el cliente como texto organizado."""
        return f"Cliente: {self.nombre} | Cédula: {self.cedula} | Teléfono: {self.telefono}"
