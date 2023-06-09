from numpy import log2, power
from random import randint
def escalera64(S="Set con los saltos", E="Lista con los peldaños", D="Set con los peldaños rotos")->list:
    '''Calcula la cantidad de sumas de permutaciones de S que lleguen a E[-1] sin pasar por D'''
    A = [0]*len(E)
    for i in range(len(E)):
        if (i+1 not in D):
            if (i+1 in S):
                A[i] += 1
            for s in S:
                if i-s >= 0:
                    A[i] += A[i-s]
    print(f"Resultados: {A}")
    return A[-1]

def main():
    largoEscalera=randint(1,30)
    #largoEscalera = 12
    E=[i+1 for i in range(largoEscalera)]
    D={randint(1,len(E)) for _ in range(int(log2(largoEscalera))+1) }
    #D = {4,11}
    p=randint(2,4)
    S={power(p,i) for i in range(int(log2(len(E))/log2(p))+1)}
    #S={1,3,9}
    print(f"E: {E}\nD: {D}\nS: {S}\nSalida: {escalera64(S,E,D)}")

if (__name__ == "__main__"):
    main()