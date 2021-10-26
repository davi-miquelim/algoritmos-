estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]) # Voce passa um array como entrada e ele e convertido em conjunto

estacoes = {}
estacoes["kum"] = set(["id", "nv", "ut"])
estacoes["kdois"] = set(["wa", "id", "mt"])
estacoes["ktres"] = set(["or", "nv", "ca"])
estacoes["kquatro"] = set(["nv", "ut"])
estacoes["kcinco"] = set(["ca", "az"])

estacoes_final = set()

print("Rodando :c")

while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()
    for estacao, estados in estacoes.items():
        cobertos = estados_abranger & estados # Nova sintaxe isso e chamado de interseccao
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos
    estados_abranger -= estados_cobertos
    estacoes_final.add(melhor_estacao)


print(estacoes_final)
    
      
    