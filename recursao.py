# Recursao
# Na recursao vou chamar funcao dentro da minha funcao para resolver o problem de maneira mais simples



def regressiva(i):
    print(i)
    if i <= 1:
        return
    else: 
        regressiva(i - 1)


# Funcao recursiva pra calcular o fatorial de x
def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x - 1)

# Funcao para somar itens em uma lista usando recursao

def somaLista(lista):
    if lista == []:
        return 0
    else:
        return lista[0] + somaLista(lista[1:])


#  Funcao recursiva para contar items em uma lista

def contaItems(lista):
    if lista == []:
        return 0
    else:
        return 1 + contaItems(lista[1:])


# Encontre o valor mais alto em uma lista

def buscaMaior(lista):
    maior = lista[0]
    maiorIndice =  0
    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            maiorIndice = i
    return lista[maiorIndice]

print(buscaMaior([1,100,50, 999]))

