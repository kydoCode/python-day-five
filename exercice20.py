def additionner(a, b):
    return a + b

def soustraire(a, b):
    return a - b

def multiplier(a,b):
    return a * b

def diviser(a,b):
    if b!=0:
        return a/b
    else:
        return "Erreur: Division par zéro !"

a = int(input"Entrez le premier nombre: ))
b = int(input("Entrez le deuxième nombre: "))
operation = input("Entrez l'opération à effectuer (+, -, *, /): ")
