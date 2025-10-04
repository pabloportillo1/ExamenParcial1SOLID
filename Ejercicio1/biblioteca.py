class Biblioteca:
    def __init__(self, libros):
        self.libros = libros

    def buscar_libro(self, estrategia, termino):
        # La lista de libros original no se modifica
        return estrategia.buscar_libro(self.libros, termino)
