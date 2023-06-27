from numpy import log2, power
from random import randint
def escalera64(S="Arreglo con los saltos", E="Arreglo con los peldaños", D="Arreglo con los peldaños rotos")->int:
    '''Calcula la cantidad de sumas de permutaciones de S que lleguen a E[-1] sin pasar por D'''
    for s in S:
        E[s-1] = 1
    for d in D:
        E[d-1] = -1

    for i in range(len(E)):
        if (E[i] != -1):
            for s in S:
                if i-s >= 0 and E[i-s] != -1:
                    E[i] += E[i-s]

    return E[-1]

def main():
    #largoEscalera=randint(1,30)
    largoEscalera = 20
    E=[0 for i in range(largoEscalera)]
    #D={randint(1,len(E)) for _ in range(int(log2(largoEscalera))+1) }
    D = []
    #p=randint(2,4)
    p=2
    S=[power(p,i) for i in range(int(log2(len(E))/log2(p))+1)]
    #S={1,3,9}
    print(f"E: {E}\nD: {D}\nS: {S}\nSalida: {escalera64(S,E,D)}")

if (__name__ == "__main__"):
    main()