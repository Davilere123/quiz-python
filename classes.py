from abc import ABC, abstractmethod #Importa, da biblioteca ABC, as funções para criar classes abstratas

#Classe Pergunta --------------------------------------

class Pergunta: #Cria a classe abstrata Pergunta, que vai representar cada pergunta do quiz
    def __init__(self, tipo, enunciado, resposta_correta, alternativa_correta, numero_correto, pontosBase): #Inicia a classe
        self.tipo = tipo
        self._enunciado = enunciado
        self._resposta_correta = resposta_correta
        self._alternativa_correta = alternativa_correta
        self._numero_correto = numero_correto
        self._pontosBase = pontosBase

    #Getters e setters do enunciado
    @property
    def enunciado(self):
        return self._enunciado
    @enunciado.setter
    def enunciado(self, novo_enunciado):
        self._enunciado = novo_anunciado

    #Getters e setter da respota, alternativa e número correto
    @property
    def resposta_correta(self):
        return self._resposta_correta
    @resposta_correta.setter
    def resposta_correta(self, resposta):
        self._resposta_correta = resposta
    
    @property
    def alternativa_correta (self):
        return self._alternativa_correta
    @alternativa_correta.setter
    def alternativa_correta (self, alternativa):
        self._alternativa_correta = alternativa

    @property
    def numero_correto (self):
        return self._numero_correto
    @numero_correto.setter
    def numero_correto (self, numero):
        self._numero_correto = numero

    #Getters e setters da pontuação base
    @property
    def pontosBase (self):
        return self._pontosBase
    @pontosBase.setter
    def pontosBase (self, pontos):
        self._pontosBase = pontos
    
    #Verificação das respostas

    @abstractmethod
    def verificar_resposta(self, resposta): #Verifica se a resposta está correta
        pass
    def verificar_alternativa(self, alternativa): #Verifica se a alternativa está correta
        pass
    def verificar_numero(self, numero): #Verifica se o número está correto
        pass

#--------------------------------
class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, enunciado, resposta_correta, alternativa_correta, numero_correto, alternativas, pontosBase)
        super().__init__(resposta_correta, alternativa_correta, numero_correto, pontosBase)
        self.alternativas = alternativas
    
    def verificar_resposta(self, resposta):
        resposta = resposta.strip().upper()

        for alt in self.alternativas:
            if resposta == alt.upper():
                return alt[0].upper() == self._resposta_correta
        return False
    
    def calcPontuacao(self):
        return self._pontosBase

#--------------------------------
class PerguntaVerdadeiroFalso(Pergunta):
    def __init__(self, enunciado, resposta_correta, alternativa_correta, numero_correto, pontosBase)
        resposta_correta = "V" if resposta_correta else "F"
        alternativa_correta = "VERDADEIRO" if alternativa_correta else "FALSO"
        numero_correto = "1" if numero_correto else "0"

        super().__init__(enunciado, resposta_correta, alternativa_correta, numero_correto, pontosBase)

        def verificar_resposta(self, resposta):

        resposta = resposta.strip().upper()



#Classe Quiz --------------------------------------
    
class Quiz: #Classe gerenciadora do quiz
    def __init__(self, totalJogados):
        self.perguntas = [] #Lista de perguntas

    def adicionar_pergunta(self, pergunta): #Adiciona uma pergunta ao quiz
        self.perguntas.append(pergunta)



#Classe Jogador --------------------------------------

class Jogador: #Classe do jogador
    def __init__(self, nome, pontos):
        self.nome = nome
        self.pontos = pontos
