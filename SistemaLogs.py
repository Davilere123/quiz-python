import datetime #Importa biblioteca datetime para registrar os horários

class SistemaLogs:
    #lasse utilitária para registrar eventos do jogo.

    #Implementa uma 'sobrecarga' simples através de parâmetros opcionais:
    #mensagem (obrigatório)
    #nivel (opcional): código/nível do evento
    # contexto (opcional): onde ocorreu o evento

    @staticmethod
    def registrarEvento(mensagem, nivel=None, contexto=None):
        agora = datetime.datetime.now()
        horario = agora.strftime("%d/%m/%Y %H:%M:%S")
        linha = f"{horario} - {mensagem}"
        if nivel is not None:
            linha += f" (NIVEL={nivel})"
        if contexto is not None:
            linha += f" [{contexto}]"
        print(linha)