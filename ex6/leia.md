## Comparação: Merge Sort Recursivo vs Iterativo

### 1. **Desempenho (Tempo de Execução)**

A **versão recursiva** apresentou um tempo médio de **0,0351 segundos** para 10 execuções.<br>
A **versão iterativa** teve um tempo médio de **0,0361 segundos** para 10 execuções.

Apesar das diferenças serem mínimas, a versão recursiva teve uma leve vantagem em termos de desempenho para um array de 10.000 elementos.<br>
Isso sugere que, para conjuntos de dados moderados, a escolha entre recursivo e iterativo não trará um impacto significativo na performance.

### 2. **Clareza e Elegância**

- **Recursiva:** O código recursivo é mais intuitivo e segue uma abordagem de "dividir e conquistar", tornando-o mais fácil de entender.
- **Iterativa:** O código iterativo elimina o uso da pilha de chamadas, mas é um pouco mais complexo de implementar e pode ser menos claro.

### 3. **Uso de Memória**

- **Recursiva:** Pode apresentar maior consumo de memória devido à profundidade da recursão.<br>
Cada chamada recursiva é armazenada na pilha de chamadas, o que aumenta o uso de memória.
- **Iterativa:** Mais eficiente em termos de uso de memória, pois evita a recursão, utilizando apenas loops.

### Conclusão Geral

A escolha entre recursiva e iterativa depende mais do contexto: se a prioridade é a **legibilidade** do código ou a **eficiência de memória**.
