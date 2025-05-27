def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = 0
    s = 0

    while i < len(esquerda) and s < len(direita):
        if esquerda[i] <= direita[s]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[s])
            s += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[s:])
    return resultado

minha_lista = [38, 27, 43, 3, 9, 82, 10]
lista_ordenada = merge_sort(minha_lista)
print ("Lista ordenada: ", lista_ordenada)


# ---Vantagens---: Eficiência, o Merge Sort tem uma complexidade de tempo de O(n log n) para todos os casos (melhor, pior e médio),
# garantindo um desempenho consistente.
# É um algoritmo estável, o que significa que ele preserva a ordem original de elementos iguais.
# E funciona bem com grandes volumes de dados, onde a complexidade logarítmica se torna vantajosa.

# ---Desvantagens---: Uso de memória, requer memória extra para armazenar os subconjuntos durante a ordenação.
# E não é um algoritmo in-place, ou seja, não ordena o array diretamente sem utilizar memória auxiliar.