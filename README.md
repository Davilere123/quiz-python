# Quiz feito em Python
Este é um quiz feito em Python. É parte de uma atividade da matéria de Programação Orientada a Objeto.
Ele foi apelidado de Kahoot 2 como referência aos quizes que o professor realiza em sala utilizando a plataforma Kahoot. Entretanto, ele não possui qualquer intenção de replicar a plataforma.

## Como executar
1 - Baixe o arquivo ZIP deste repositório e extraia em seu computador.  
2 - Dentro da pasta, abra um terminal ou prompt de comando.  
3 - Execute:
```
python main.py
```
  
## Como os conceitos de POO foram aplicados

- **Classe Abstrata**: `Pergunta` é uma classe abstrata (em `classes.py`) que representa a ideia geral das perguntas.  
- **Interface**: `Pontuavel` (`Pontuavel.py`) exige que perguntas implementem o método `calcPontuacao`.  
- **Herança**: `PerguntaMultiplaEscolha` e `PerguntaVerdadeiroFalso` herdam de `Pergunta`.  
- **Polimorfismo**: a lista `quiz.perguntas` armazena objetos de subclasses diferentes e chama os mesmos métodos.  
- **Encapsulamento**: atributos privados com getters/setters (ex.: `Jogador.nome`, `Pergunta.enunciado`).  
- **Validação**: setters validam valores (nome não vazio, pontuação não-negativa, enunciado válido).  
- **Composição**: `Quiz` possui uma lista de `Pergunta` e um `Jogador` (relação de composição).  
- **Atributos/métodos estáticos**: `Quiz.total_quizzes` e `getTotalQuizzesJogos()` demonstram atributos estáticos.  
- **Sobrecarga (simulada)**: `SistemaLogs.registrarEvento` aceita parâmetros opcionais (`nivel` e `contexto`) para simular sobrecarga.  
- **Sobrescrita**: `verificar_resposta` é sobrescrito nas subclasses de `Pergunta`.  
