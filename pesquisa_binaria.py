# Algoritmo de pesquisa binaria

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1 # Baixo e alto acompanham a parte da lista que esta procurando

    while baixo <= alto: # Enquanto ainda nao  conseguiu chegar a um unico elemento
        meio = (baixo + alto) // 2  # ...verifica o elemento central
        chute = lista[meio] 
        if chute == item: # Item encontrado
            return meio
            
        if chute > item: # O chute foi muito alto
            alto = meio -1
        else:
            baixo = meio + 1 # O chute foi muito baixo

    return None # Indica que o item nao foi encontrado


minha_lista = [1, 3, 5, 7, 9]  # Hora do teste!

print(pesquisa_binaria(minha_lista, 5))

print(pesquisa_binaria(minha_lista, 9))
