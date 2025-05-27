def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        troca = False
        for s in range(0, n-i-1):
            if lista[s] > lista[s+1]:
                lista[s], lista[s+1] = lista[s+1], lista[s]
                troca = True
        if not troca:
            break

minha_lista = [6, 2, 8, 4, 10, 76, 23]
bubble_sort(minha_lista)
print ("Lista ordenada: ", minha_lista)

# ---Vantagens---: É simples, um dos algoritmos de ordenação mais fáceis de entender e implementar,
# o processo de comparação e troca de elementos é transparente e intuitivo.
# E se o conjunto de dados for pequeno e quase ordenado, o Bubble Sort pode ser uma opção razoável. 

# ---Desvantagens---: É ineficiente para grandes conjuntos de dados, a complexidade quatrática (O(n²)) torna-o muito lento,
# para conjuntos de dados grandes.
# Comparado com outros algoritmos de ordenação, como o Quick Sort, o Bubble Sort é consideravelmente mais lento. 
# Para listas grandes, existem algoritmos mais eficientes, como o Merge Sort ou o Quick Sort.
# E mesmo comparado a outros algoritmos quadráticos, o Bubble Sort tem um desempenho lento na prática. 