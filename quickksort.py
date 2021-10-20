def quicksort(lista):
    if len(lista) < 2:
        return lista # Base lista com 0 ou 1 elemento ja estao ordenados
    else:
        pivo = lista[0] # Caso recursivo
        menores = [i for i in lista[1:] if i <= pivo] # Subarray de todos os elementos menores do que o pivo
        maiores = [i for i in lista[1:] if i > pivo]  # Subarray de todos os elementos maiores do que o pivo
        return quicksort(menores) + [pivo] + quicksort(maiores)

    
print(quicksort([10,9,8,3]))

