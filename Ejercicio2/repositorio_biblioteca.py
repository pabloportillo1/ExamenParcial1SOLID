class RepositorioBiblioteca:
    def __init__(self, archivo):
        self.archivo = archivo

    def guardar(self, libro):
        # Guardar el libro en el archivo
        with open(self.archivo, 'a') as file:
            file.write(f"{libro['titulo']},{libro['autor']}\n")
        print(f"Libro '{libro['titulo']}' guardado exitosamente.")

    def cargar(self):
        libros = []
        with open(self.archivo, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Verifica que la línea no esté vacía
                    partes = line.split(',')
                    if len(partes) == 2:  # Verifica que haya exactamente 2 valores
                        titulo, autor = partes
                        libros.append({'titulo': titulo, 'autor': autor})
                    else:
                        print(f"Formato incorrecto en la línea: {line}")  # Maneja el error
        return libros