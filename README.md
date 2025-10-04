# ExamenParcial1SOLID
Ejercicio 1: 



Ejercicio 2: 


Ejercicio 3:



Pregunta 1: LSP (5 pts)
a) (5 pts) Explica qué es LSP y cómo se aplica al ejemplo:
class Usuario:
    def calcular_limite_prestamos(self):
        return 3

class Estudiante(Usuario):
    def calcular_limite_prestamos(self):
        return 3

El Liskov Substitution Principle (LSP) establece que las clases derivadas deben ser intercambiables por sus clases base sin afectar la funcionalidad del sistema. Es decir, si una clase B es una subclase de la clase A, entonces cualquier instancia de A debe poder ser reemplazada por una instancia de B, sin alterar el comportamiento esperado del programa.

b) (5 pts) Da un ejemplo que VIOLE LSP y explica por qué:
# Tu código aquí
class Vehiculo:
    def arrancar(self):
        return "Arrancando el vehículo"

class Coche(Vehiculo):
    def arrancar(self):
        return "Arrancando el coche"

class Bicicleta(Vehiculo):
    def arrancar(self):
        raise Exception("La bicicleta no tiene motor")




# Explicación:

En este caso, la subclase Bicicleta está violando el principio LSP. Aunque Bicicleta hereda de Vehiculo, no puede sustituir a Vehiculo de manera transparente porque lanza una excepción cuando se invoca el método arrancar(), mientras que la clase base Vehiculo y la subclase Coche no lo hacen. Esto crea una inconsistencia en el comportamiento y viola el principio LSP, ya que una instancia de Vehiculo no puede ser reemplazada de manera transparente por Bicicleta sin alterar el comportamiento esperado.

Pregunta 2: ISP (5 pts)

a) (5 pts) ¿Por qué esta interfaz VIOLA ISP?
class IGestionBiblioteca:
    def agregar_libro(self): pass
    def buscar_libro(self): pass
    def realizar_prestamo(self): pass
    def generar_reporte(self): pass
    def hacer_backup(self): pass

Respuesta:

Esta interfaz viola el Interface Segregation Principle (ISP) porque está obligando a las clases que la implementan a depender de métodos que no utilizan. Por ejemplo, una clase que solo se encargue de agregar libros no debería verse obligada a implementar los métodos de generar_reporte o hacer_backup, ya que no son necesarios para su funcionalidad. Según ISP, las interfaces deben ser específicas para que las clases solo implementen los métodos que realmente necesita, evitando que se vean obligadas a implementar funcionalidades innecesarias.


b) (5 pts) Propón cómo segregar esta interfaz:


Interface 1: IAgregarLibro  -   Métodos: agregar_libro()

Interface 2: IBuscarLibro  -  Métodos: buscar_libro()

Interface 3: IPrestamo     -  Métodos: realizar_prestamo()

