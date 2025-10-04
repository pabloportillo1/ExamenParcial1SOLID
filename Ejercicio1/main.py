# Importamos las clases necesarias
from estrategia_busqueda import BusquedaPorTitulo, BusquedaPorDisponibilidad
from biblioteca import Biblioteca

# Lista de libros (no se modifica)
libros = [
    {'titulo': 'Python para todos', 'autor': 'Juan Perez', 'isbn': '12345', 'disponible': True},
    {'titulo': 'JavaScript Avanzado', 'autor': 'Maria Lopez', 'isbn': '67890', 'disponible': False}
]

# Creamos la instancia de la clase Biblioteca
biblioteca = Biblioteca(libros)

# Usamos la estrategia de búsqueda por título
estrategia = BusquedaPorTitulo()
resultados = biblioteca.buscar_libro(estrategia, 'Python')  # Buscará sin modificar la lista
print("Resultados por Título:", resultados)

# Usamos la estrategia de búsqueda por disponibilidad
estrategia_disponibilidad = BusquedaPorDisponibilidad()
resultados_disponibles = biblioteca.buscar_libro(estrategia_disponibilidad, True)  # Buscará sin modificar la lista
print("Resultados por Disponibilidad:", resultados_disponibles)