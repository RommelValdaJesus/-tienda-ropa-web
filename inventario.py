from singleton_observable import SingletonObservable

class Inventario(SingletonObservable):
    def __init__(self):
        if not hasattr(self, "prendas"):
            self.prendas = []

    def agregar(self, prenda):
        self.prendas.append(prenda)
        self.notificar(prenda)

    def valor_total(self):
        return sum(p.precio * p.cantidad for p in self.prendas)

    def total_unidades(self):
        return sum(p.cantidad for p in self.prendas)

    def total_en_oferta(self):
        return sum(1 for p in self.prendas if p.en_oferta)