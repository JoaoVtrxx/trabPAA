import time
import random
import timeit

def merge_sort_recursive(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort_recursive(arr[:mid])
    right_half = merge_sort_recursive(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

def merge_sort_iterative(arr):
    width = 1
    n = len(arr)
    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]
            arr[i:i + 2 * width] = merge(left, right)
        width *= 2
    return arr


# Gerando um array grande de 10000 elementos
arr = [random.randint(0, 10000) for _ in range(10000)]

# Medindo tempo para a versão recursiva
start = time.time()
merge_sort_recursive(arr.copy())
end = time.time()
print(f"Tempo de execução recursivo: {end - start} segundos")

# Medindo tempo para a versão iterativa
start = time.time()
merge_sort_iterative(arr.copy())
end = time.time()
print(f"Tempo de execução iterativo: {end - start} segundos")


# Medindo a versão recursiva
recursivo_time = timeit.timeit('merge_sort_recursive(arr.copy())', globals=globals(), number=10)
print(f"Tempo de execução recursivo (média de 10 execuções): {recursivo_time / 10} segundos")

# Medindo a versão iterativa
iterativo_time = timeit.timeit('merge_sort_iterative(arr.copy())', globals=globals(), number=10)
print(f"Tempo de execução iterativo (média de 10 execuções): {iterativo_time / 10} segundos")
