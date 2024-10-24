import time
start_time = time.time()
def bubble_sort(arr):
    iter = 0;
    print("Array inicial:", arr)
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                iter = iter+1
                print("Iteração %d: %s"%(iter, arr))
    return arr
##arrMedio = [11,12,22,90,34,25,64]
##arrMelhor = [11, 12, 22, 25, 34, 64, 90]
##arrPior = [90, 64, 34, 25, 22, 12, 11]

arrMedio = [23, 7, 45, 12, 88, 34, 67, 56, 91, 11, 49, 72, 6, 39, 80]
arrMelhor = [6, 7, 11, 12, 23, 34, 39, 45, 49, 56, 67, 72, 80, 88, 91]
arrPior = [91,88,80,72,67,56,49,45,39,34,23,12,11,7,6]

print("\nMelhor caso")
start_time = time.time()
sorted_arr = bubble_sort(arrMelhor)
end_time = time.time()
execution_time = end_time - start_time
print(f"Tempo de execução: {execution_time} segundos")

print("\nCaso medio")
start_time = time.time()
sorted_arr = bubble_sort(arrMedio)
end_time = time.time()
execution_time = end_time - start_time
print(f"Tempo de execução: {execution_time} segundos")

print("\n Pior Caso")
start_time = time.time()
sorted_arr = bubble_sort(arrPior)
end_time = time.time()
execution_time = end_time - start_time
print(f"Tempo de execução: {execution_time} segundos")

print("Array ordenado:", sorted_arr)
