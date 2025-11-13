#Importações e outros preparos
from elementos import Pergunta, Quiz, Jogador #Importa as classes
import time #Importa biblioteca "time" para dar um "tempo" em algumas partes do jogo

#As perguntas do jogo
pergunta1 = Pergunta(
    "O que significa POO?",
    ["A) Proogramação", "B) Programação Orientada a Objeto", "C) Programação Offline e Online", "D) Programação Online e Offline"],
    "B",
    "PROGRAMAÇÃO ORIENTADA A OBJETO",
    "2"
)

pergunta2 = Pergunta(
    "Qual a cor do céu em um dia claro?",
    ["A) Azul", "B) Verde", "C) Vermelho", "D) Amarelo"],
    "A",
    "AZUL",
    "1"
)

pergunta3 = Pergunta (
    "O Python é uma linguagem de programação de alto nível",
    ["V) Verdadeiro", "F) Falso"],
    "V",
    "VERDADEIRO",
    "1"
)

pergunta4 = Pergunta (
    "HTML é uma linguagem de programação",
    ["V) Verdadeiro", "F) Falso"],
    "F",
    "FALSO",
    "2"
)

quiz = Quiz() #Atribui a classe quiz e suas funções a variável quiz

#Adiciona perguntas
quiz.adicionar_pergunta(pergunta1)
quiz.adicionar_pergunta(pergunta2)
quiz.adicionar_pergunta(pergunta3)
quiz.adicionar_pergunta(pergunta4)

# O quiz

print("Quiz - Kahoot 2")
print("Bem-vindo ao \"\"Kahoot 2\"\"!")
print("=" * 10)
print("")

jogador = Jogador(input("Qual o seu nome? -> "), 0) #Atribui a classe Jogador e suas funções a variavel jogador

print("=" * 10)
print("")

print(f"Beleza, {jogador.nome}! Vamos começar!") #Alerta o jogador que o jogo vai começar

time.sleep(2)
print("")

for pergunta in quiz.perguntas: #Loop para cada pergunta
    print(pergunta.enunciado) #Imprime a pergunta

    for opcao in pergunta.opcoes: #Percorre as alternativas
        print(opcao) #Imprime cada alternativa
    print("")

    resposta = input("Digite a alternativa correta: ").strip().upper() #Recebe a resposta do usuário
    print("")

    if pergunta.verificar_resposta(resposta): #Verifica se a resposta (digitada por extenso) está correta
        print("Resposta correta!")
        jogador.pontos += 1

    elif pergunta.verificar_alternativa(resposta): #Verifica se a alternativa (letra) está correta
        print("Resposta correta!")
        jogador.pontos += 1

    elif pergunta.verificar_numero(resposta): #Verifica se a alternativa (número) está correta
        print("Resposta correta!")
        jogador.pontos += 1 #adiciona +1 na pontuação (o mesmo vale para as outras)

    else: #Se errar
        print(f"Resposta incorreta. A resposta correta é: {pergunta.resposta_correta}")
        
    print("")
    print(f"Sua pontuação atual é de {jogador.pontos} pontos!")
    print("-" * 10)
    print("")
    time.sleep(2)

#Depois do quiz

print(f"Sua pontuação final é: {jogador.pontos} de {len(quiz.perguntas)}") #mostra quanto o usuário acertou e o total de perguntas

#mensagens para alegrar (ou não) o usuário
if jogador.pontos < len(quiz.perguntas) / 2: #se o usuário fez menos que a metade (foi ruim)
    print(f"Desculpa {jogador.nome}, mas... você foi péssimo :(")

elif len(quiz.perguntas) / 2 <= jogador.pontos < len(quiz.perguntas) / 1.5: #se o usuário fez entre a metade e /1.5 (foi mediano)
    print("Você foi... meh :|")

else: #se o usuário mais (foi bom)
    print(f"Boa {jogador.nome}!! :D")
