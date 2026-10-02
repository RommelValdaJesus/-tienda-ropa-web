class Prenda:
    def __init__(self, nombre, precio, categoria, talla, cantidad,
                 fecha_ingreso, en_oferta=False):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.talla = talla
        self.cantidad = cantidad
        self.fecha_ingreso = fecha_ingreso
        self.en_oferta = en_oferta

    def __str__(self):
        return f"{self.nombre} ({self.categoria}, {self.talla}) - Bs {self.precio}"