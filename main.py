import random

def name_generator():
    firsts = ["Albrecht", "Lysa", "Yvette", "Jésus", "Amanitus"]
    lasts = ["Andersson", "Natt och Dag", "av Pommern", "Krusmynta"]

    random.seed()
    first = firsts[random.randint(0, len(firsts)-1)]
    last = lasts[random.randint(0, len(lasts)-1)]

    print(first, last)
