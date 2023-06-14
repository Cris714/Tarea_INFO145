#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <ctime>
#include <cstdlib>

using namespace std;

struct Escalon {
    unsigned long number;
    unsigned long value;
    vector<unsigned long> road;
};

int escalera64(set<unsigned long> S, Escalon* E, set<unsigned long> D, int l) {
    
    for (int i = 0; i < l; i++) {
        if (D.find(i + 1) == D.end()) {
            if (S.find(i + 1) != S.end()) {
                E[i].value += 1;
                E[i].road.push_back(i + 1);
            }
            for (int s : S) {
                if (i - s >= 0 && E[i - s].value > 0) {
                    E[i].value += E[i - s].value;
                    vector<unsigned long> r = E[i - s].road;
                    r.push_back(i + 1);
                    if (E[i].road.empty() || r.size() < E[i].road.size() + 1) 
                        E[i].road = r;
                    
                }
            }
        }
    }
    return E[l].value;
}

int main() {
    srand(time(nullptr));
    
    // Parametros de entrada
    int p = 2;
    int largoEscalera = 900;
    
    // Creacion de vector con escalones
    Escalon* E = new Escalon[largoEscalera];
    for (int i = 0; i < largoEscalera; i++) {
        Escalon e = Escalon();
        e.number = i+1;
        e.value = 0;
        E[i]=e;
    }
    
    set<unsigned long> D = {};
    
    // Generacion de saltos respecto a P
    set<unsigned long> S;
    for (int i = 0; i <= int(log2(largoEscalera) / log2(p)); i++) {
        S.insert(pow(p, i));
    }
    
    // Escribir la entrada
    if (largoEscalera < 101){
        printf("E:[");
        for (int i = 0; i < largoEscalera; i++) {
            printf("%lu", E[i].number);
            if (i < largoEscalera - 1) printf(", ");
        }
        printf("]");
    }
    else printf("E (largo): %d", largoEscalera);
    printf("\nD: {");
    for (unsigned long d : D) 
        printf("%lu, ", d);
    printf("\b\b}\nS: {");
    for (unsigned long s : S) 
        printf("%lu, ", s);
    
    //Ejecutar
    printf("\b\b}\nSoluciones posibles: ");
    clock_t inicio = clock();
    escalera64(S, E, D, largoEscalera);
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