def buscaMenor (arr):
    menor = arr[0] # Armazena o menor valor
    menor_inidice = 0 # Armazena o indice de menor valor
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_inidice = i
    return menor_inidice


# Ordena o array do menor para o maior
def ordenacaoporSelecao(arr): # Ordenaacoes em um rray
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr) # Encontra o menor elemento do array e adiciona ao novo array
        novoArr.append(arr.pop(menor))
    return novoArr


print(ordenacaoporSelecao([11,5,6,7,8]))