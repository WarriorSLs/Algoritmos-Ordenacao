def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for s in range(i+1, n):
            if lista[s] < lista[indice_minimo]:
                indice_minimo = s

        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

minha_lista = [5, 1, 10, 7, 3, 2, 8, 6, 4, 9]
selection_sort(minha_lista)
print ("Lista ordenada: ", minha_lista)


# ---Vantagens---: A facilidade de implementação, o Selection Sort é um algoritmo muito simples de entender e implementar,
# o que o torna ideal para aprender conceitos básicos de ordenação.
# Requer um número menor de trocas (ou operações de memória) em comparação com alguns outros algoritmos,
# o que pode ser vantajoso em situações específicas.
# E é um dos algoritmos mais rápidos para ordenar pequenos vetores. 

# ---Desvantagens---: É lento para grandes conjuntos: A complexidade quadrática O(n²) do Selection Sort
# significa que seu tempo de execução aumenta proporcionalmente ao quadrado do número de elementos a serem ordenados,
# tornando-o muito lento para grandes listas.
# Comparado a algoritmos como Quick Sort, que têm complexidade O(n log n), o Selection Sort é significativamente menos eficiente.
# E dependendo da implementação, o Selection Sort pode não ser estável, o que significa que ele pode alterar a ordem relativa de elementos iguais.