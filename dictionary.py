# Dictionary is a built in function em python for hash tables

# Check if the person has voted
votaram = {}
votaram["Tom"] = True
votaram["Ana"] = True
votaram["James"] = True


def verfica_eleitor(nome):
    if votaram.get(nome):
        print("Mande embora!")
    else:
        votaram[nome] = True
        print("Deixe Votar!")

verfica_eleitor("Davi")
verfica_eleitor("Davi")
