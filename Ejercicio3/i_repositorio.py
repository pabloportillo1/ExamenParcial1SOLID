from abc import ABC, abstractmethod

class IRepositorio(ABC):
    @abstractmethod
    def guardar(self, libro):
        pass

    @abstractmethod
    def cargar(self):
        pass