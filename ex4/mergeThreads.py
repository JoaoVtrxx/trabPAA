import threading

# Função para mesclar duas sublistas ordenadas
def merge(left, right):
    sorted_list = []
    i = j = 0

    # Comparar os elementos e mesclar as listas
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Adicionar os elementos restantes de cada lista
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

# Função Merge Sort paralela
def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Dividir o array ao meio
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Criar threads para ordenar as sublistas em paralelo
    left_thread = threading.Thread(target=lambda l: l.append(parallel_merge_sort(left)), args=([],))
    right_thread = threading.Thread(target=lambda r: r.append(parallel_merge_sort(right)), args=([],))

    # Iniciar as threads
    left_thread.start()
    right_thread.start()

    # Esperar as threads finalizarem
    left_thread.join()
    right_thread.join()

    # Mesclar as listas ordenadas
    return merge(left, right)

# Exemplo de uso
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print(f"Array original: {arr}")
    sorted_arr = parallel_merge_sort(arr)
    print(f"Array ordenado: {sorted_arr}")
