def InvertendoString(base):
    N = len(base)
    newString = ''
    for i in range(N):
        newString = newString + base[-1-i] 
    return str(newString)

invertString = "PARALELEPIPEDO" #string entrada a qual sera testada.
inverted = InvertendoString(invertString)
print(f"Invertendo a palavra: {invertString} \nObtemos: {inverted}")