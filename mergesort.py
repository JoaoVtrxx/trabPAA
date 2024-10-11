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

# inicio
arr = [5, 4, 3, 2, 1]
merge_sort(arr)
print("Array ordenado:", arr)
