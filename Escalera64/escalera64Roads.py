from numpy import log2, power
from random import randint

class escalon():
    def __init__(self):
        self.value = 0
        self.road = []

def escalera64(S="Set con los saltos", E="Lista con los peldaños", D="Set con los peldaños rotos")->list:
    
    for i in range(len(E)):
        if (i+1 not in D):
            if (i+1 in S):
                E[i].value += 1
                E[i].road.append([i+1])
            for s in S:
                if (i-s >= 0):
                    E[i].value += E[i-s].value
                    for path in E[i-s].road:
                        E[i].road.append(path + [i + 1])
    return E[-1]

def main():
    largoEscalera = 20
    E=[escalon() for _ in range(largoEscalera)]
    D = {}
    p=2
    S=S={power(p,i) for i in range(int(log2(len(E))/log2(p))+1)}
    print(f"E: {largoEscalera}\nD: {D}\nS: {S}\nSalida: {escalera64(S,E,D).value}")

if (__name__ == "__main__"):
    main()