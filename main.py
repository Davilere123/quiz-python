#Importações e outros preparos
from classes import Pergunta, PerguntaMultiplaEscolha, PerguntaVerdadeiroFalso, Quiz, Jogador #Importa as classes
from SistemaLogs import SistemaLogs
from Pontuavel import Pontuavel
import time #Importa biblioteca "time" para dar um "tempo" em algumas partes do jogo

#-------------------------------

#As perguntas do jogo
pergunta1 = PerguntaMultiplaEscolha(
    "multiple",
    "O que significa POO?",
    ["A) Proogramação", "B) Programação Orientada a Objeto", "C) Programação Offline e Online", "D) Programação Online e Offline"],
    "B",
    "PROGRAMAÇÃO ORIENTADA A OBJETO",
    "2"
)

pergunta2 = PerguntaMultiplaEscolha(
    "multiple",
    "Qual a cor do céu em um dia claro?",
    ["A) Azul", "B) Verde", "C) Vermelho", "D) Amarelo"],
    "A",
    "AZUL",
    "1"
)

pergunta3 = PerguntaVerdadeiroFalso(
    "vf",
    "O Python é uma linguagem de programação de alto nível",
    ["V) Verdadeiro", "F) Falso"],
    "V",
    "VERDADEIRO",
    "1"
)

pergunta4 = PerguntaVerdadeiroFalso(
    "vf",
    "HTML é uma linguagem de programação",
    ["V) Verdadeiro", "F) Falso"],
    "F",
    "FALSO",
    "2"
)

#--------------------------

#Cria o ranking (nome -> melhor pontuação)
ranking = {}

#--------------------------

#Funções do menu
def iniciarJogo(jogador, quiz_obj):
    print(f"Beleza, {jogador.nome}! Vamos começar!") #Alerta o jogador que o jogo vai começar
    time.sleep(2)
    print("")

    for pergunta in quiz_obj.perguntas: #Loop para cada pergunta

        if pergunta.tipo == "multiple":
            print("Pergunta de Múltipla Escolha!")
            print("")
            time.sleep(0.5)
            print(pergunta.enunciado) #Imprime a pergunta

            for alternativa in pergunta.alternativas: #Percorre as alternativas
                print(alternativa) #Imprime cada alternativa

            print("")

        elif pergunta.tipo == "vf":
            print("Pergunta de Verdadeiro ou Falso")
            print("")
            time.sleep(0.5)
            print(pergunta.enunciado) #Imprime a pergunta

            for alternativa in pergunta.alternativas:
                print(alternativa)

            print("")

        resposta = input("Digite a alternativa correta: ").strip().upper() #Recebe a resposta do usuário
        print("")

        #calcula os pontos da pergunta via método da pergunta
        try:
            pontos_pergunta = pergunta.calcPontuacao()
        except Exception:
            #fallback para 1 ponto caso não exista
            pontos_pergunta = 1

        if pergunta.verificar_resposta(resposta): #Verifica se a resposta (digitada por extenso) está correta
            print("Resposta correta!")
            jogador.adicionar_pontos(pontos_pergunta)
            SistemaLogs.registrarEvento(f"Pergunta respondida - correta | Jogador: {jogador.nome}", nivel=200)

        elif pergunta.verificar_alternativa(resposta): #Verifica se a alternativa (letra) está correta
            print("Resposta correta!")
            jogador.adicionar_pontos(pontos_pergunta)
            SistemaLogs.registrarEvento(f"Pergunta respondida - correta (alternativa) | Jogador: {jogador.nome}", nivel=200)

        elif pergunta.verificar_numero(resposta): #Verifica se a alternativa (número) está correta
            print("Resposta correta!")
            jogador.adicionar_pontos(pontos_pergunta) #adiciona pontos da pergunta
            SistemaLogs.registrarEvento(f"Pergunta respondida - correta (número) | Jogador: {jogador.nome}", nivel=200)

        else: #Se errar
            print(f"Resposta incorreta. A resposta correta é: {pergunta.resposta_correta}")
            SistemaLogs.registrarEvento(f"Pergunta respondida - incorreta | Jogador: {jogador.nome}", nivel=400)
            
        print("")
        print(f"Sua pontuação atual é de {jogador.pontos} pontos!")
        print("-" * 10)
        print("")
        time.sleep(2)

    #Depois do quiz

    print(f"Sua pontuação final é: {jogador.pontos} de {len(quiz_obj.perguntas)}") #mostra quanto o usuário acertou e o total de perguntas

    #atualiza ranking (mantém o melhor score por nome)
    prev = ranking.get(jogador.nome)
    if prev is None or jogador.pontos > prev:
        ranking[jogador.nome] = jogador.pontos

    #Exibe total de quizzes (contador estático)
    print(f"Total de quizzes criados: {Quiz.getTotalQuizzesJogos()}")
    SistemaLogs.registrarEvento(f"Quiz finalizado | Jogador: {jogador.nome} | Pontos: {jogador.pontos}", nivel=300)

    #mensagens para alegrar (ou não) o usuário
    if jogador.pontos < len(quiz_obj.perguntas) / 2: #se o usuário fez menos que a metade (foi ruim)
        print(f"Desculpa {jogador.nome}, mas... você foi péssimo :(")

    elif len(quiz_obj.perguntas) / 2 <= jogador.pontos < len(quiz_obj.perguntas): #se o usuário fez entre a metade e o total (foi mediano)
        print("Você foi... meh :|")

    else: #se o usuário fez uma pontuação boa
        print(f"Boa {jogador.nome}!! :D")


