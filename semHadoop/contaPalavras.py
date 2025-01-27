from collections import Counter

# Criar um contador vazio
word_counts = Counter()

# Ler o arquivo em blocos
with open("palavras.txt", "r") as file:
    for line in file:
        words = line.strip().split()
        word_counts.update(words)  # Atualiza o contador apenas com o bloco atual

# Exibir resultados
print("Frequência de Palavras:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
