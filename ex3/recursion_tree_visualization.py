import matplotlib.pyplot as plt
import networkx as nx

# Função MergeSort com visualização
def merge_sort(arr, depth=0, parent_node=None, graph=None, node_counter=[0]):
    current_node = node_counter[0]
    graph.add_node(current_node, label=str(arr))
    node_counter[0] += 1

    if parent_node is not None:
        graph.add_edge(parent_node, current_node)

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid], depth + 1, current_node, graph, node_counter)
    right_half = merge_sort(arr[mid:], depth + 1, current_node, graph, node_counter)

    # Mesclando os subarrays
    merged_array = merge(left_half, right_half)
    return merged_array

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


# Função para desenhar a árvore de recursão
def draw_recursion_tree(graph):
    pos = hierarchy_pos(graph)
    labels = nx.get_node_attributes(graph, 'label')

    plt.figure(figsize=(12, 8))
    nx.draw(graph, pos, with_labels=True, labels=labels, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
    plt.title('Árvore de Recursão do Merge Sort')
    plt.show()

def hierarchy_pos(G):
    pos = _hierarchy_pos(G, root=list(G.nodes())[0], width=1.0, vert_gap=0.5, xcenter=0.5)
    return pos


def _hierarchy_pos(G, root, pos=None, parent=None, width=1.0, vert_gap=0.5, xcenter=0.5):
    if pos is None:
        pos = {root: (xcenter, 0)}  # Inicializa a posição da raiz no centro (xcenter)
    else:
        pos[root] = (xcenter, pos[parent][1] - vert_gap)  # Posiciona os filhos verticalmente mais abaixo

    children = list(G.successors(root))
    if len(children) != 0:
        dx = width / len(children)  # Espaçamento horizontal
        next_x = xcenter - width / 2 - dx / 2  # Inicia o próximo filho à esquerda

        for child in children:
            next_x += dx
            pos = _hierarchy_pos(G, child, pos=pos, parent=root, width=dx, vert_gap=vert_gap, xcenter=next_x)

    return pos


# Array de exemplo para ordenar
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]

    # Criando o grafo e iniciando o MergeSort
    G = nx.DiGraph()
    merge_sort(arr, graph=G)

    # Desenhando a árvore de recursão
    draw_recursion_tree(G)

