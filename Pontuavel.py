from abc import ABC, abstractmethod

class Pontuavel(ABC):
    @abstractmethod
    def calcPontuacao(self):
        pass