def mostrarRanking():
    if not ranking: #se o ranking for nulo
        print("Nenhum jogador registrado ainda.")
        print("")
        return
    
    print("\n===== RANKING =====")
    sorted_rank = sorted(ranking.items(), key=lambda x: x[1], reverse=True) #Classifica o ranking
    for i, (nome, pts) in enumerate(sorted_rank, start=1): #loop para exibir os nomes e pontuações
        print(f"{i}) {nome} - {pts} pontos")
    print("===================\n")


def menuPrincipal():
    while True: #loop para o programa só encerrar quando o usuário escolher
        print("\n=========== MENU DO QUIZ ===========")
        print("1) Iniciar jogo")
        print("2) Ver ranking de jogadores")
        print("3) Ver o número total de quizzes jogados")
        print("4) Sair")
        print("====================================")
        opcao = input("Escolha uma opção: ").strip()  #Recebe a opção que o usuário escolheu
        print("")

        if opcao == "1": #O usuário escolhe jogar
            nome = input("Quem vai jogar? (digite o nome do jogador atual) ->  ").strip() #Recebe o nome
            jogador = Jogador(nome, 0) #Cria o jogador com o nome dado e pontuação 0

            #cria um novo Quiz
            quiz = Quiz()

            #Adiciona as perguntas
            quiz.adicionar_pergunta(pergunta1)
            quiz.adicionar_pergunta(pergunta2)
            quiz.adicionar_pergunta(pergunta3)
            quiz.adicionar_pergunta(pergunta4)

            #Começa o jogo
            iniciarJogo(jogador, quiz)

        elif opcao == "2": #O usuário escolhe mostrar o ranking
            mostrarRanking()
            time.sleep(2)

        elif opcao == "3": #O usuário escolhe ver o total de quizzes já jogados
            print(f"Total de quizzes jogados: {Quiz.getTotalQuizzesJogos()}")
            time.sleep(2)

        elif opcao == "4": #O usuário escolhe sair
            print("Saindo...")
            time.sleep(1)
            break

        else: #O usuário escolheu algo que não existe
            print("Opção inválida")
            time.sleep(2)

#-----------------------

#Inicia o menu do quiz

if __name__ == "__main__":
    print("Quiz - Kahoot 2")
    print("Bem-vindo ao \"\"Kahoot 2\"\"!")
    print("=" * 10)
    menuPrincipal()
