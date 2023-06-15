#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <ctime>
#include <cstdlib>

using namespace std;
#define INF (unsigned int) -1

struct Escalon {
    unsigned long value;
    vector<unsigned long> road;
};

int escalera64(unsigned long* S, Escalon* E, int n, int k) {
    
    for (int j = 0; j < k; j++){
        E[S[j]].value = 1;
        E[S[j]].road.push_back(S[j] + 1);
    }
    unsigned long s;
    for (int i = 0, j=0; i < n; i++, j=0) {
        if (E[j].value != INF) {
            while ((s=S[j++]) < E[j].value) {
                if (i - s >= 0 && E[i - s].value > 0) {
                    E[i].value += E[i - s].value;
                    vector<unsigned long> r = E[i - s].road;
                    r.push_back(i + 1);
                    if (E[i].road.empty() || r.size() < E[i].road.size() + 1) 
                        E[i].road = r;
                }
                else break;
            }
        }
    }
    return E[n].value;
}

int main() {
    
    srand(time(nullptr));
    
    // Parametros de entrada
    int p = 2;
    int largoEscalera = 900;
    
    // Creacion de vector con escalones
    Escalon* E = new Escalon[largoEscalera]; //n
    for (int i = 0; i < largoEscalera; i++) {
        Escalon e = Escalon();
        e.value = 0;
        E[i]=e;
    }
    
    // Destruidos
    int d = 0;
    int r = 0;
    for (int i=0;i<d;i++) while (E[(r=rand()%largoEscalera)].value == INF) E[r].value = INF;
    
    // Generacion de saltos respecto a P
    int k = int(log2(largoEscalera) / log2(p));
    unsigned long* S = new unsigned long [k];
    for (int i = 0; i <= k; i++)
        S.pow(p, i);
    
    /* Escribir en pantalla */
    // Escribir la entrada
    printf("E (largo): %d", largoEscalera);
    printf("\b\b}\nS: {");
    for (unsigned long s : S) printf("%lu, ", s);
    
    //Ejecutar
    printf("\b\b}\nSoluciones posibles: ");
    clock_t inicio = clock();
    escalera64(S, E, largoEscalera, k);
    clock_t final = clock();
    
    // Escribir los Resultados
    printf("%lu",E[largoEscalera-1].value);
    if (largoEscalera < 101){
        printf("Resultados: [");
        for (int i = 0; i < largoEscalera; i++) {
            printf("%lu", E[i].value);
            if (i < largoEscalera - 1) printf(", ");
        }
        printf("]");
    }
    printf("\nEjemplo de camino mas corto: [");
    for (int i = 0; i < E[largoEscalera-1].road.size(); i++) {
        printf("%lu", E[largoEscalera-1].road[i]);
        if (i < E[largoEscalera-1].road.size() - 1) printf(", ");
    }
    printf("]\n");
    
    double tiempoEjecucion = double(final - inicio) / CLOCKS_PER_SEC;
    printf("Tiempo de ejecucion: %.6f\n", tiempoEjecucion);
    
    return 0;
}