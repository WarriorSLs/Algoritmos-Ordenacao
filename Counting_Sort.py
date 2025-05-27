def counting_sort(lista):
    if not lista:
        return []

    min_valor = min(lista)
    max_valor = max(lista)
    range_valor = max_valor - min_valor + 1

    count = [0] * range_valor

    for num in lista:
        count[num - min_valor] += 1

    for i in range(1, range_valor):
        count[i] += count[i - 1]

    output = [0] * len(lista)
    for i in range(len(lista) - 1, -1, -1):
        output[count[lista[i] - min_valor] - 1] = lista[i]
        count[lista[i] - min_valor] -= 1

    return output

minha_lista = [4, 2, 2, 8, 3, 3, 1]
lista_ordenada = counting_sort(minha_lista)
print("Lista ordenada: ", lista_ordenada)


# ---Vantagens---: Rápido e eficiente, o Counting Sort tem uma complexidade de tempo de O(n + k),
# onde n é o número de elementos e k é o intervalo de valores,
# tornando-o eficiente para conjuntos de dados com um intervalo limitado de valores.
# O algoritmo é relativamente simples de entender e implementar.
# O Counting Sort é estável, o que significa que a ordem relativa de elementos iguais é preservada durante a ordenação.
# E o Counting Sort funciona bem com números inteiros e é especialmente útil quando o intervalo de valores é pequeno.

# ---Desvantagens---: Requer espaço adicional, o algoritmo utiliza espaço adicional para armazenar o array de contagem,
# o que pode ser uma desvantagem em situações onde o espaço é limitado. 
# O Counting Sort foi originalmente projetado para trabalhar com inteiros não negativos e não funciona com números negativos ou decimais.
# E O Counting Sort se torna menos eficiente quando o intervalo de valores (k) é muito grande em relação ao número de elementos (n),
# pois a complexidade de espaço e tempo aumentam. 