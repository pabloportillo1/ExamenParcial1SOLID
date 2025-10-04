class SistemaBiblioteca:
    def __init__(self, repositorio, validador, notificador):
        # Inyección de dependencias
        self.repositorio = repositorio
        self.validador = validador
        self.notificador = notificador

    def agregar_libro(self, libro):
        try:
            self.validador.validar_libro(libro)  # Validar el libro antes de agregarlo
            self.repositorio.guardar(libro)  # Guardar el libro en el repositorio
            self.notificador.enviar_notificacion(f"El libro '{libro['titulo']}' ha sido agregado.")
        except ValueError as e:
            print(f"Error: {e}")