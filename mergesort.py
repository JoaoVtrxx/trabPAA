def merge_sort(arr, iteration=0):
    if len(arr) > 1:
        mid = len(arr) // 2  # Divide o array no meio
        left_half = arr[:mid]  # Metade esquerda
        right_half = arr[mid:]  # Metade direita

        # Recursivamente chama o merge_sort para as metades
        iteration = merge_sort(left_half, iteration)
        iteration = merge_sort(right_half, iteration)

        i = 0  # contador posição da left_half
        j = 0  # contador posição da right_half
        k = 0  # contador do arr normal
        
        # Enquanto há elementos em ambas as metades
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Se saiu do while e alguma metade ficou com elementos sem ir pro array do nó pai, ele vai adicionando e incrementando o k
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Imprime o estado do array após a fusão das metades
        iteration += 1
        print(f"Iteração {iteration}: {arr}")
        
    return iteration

# Início
arrMedio = [23, 7, 45, 12, 88, 34, 67, 56, 91, 11, 49, 72, 6, 39, 80]
arrMelhor = [6, 7, 11, 12, 23, 34, 39, 45, 49, 56, 67, 72, 80, 88, 91]
arrPior = [91,88,80,72,67,56,49,45,39,34,23,12,11,7,6]
print("\nMelhor caso")
print("Array original:", arrMelhor)
total_iterations = merge_sort(arrMelhor)
print("Total de iterações:", total_iterations)

print("\nCaso Medio")
print("Array original:", arrMedio)
total_iterations = merge_sort(arrMedio)
print("Total de iterações:", total_iterations)

print("\nPior Caso")
print("Array original:", arrPior)
total_iterations = merge_sort(arrPior)
print("Total de iterações:", total_iterations)
