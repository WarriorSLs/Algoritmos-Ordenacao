def heap(lista, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]

        heap(lista, n, maior)

def heap_sort(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heap(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heap(lista, i, 0)

minha_lista = [36, 6, 21, 3, 9, 93, 12]
heap_sort(minha_lista)
print("Lista ordenada: ", minha_lista)


# ---Vantagens---: Complexidade de tempo consistente, o Heap Sort sempre tem uma complexidade de tempo de O(n log n),
# independentemente do tipo de dados de entrada. Isso garante um desempenho consistente, mesmo em casos de pior caso.
# O Heap Sort é um algoritmo de ordenação in-place, o que significa que não requer memória adicional além do array original a ser ordenado.
# Para conjuntos de dados grandes, o Heap Sort geralmente se mostra eficiente devido à sua complexidade de tempo consistente e baixo espaço de memória.

# ---Desvantagens---: Não é um algoritmo estável, o Heap Sort não preserva a ordem relativa de elementos iguais.
# Se dois elementos são iguais, o algoritmo não garante que eles mantenham a mesma ordem original no array ordenado.
# A construção e manutenção do heap podem ser complexas,
# tornando o Heap Sort menos eficiente em pequenos conjuntos de dados em comparação com algoritmos como o Insertion Sort ou o Quicksort.
# E o anel interno do algoritmo do Heap Sort é considerado mais complexo do que o do Quicksort,
# o que pode dificultar a implementação e a compreensão do algoritmo.