#!/usr/bin/env python3
import sys
from collections import defaultdict

# Dicionário para contar as palavras
contagem = defaultdict(int)

# Processar as entradas do stdin
for linha in sys.stdin:
    palavra, valor = linha.strip().split("\t")
    contagem[palavra] += int(valor)

# Emitir os resultados finais
for palavra, freq in contagem.items():
    print(f"{palavra}\t{freq}")
