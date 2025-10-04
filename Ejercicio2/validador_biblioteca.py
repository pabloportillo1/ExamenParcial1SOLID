class ValidadorBiblioteca:
    def validar_libro(self, libro):
        # Validación para asegurar que el libro tiene un título y autor
        if not libro.get('titulo') or not libro.get('autor'):
            raise ValueError('El libro debe tener título y autor')
        print(f"Libro '{libro['titulo']}' validado correctamente.")