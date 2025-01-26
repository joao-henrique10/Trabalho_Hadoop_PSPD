from collections import Counter

# Ler o arquivo e contar as palavras
with open("../palavras.txt", "r") as file:
    words = file.read().splitlines()

# Contar frequências com Counter
word_counts = Counter(words)

# Exibir resultados
print("Frequência de Palavras:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
