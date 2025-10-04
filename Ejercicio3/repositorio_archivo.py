# Asegúrate de importar IRepositorio desde el archivo correcto
from .i_repositorio import IRepositorio

class RepositorioArchivo(IRepositorio):
    def __init__(self, archivo):
        self.archivo = archivo

    def guardar(self, libro):
        with open(self.archivo, 'a') as file:
            file.write(f"{libro['titulo']},{libro['autor']}\n")
        print(f"Libro '{libro['titulo']}' guardado exitosamente.")

    def cargar(self):
        libros = []
        with open(self.archivo, 'r') as file:
            for line in file:
                titulo, autor = line.strip().split(',')
                libros.append({'titulo': titulo, 'autor': autor})
        return libros