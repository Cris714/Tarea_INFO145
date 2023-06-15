from numpy import log2, power
from random import randint

class escalon():
    def __init__(self):
        self.value = 0
        self.road = []

def escalera64(S="Set con los saltos", E="Lista con los peldaños", D="Set con los peldaños rotos")->list:
    '''Calcula la cantidad de sumas de permutaciones de S que lleguen a E[-1] sin pasar por D'''
    A = [escalon() for _ in range(len(E))]
    for i in range(len(E)):
        if (i+1 not in D):
            if (i+1 in S):
                A[i].value += 1
                A[i].road.append([i+1])
            for s in S:
                if (i-s >= 0):
                    A[i].value += A[i-s].value
                    for path in A[i-s].road:
                            A[i].road.append(path + [i + 1])
    print(f"Resultados: {[a.value for a in A]}\nCaminos: {A[-1].road}")
    return A[-1].value

def main():
    largoEscalera = 30
    E=[i+1 for i in range(largoEscalera)]
    D = {}
    p=2
    S=S={power(p,i) for i in range(int(log2(len(E))/log2(p))+1)}
    print(f"E: {E}\nD: {D}\nS: {S}\nSalida: {escalera64(S,E,D)}")

if (__name__ == "__main__"):
    main()