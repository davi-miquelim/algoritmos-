from collections import deque



grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []


def pessoa_e_vendedor(nome): # Enquanto a fila nao estiver vazia...
    return nome[-1] == "m"

def pesquisa(nome):
    fila_de_pesquisa = deque() # Cria uma nova fila
    fila_de_pesquisa += grafo[nome] # adiciona todos os seus vizinhos para a lista de pesquisa
    verificadas = [] # Esse vetor e a forma pela qual voce mantem o registro das pessoas que ja form verificadas
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft() # Pega a primeira pessoa da fila
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa): # Verifica se essa pesssoa e uma vendedora de mangas
                    print(pessoa + " vende manga") # Sim a pessoa vende manga
                    return True
            else:
                fila_de_pesquisa += grafo[pessoa] # Ela nao vende manga, adiciona todos os amigos dessa pessoa na lista
                verificadas.append(pessoa) # Marca essa pessoa como verificada
    return False

pesquisa("voce")
