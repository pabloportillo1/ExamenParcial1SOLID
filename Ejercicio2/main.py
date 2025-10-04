# Importar las clases necesarias
from repositorio_biblioteca import RepositorioBiblioteca
from servicio_notificaciones import ServicioNotificaciones
from sistema_biblioteca import SistemaBiblioteca
from validador_biblioteca import ValidadorBiblioteca

def main():
    # Instanciar las clases
    validador = ValidadorBiblioteca()
    repositorio = RepositorioBiblioteca('biblioteca.txt')
    notificador = ServicioNotificaciones()
    
    # Inyección de dependencias en SistemaBiblioteca
    sistema = SistemaBiblioteca(repositorio, validador, notificador)
    
    # Agregar un libro
    libro = {'titulo': 'Cien Años de Soledad', 'autor': 'Gabriel García Márquez'}
    sistema.agregar_libro(libro)

    # Probar cargar los libros desde el repositorio
    libros = repositorio.cargar()
    print(f"Libros cargados desde el repositorio: {libros}")

# Ejecutar el programa
main()