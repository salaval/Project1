import random

def name_generator():
    """ Prints a random combination of common swedish names """
    firsts = ["Albrecht", "Lysa", "Yvette", "Jésus", "Amanitus"]
    lasts = ["Andersson", "Natt och Dag", "av Pommern", "Krusmynta"]

    random.seed()
    first = firsts[random.randint(0, len(firsts)-1)]
    last = lasts[random.randint(0, len(lasts)-1)]

    name = first + " " + last
    return name


class bot:
    def __init__(self, execute, write, request, msg):
        self.execute = execute
        self.write = write
        self.request = request
        self.msg = msg
        self.response = ""
        # self.memory = dict()


def evaluate(state):
    # Magic goes here
    domain1 = ["katt", "hund", "ko", "häst"]    # djur
    domain2 = ["pasta", "käk", "mat", "macka"]    # mat
    domain3 = ["namn", "heter"]    # namn
    prob1 = 0
    prob2 = 0
    prob3 = 0
    domains = [[domain1, prob1], [domain2, prob2], [domain3, prob3]]

    # compare probability of domains
    for domain in domains:
        for word in domain[0]:
            if word in state.response:
                domain[1] += 1

    highest_prob = 0
    most_likely_domain = None
    for domain in domains:
        if domain[1] > highest_prob:
            if highest_prob != 0:
                pass
                # second_most_likely_domain = most_likely_domain
            highest_prob = domain[1]
            most_likely_domain = domain[0]

    state.msg = ""

    if most_likely_domain is None:
        state.msg += "Jag har ingen aning om vad du talar om."

    if most_likely_domain == domain1:  # hanterar svar om djur
        state.msg += "Jag gillar också djur!"

    if most_likely_domain == domain2:
        state.msg += "Jag finner det lätt obehagligt att du är så jävla tänd på mat..."

    if most_likely_domain == domain3:
        state.msg += "Mitt namn är" + name_generator()

    if "exit" in state.response or "stäng av" in state.response or "stick" in state.response:
        state.msg += "\nJag borde gå nu."
        state.execute = False

    # print(most_likely_domain)
    return state


def chatbot():
    #
    # input string
    # eval what to make of it
    # reply

    state = bot(True, True, True, "Wazzup, dawg?")
    print(state.msg)

    while state.execute:
        if state.request:
            state.response = input()

        state = evaluate(state)

        if state.write:
            print(state.msg)

    return
