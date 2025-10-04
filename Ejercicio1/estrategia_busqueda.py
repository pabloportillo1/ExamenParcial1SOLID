# Estrategia de búsqueda
from abc import ABC, abstractmethod

class EstrategiaBusqueda(ABC):
    @abstractmethod
    def buscar_libro(self, biblioteca, termino):
        pass

class BusquedaPorTitulo(EstrategiaBusqueda):
    def buscar_libro(self, biblioteca, termino):
        return [libro for libro in biblioteca if termino.lower() in libro['titulo'].lower()]

class BusquedaPorAutor(EstrategiaBusqueda):
    def buscar_libro(self, biblioteca, termino):
        return [libro for libro in biblioteca if termino.lower() in libro['autor'].lower()]

class BusquedaPorISBN(EstrategiaBusqueda):
    def buscar_libro(self, biblioteca, termino):
        return [libro for libro in biblioteca if termino == libro['isbn']]

class BusquedaPorDisponibilidad(EstrategiaBusqueda):
    def buscar_libro(self, biblioteca, termino):
        return [libro for libro in biblioteca if libro['disponible'] == termino]