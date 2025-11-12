#Importações e outros preparos
from elementos import Pergunta, Quiz

pergunta1 = Pergunta(
    "Qual o nome da faculdade?",
    ["A) CESMAC", "B) UNIMA", "C) UFAL", "D) UNINASSAU"],
    "D",
    "UNINASSAU",
    "4"
)
pergunta2 = Pergunta(
    "Qual a cor do céu em um dia claro?",
    ["A) Azul", "B) Verde", "C) Vermelho", "D) Amarelo"],
    "A",
    "AZUL",
    "1"
)

quiz = Quiz()
quiz.adicionar_pergunta(pergunta1)
quiz.adicionar_pergunta(pergunta2)

# O quiz

print("Quiz - Kahoot 2")
print("Bem-vindo ao \"\"Kahoot 2\"\"!")
print("=" * 10)

for pergunta in quiz.perguntas: #Loop para cada pergunta
    print(pergunta.enunciado) #Imprime a pergunta
    for opcao in pergunta.opcoes: #Percorre as alternativas
        print(opcao) #Imprime cada alternativa
    
    resposta = input("Digite a alternativa correta: ").strip().upper() #Recebe a resposta do usuário
    
    if pergunta.verificar_resposta(resposta): #Verifica se a resposta (digitada por extenso) está correta
        print("Resposta correta!")
        quiz.pontuacao += 1
    elif pergunta.verificar_alternativa(resposta): #Verifica se a alternativa (letra) está correta
        print("Resposta correta!")
        quiz.pontuacao += 1
    elif pergunta.verificar_numero(resposta): #Verifica se a alternativa (número) está correta
        print("Resposta correta!")
        quiz.pontuacao += 1 #adiciona +1 na pontuação (o mesmo vale para as outras)
    else: #Se errar
        print(f"Resposta incorreta. A resposta correta é: {pergunta.resposta_correta}")
    print("-" * 10)

#Depois do quiz

print(f"Sua pontuação final é: {quiz.pontuacao} de {len(quiz.perguntas)}") #mostra quanto o usuário acertou e o total de perguntas

#mensagens para alegrar (ou não) o usuário
if quiz.pontuacao < 5: #se o usuário fez menos que 5 (foi ruim)
    print("Desculpa, mas... você foi péssimo :(")
elif 5 <= quiz.pontuacao < 8: #se o usuário fez entre 5 e 7 (foi mediano)
    print("Você foi... meh :|")
else: #se o usuário fez 8 ou mais (foi bom)
    print("Boa!! :D")