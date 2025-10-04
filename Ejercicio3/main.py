# Asegúrate de importar las clases correctas desde los archivos correspondientes
from .repositorio_archivo import RepositorioArchivo
from .repositorio_memoria import RepositorioMemoria

from ejercicio2.servicio_notificaciones import ServicioNotificaciones  # Correcto desde ejercicio2
from ejercicio2.sistema_biblioteca import SistemaBiblioteca  # Correcto desde ejercicio2
from ejercicio2.validador_biblioteca import ValidadorBiblioteca  # Correcto desde ejercicio2


def main():
    # Instanciar las clases
    validador = ValidadorBiblioteca()
    notificador = ServicioNotificaciones()

    # Usar RepositorioArchivo o RepositorioMemoria según sea necesario
    repositorio = RepositorioMemoria()  # Usando el repositorio en memoria
    # repositorio = RepositorioArchivo('biblioteca.txt')  # Alternativamente, usa el repositorio de archivo

    # Inyección de dependencias en SistemaBiblioteca
    sistema = SistemaBiblioteca(repositorio, validador, notificador)

    # Agregar un libro
    libro = {'titulo': 'Crimen y Castigo', 'autor': 'Fyodor Dostoevsky'}
    sistema.agregar_libro(libro)

    # Probar cargar los libros desde el repositorio
    libros = repositorio.cargar()
    print(f"Libros cargados desde el repositorio: {libros}")

# Ejecutar el programa
main()