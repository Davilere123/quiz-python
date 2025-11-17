from abc import ABC, abstractmethod #Importa, da biblioteca ABC, as funções para criar classes abstratas e interfaces

class Pontuavel(ABC): #Cria a interface Pontuavel
    @abstractmethod
    def calcPontuacao(self):
        pass