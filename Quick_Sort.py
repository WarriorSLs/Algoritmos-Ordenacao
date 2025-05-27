def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[-1]

    menores = []
    iguais = []
    maiores = []

    for elemento in lista:
        if elemento < pivo:
            menores.append(elemento)
        elif elemento == pivo:
            iguais.append(elemento)
        else:
            maiores.append(elemento)

    return quick_sort(menores) + iguais + quick_sort(maiores)

minha_lista = [28, 33, 47, 3, 9, 82, 10]
lista_ordenada = quick_sort(minha_lista)
print("Lista ordenada: ", lista_ordenada)


# ---Vantagens---: Eficiência, o Quick Sort é um dos algoritmos de ordenação mais rápidos,
# especialmente em casos médios, com complexidade O(n log n). 
# É um algoritmo in-place, ou seja, não requer memória auxiliar significativa para a ordenação,
# tornando-o eficiente em termos de espaço.
# Em diversos cenários, o Quick Sort geralmente supera outros algoritmos, como o HeapSort, em termos de velocidade.
# E a escolha do pivô pode ser adaptada para melhorar o desempenho em diferentes situações, como a escolha do pivô mediano ou amostragem aleatória.

# ---Desvantagens---: Pior caso, se o pivô for mal escolhido, o Quick Sort pode ter um desempenho muito ruim, com complexidade O(n²).
# O Quick Sort não é um algoritmo estável, o que significa que a ordem relativa de elementos iguais pode ser alterada após a ordenação.
# A escolha do pivô é crucial para o desempenho do algoritmo, e uma escolha inadequada pode comprometer a eficiência.
# E para ordenação de grandes arquivos de dados que não cabem na memória principal, o Quick Sort não é a melhor opção, pois seu desempenho pode ser prejudicado.