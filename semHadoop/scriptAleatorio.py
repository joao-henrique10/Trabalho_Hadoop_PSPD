import random

# Lista de palavras em português
palavras = [
    "amor", "amizade", "casa", "felicidade", "natureza", "sol", "chuva",
    "flor", "montanha", "rio", "vida", "saúde", "alegria", "esperança",
    "sorriso", "trabalho", "família", "paz", "luz", "estrela", "pspd"
]

# Gerar 100 palavras aleatórias
with open("palavras.txt", "w") as arquivo:
    for _ in range(10000000):
        arquivo.write(random.choice(palavras) + "\n")

print("Arquivo 'palavras.txt' gerado com sucesso!")
