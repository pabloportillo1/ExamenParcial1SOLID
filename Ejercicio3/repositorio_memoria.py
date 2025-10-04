from .i_repositorio import IRepositorio

class RepositorioMemoria(IRepositorio):
    def __init__(self):
        self.libros = []

    def guardar(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro['titulo']}' guardado en memoria.")

    def cargar(self):
        return self.libros