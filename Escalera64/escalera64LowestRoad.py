from numpy import log2, power
from random import randint
import time

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
                A[i].road = [i+1]
            for s in S:
                if (i-s >= 0 and A[i-s].value > 0):
                    A[i].value += A[i-s].value
                    r = A[i-s].road + [i+1]
                    if (len(A[i].road) == 0 or len(r) < len(A[i].road)+1):
                        A[i].road = r
                
    print(["", f"Resultados: {[a.value for a in A]}\n"][len(E)<=100] + f"Ejemplo de camino mas corto: {A[-1].road}")
    
    return A[-1].value

def main():
    
    '''
    largoEscalera = 900
    E=[i+1 for i in range(largoEscalera)]
    D = {1,3,4}
    S={1,2,4}
    '''
    
    largoEscalera=900
    E=[i+1 for i in range(largoEscalera)]
    D={randint(1,len(E)) for _ in range(int(log2(largoEscalera))+1) }
    p=randint(2,5)
    S={power(p,i) for i in range(int(log2(len(E))/log2(p))+1)}

    inicio = time.perf_counter()
    print("E:" + [f" {len(E)} (Largo)", f"{E}"][len(E)<=100] + f"\nD: {D}\nS: {S}\nSalida: {escalera64(S,E,D)}")
    final = time.perf_counter()
    print(f"Tiempo de ejecucion: {final-inicio}")
    
if (__name__ == "__main__"):
    main()
