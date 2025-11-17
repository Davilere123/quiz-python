import datetime #Importa biblioteca datetime para registrar os horários
from abc import ABC, abstractmethod #Importa a biblioteca abc para criar classes abstratas

class SistemaLogs:

    @abstractmethod
    def registrarEvento(self, mensagem):
        dataAtual = datetime.datetime.now()
        dataFormatada = dataAtual.strftime("%d/%m/%Y %H:%M:%S")
        print(f"{dataFormatada} - {mensagem}")