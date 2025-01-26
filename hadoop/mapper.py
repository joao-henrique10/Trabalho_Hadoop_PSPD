#!/usr/bin/env python3
import sys

# Ler dados do stdin
for linha in sys.stdin:
    palavras = linha.strip().split()
    for palavra in palavras:
        # Emitir palavra e contador inicial
        print(f"{palavra}\t1")
