def radix(lista, exp):
    n = len(lista)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = lista[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = lista[i] // exp
        output[count[index % 10] - 1] = lista[i]
        count[index % 10] -= 1

    for i in range(n):
        lista[i] = output[i]

def radix_sort(lista):
    max_valor = max(lista)

    exp = 1
    while max_valor // exp > 0:
        radix(lista, exp)
        exp *= 10

minha_lista = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(minha_lista)
print("Lista ordenada: ", minha_lista)


# ---Vantagens---: Eficiência, no caso de números com dígitos fixos, pode ser muito eficiente, com complexidade de tempo O(nk),
# onde n é o número de elementos e k é o número de dígitos.
# O Radix Sort é um algoritmo de ordenação estável, o que significa que a ordem relativa dos elementos iguais é preservada durante a ordenação.
# A sua implementação é relativamente simples, especialmente quando comparado com outros algoritmos de ordenação complexos como o Quick Sort.
# E diferentemente de outros algoritmos de ordenação (como Quick Sort, Merge Sort),
# o Radix Sort não faz comparações diretas entre os elementos, o que o torna mais rápido em alguns casos.

# ---Desvantagens---: Dependência de dígitos fixos, o Radix Sort funciona melhor quando os elementos têm um número fixo de dígitos.
# No caso de elementos com diferentes números de dígitos, pode ser necessário aplicar um pré-processamento ou usar uma variante adaptada do algoritmo.
# O Radix Sort requer espaço extra para armazenar as contagens em cada dígito.
# Esta desvantagem pode ser significativa se os elementos tiverem muitos dígitos ou se forem usados muitos dígitos na implementação.
# Apesar de ser eficiente em certos casos, o Radix Sort pode não ser o algoritmo de ordenação mais eficiente para todos os cenários.
# Algoritmos como o Quick Sort, em média, podem ser mais eficientes em situações onde a complexidade de tempo é mais importante do que o espaço extra.
# E embora a implementação básica seja simples,
# a adaptação para lidar com diferentes números de dígitos ou elementos com diferentes tipos pode tornar a implementação mais complexa.