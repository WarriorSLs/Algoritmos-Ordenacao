def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        s = i - 1
        while s >= 0 and chave < lista[s]:
            lista[s + 1] = lista[s]
            s -= 1
        lista[s + 1] = chave

minha_lista = [34, 11, 54, 8, 2, 5]
insertion_sort(minha_lista)
print ("Lista ordenada: ", minha_lista)


# ---Vantagens---: É simples, fácil de entender e implementar, tornando-o uma boa opção para estudantes e projetos de menor escala.
# Desempenha bem com listas pequenas e também com listas quase ordenadas, pois o custo de inserção de um novo elemento é linear nesse caso.
# Mantém a ordem relativa de elementos iguais, o que é importante em algumas aplicações.
# É um algoritmo "in-place", ou seja, não requer memória adicional para realizar a ordenação.
# E é eficiente para adicionar novos elementos a uma lista já ordenada, pois apenas precisa verificar a posição correta para o novo elemento.

# ---Desvantagens---: Desempenho ruim para grandes listas, sua complexidade de tempo é O(n²),
# o que significa que o tempo de execução aumenta significativamente com o tamanho da lista,
# tornando-o ineficiente para grandes quantidades de dados.
# Em listas completamente desordenadas,
# o insertion sort pode ser mais lento do que outros algoritmos de ordenação mais eficientes, como merge sort ou quick sort.
# Mesmo para listas quase ordenadas, o insertion sort pode ser mais lento do que algoritmos como shell sort.