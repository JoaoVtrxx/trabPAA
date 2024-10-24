import time
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Divide o array no meio
        left_half = arr[:mid]  # Metade esquerda
        right_half = arr[mid:]  # Metade direita

        # Recursivamente chama o merge_sort para as metades
        merge_sort(left_half)
        merge_sort(right_half)

        i =  0 # contador posicao da left_half
        j = 0   # contador posicao da right_half
        k = 0   # contador do arr normal
        
        # o contador das duas metades deve ser menor que o tamanho delas
        # compara o valor das metades apontadas por i e j e coloca na ordem para o array do nó pai 
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # se saiu do while e alguma metade ficou com elementos sem ir pro array do nó pai ele vai adicionando e incrmentando o k
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

def measure_sort_time(arr):
    start_time = time.time()
    merge_sort(arr)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Tempo de execução: {duration:.6f} segundos")
    return duration

# inicio
start_time = time.time()


arrMelhor = list(range(1, 1001))  

arrPior = list(range(1001, 1, -1))  

arrMedio = random.sample(range(1, 1001), 1000)  

# print("\nMelhor Caso (ordenado):")
# measure_sort_time(arrMelhor)

# print("\nCaso Médio (aleatório):")
# measure_sort_time(arrMedio)

print("\nPior Caso (decrescente):")
measure_sort_time(arrPior)
