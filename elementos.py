class Pergunta: #Cria a classe Pergunta, que vai representar cada pergunta do quiz
    def __init__(self, enunciado, opcoes, resposta_correta, alternativa_correta, numero_correto): #Inicia a classe
        self.enunciado = enunciado
        self.opcoes = opcoes
        self.resposta_correta = resposta_correta
        self.alternativa_correta = alternativa_correta
        self.numero_correto = numero_correto

    def verificar_resposta(self, resposta): #Verifica se a resposta está correta
        return resposta == self.resposta_correta
    def verificar_alternativa(self, alternativa): #Verifica se a alternativa está correta
        return alternativa.upper() == self.alternativa_correta.upper()
    def verificar_numero(self, numero): #Verifica se o número está correto
        return numero == self.numero_correto
    
class Quiz: #Classe gerenciadora do quiz
    def __init__(self):
        self.perguntas = [] #Lista de perguntas
        self.pontuacao = 0 #Pontuação do jogador

    def adicionar_pergunta(self, pergunta): #Adiciona uma pergunta ao quiz
        self.perguntas.append(pergunta)