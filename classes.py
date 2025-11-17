from abc import ABC, abstractmethod #Importa, da biblioteca ABC, as funções para criar classes abstratas
from Pontuavel import Pontuavel

#Classe Pergunta --------------------------------------

class Pergunta(Pontuavel, ABC):
    """Abstração da ideia de pergunta.

    Todos os atributos ficam privados (com validação nos setters)
    para aplicar encapsulamento.
    """
    def __init__(self, tipo, enunciado, alternativas, resposta_correta, resposta_extenso, pontosBase):
        # tipo: 'multiple' ou 'vf' (manter compatibilidade com main.py)
        self._tipo = tipo
        self.enunciado = enunciado
        self.alternativas = alternativas or []
        self.resposta_correta = resposta_correta
        self.resposta_extenso = resposta_extenso
        # aceita pontosBase como string (vindo do main) ou int
        try:
            pontos = int(pontosBase)
        except Exception:
            pontos = 1
        self.pontosBase = pontos

    #Getter e setter do tipo
    @property
    def tipo(self):
        return self._tipo

    #Getter e setter do enunciado
    @property
    def enunciado(self):
        return self._enunciado

    @enunciado.setter
    def enunciado(self, novo_enunciado):
        if not novo_enunciado or not str(novo_enunciado).strip():
            raise ValueError("Enunciado inválido")
        self._enunciado = str(novo_enunciado).strip()

    #Getter e setter da resposta correta
    @property
    def resposta_correta(self):
        return self._resposta_correta

    @resposta_correta.setter
    def resposta_correta(self, resposta):
        if resposta is None:
            raise ValueError("Resposta correta inválida")
        # mantém como letra maiúscula quando aplicável
        self._resposta_correta = str(resposta).strip().upper()

    #Getter e setter da resposta correta (por extenso)
    @property
    def resposta_extenso(self):
        return self._resposta_extenso

    @resposta_extenso.setter
    def resposta_extenso(self, valor):
        self._resposta_extenso = str(valor).strip() if valor is not None else ""

    #Getter e setter da pontuação base da pergunta
    @property
    def pontosBase(self):
        return self._pontosBase

    @pontosBase.setter
    def pontosBase(self, pontos):
        pontos_int = int(pontos)
        if pontos_int <= 0:
            raise ValueError("Pontuação base deve ser maior que 0")
        self._pontosBase = pontos_int

    # Métodos de verificação básicos (podem ser sobrescritos)
    @abstractmethod
    def verificar_resposta(self, resposta):
        pass

    def verificar_alternativa(self, alternativa):
        #Verifica se a alternativa (letra) está correta
        if not alternativa:
            return False
        alt = str(alternativa).strip().upper()
        return alt == self.resposta_correta

    def verificar_numero(self, numero):
        #Verifica se o número corresponde à alternativa correta
        if not numero:
            return False
        try:
            idx = int(str(numero).strip()) - 1
        except Exception:
            return False
        if idx < 0 or idx >= len(self.alternativas):
            return False
        
        alt_text = self.alternativas[idx]
        letra = alt_text.strip()[0].upper()
        return letra == self.resposta_correta

#--------------------------------
class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, tipo, enunciado, alternativas, resposta_correta, resposta_extenso, pontosBase):
        super().__init__(tipo, enunciado, alternativas, resposta_correta, resposta_extenso, pontosBase)

    def verificar_resposta(self, resposta):
        #Aceita letra, texto completo da alternativa ou número
        if not resposta:
            return False
        r = str(resposta).strip()
        #letra
        if len(r) == 1 and r.isalpha():
            return self.verificar_alternativa(r)
        #número
        if r.isdigit():
            return self.verificar_numero(r)
        #texto completo
        for alt in self.alternativas:
            if r.upper() == alt.upper() or r.upper() == alt[3:].strip().upper():
                return alt[0].upper() == self.resposta_correta
        return False

    def calcPontuacao(self):
        return self.pontosBase

#--------------------------------
class PerguntaVerdadeiroFalso(Pergunta):
    def __init__(self, tipo, enunciado, alternativas, resposta_correta, resposta_extenso, pontosBase):
        # resposta_correta pode vir como V/F ou booleano
        resp = str(resposta_correta).strip().upper()
        if resp in ["V", "VERDADEIRO", "TRUE", "1"]:
            resp = "V"
        else:
            resp = "F"
        super().__init__(tipo, enunciado, alternativas, resp, resposta_extenso, pontosBase)

    def verificar_resposta(self, resposta):
        if not resposta:
            return False
        r = str(resposta).strip().upper()
        if r in ["V", "VERDADEIRO", "TRUE", "1"]:
            return self.resposta_correta == "V"
        if r in ["F", "FALSO", "FALSE", "2"]:
            return self.resposta_correta == "F"
        return False

    def calcPontuacao(self):
        return max(1, self.pontosBase // 2)



#Classe Quiz --------------------------------------
class Quiz:
    #Classe gerenciadora do quiz.

    #Mantém uma lista de perguntas (composição) e um contador estático
    #do total de quizzes criados/executados

    total_quizzes = 0

    def __init__(self, totalJogados=0):
        self.perguntas = [] #Lista de perguntas (composição)
        Quiz.total_quizzes += 1

    @staticmethod
    def getTotalQuizzesJogos():
        return Quiz.total_quizzes

    def adicionar_pergunta(self, pergunta): #Adiciona uma pergunta ao quiz
        self.perguntas.append(pergunta)



#Classe Jogador --------------------------------------

class Jogador: #Classe do jogador com encapsulamento
    def __init__(self, nome, pontos=0):
        self.nome = nome
        self.pontos = pontos

    #Getter e setter do nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("Nome inválido")
        self._nome = str(valor).strip()

    #Getter e setter da pontuação do jogador
    @property
    def pontos(self):
        return self._pontos

    @pontos.setter
    def pontos(self, valor):
        v = int(valor)
        if v < 0:
            raise ValueError("Pontuação não pode ser negativa")
        self._pontos = v

    #Função para adicionar os pontos do jogador
    def adicionar_pontos(self, pontos):
        if int(pontos) < 0:
            raise ValueError("Pontos inválidos")
        self._pontos += int(pontos)
