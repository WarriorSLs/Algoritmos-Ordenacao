def bucket_sort(lista):
    if not lista:
        return []

    max_valor = max(lista)
    min_valor = min(lista)
    bucket_range = (max_valor - min_valor) / len(lista) + 1
    buckets = [[] for _ in range(len(lista))]

    for num in lista:
        index = int((num - min_valor) // bucket_range)
        buckets[index].append(num)

    sorted_list = []
    for bucket in buckets:
        sorted_list.extend(sorted(bucket))

    return sorted_list

minha_lista = [12, 9, 24, 4, 19, 21, 14, 6, 2, 16]
lista_ordenada = bucket_sort(minha_lista)
print("Lista ordenada: ", lista_ordenada)


# ---Vantagens---: Eficiência com distribuição uniforme, quando a distribuição dos dados é uniforme,
# o bucket sort pode ser muito rápido, com tempo de execução linear em alguns casos.
# O conceito do bucket sort é relativamente simples de entender e implementar.
# E a forma como os baldes são ordenados internamente pode ser adaptada para otimizar o desempenho em diferentes cenários.

# ---Desvantagens---: Desempenho ruim com distribuição desigual, se a distribuição dos dados for muito desigual,
# alguns baldes podem conter muitos elementos, comprometendo a eficiência do algoritmo.
# O bucket sort requer espaço de memória extra para os baldes, o que pode ser uma desvantagem em situações com escassez de memória.
# E a escolha do algoritmo de ordenação interna para os baldes pode influenciar o desempenho geral do bucket sort.