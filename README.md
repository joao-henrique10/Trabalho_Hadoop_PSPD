# Contagem de Frequência de Palavras com Hadoop e Python

Este guia fornece o passo a passo para configurar e executar um programa de contagem de frequência de palavras no Hadoop utilizando Python. Ele considera um cluster com uma máquina Master e duas Slaves.

---

## **1. Pré-requisitos**
Certifique-se de ter:

- Hadoop instalado e configurado no cluster.
- Uma máquina **Master** e pelo menos duas máquinas **Slave** configuradas corretamente.
- O HDFS (Hadoop Distributed File System) configurado e funcionando.
- O modo **YARN** ativado para execução de jobs no Hadoop.

---

## **2. Scripts Mapper e Reducer**

### **Mapper (mapper.py)**
Este script lê o arquivo de entrada linha por linha, divide em palavras e emite cada palavra com o valor `1`:

```python
#!/usr/bin/env python3
import sys

# Ler dados do stdin
for linha in sys.stdin:
    palavras = linha.strip().split()
    for palavra in palavras:
        # Emitir palavra e contador inicial
        print(f"{palavra}\t1")
```

### **Reducer (reducer.py)**
Este script agrega os valores recebidos do Mapper e calcula a frequência de cada palavra:

```python
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
```

---

## **3. Preparar os Scripts no Cluster**
1. **Copie os scripts** `mapper.py` e `reducer.py` para a máquina Master.
2. Certifique-se de que ambos tenham permissão de execução:
   ```bash
   chmod +x mapper.py reducer.py
   ```

---

## **4. Subir o Arquivo para o HDFS**
O arquivo de entrada (`palavras.txt`) precisa ser enviado para o HDFS.

1. Crie o diretório de entrada no HDFS:
   ```bash
   hdfs dfs -mkdir -p /user/hadoop/input
   ```
2. Envie o arquivo de texto para o HDFS:
   ```bash
   hdfs dfs -put palavras.txt /user/hadoop/input/
   ```

---

## **5. Executar o Job no Cluster**
Use o Hadoop Streaming para executar o job MapReduce com os scripts Python.

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -input /user/hadoop/input/palavras.txt \
    -output /user/hadoop/output/ \
    -mapper "python3 mapper.py" \
    -reducer "python3 reducer.py"
```

### Explicação dos parâmetros:
- **`-input`**: Diretório de entrada no HDFS onde está o arquivo.
- **`-output`**: Diretório onde os resultados serão salvos no HDFS.
- **`-mapper`**: Caminho para o script Mapper em Python.
- **`-reducer`**: Caminho para o script Reducer em Python.

---

## **6. Verificar os Resultados**
Depois que o job for concluído, visualize a saída:

```bash
hdfs dfs -cat /user/hadoop/output/part-00000
```

A saída mostrará as palavras e suas frequências, como:

```
amizade: 476579
casa: 475505
sol: 476059
esperança: 475551
paz: 476115
alegria: 476292
sorriso: 475933
família: 475678
chuva: 477155
rio: 476944
luz: 474687
trabalho: 477185
montanha: 477412
vida: 475947
saúde: 475713
estrela: 475710
flor: 476678
natureza: 475188
felicidade: 476291
pspd: 476770
amor: 476608
```

---

## **7. Configuração de Cluster com Master e Slaves**
1. **Configure o Master**:
   - No arquivo `core-site.xml`, defina o endereço do HDFS do Master.
   - No arquivo `hdfs-site.xml`, configure o número de réplicas e os DataNodes.

2. **Liste os Slaves**:
   - No arquivo `slaves` do Master, adicione os endereços das máquinas Slaves:
     ```
     slave1
     slave2
     ```

3. **Inicie o Hadoop no cluster**:
   ```bash
   start-dfs.sh
   start-yarn.sh
   ```

4. Verifique os DataNodes e NodeManagers no Master acessando a interface web do Hadoop (geralmente disponível em `http://<master-ip>:9870`).

---

## **Resumo do Fluxo**
1. Suba o arquivo de entrada no HDFS.
2. Execute o job Hadoop Streaming no Master.
3. Os Slaves processarão as tarefas do Mapper e Reducer.
4. O resultado final será salvo no HDFS e poderá ser consultado.

---

Com isso, você terá uma contagem de palavras funcional usando Hadoop e Python no seu cluster. Se precisar de ajustes ou ajuda adicional, é só perguntar!
