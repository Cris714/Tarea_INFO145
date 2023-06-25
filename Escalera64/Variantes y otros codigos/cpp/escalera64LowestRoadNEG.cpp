#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>

using namespace std;

struct Escalon {
    long long value;
    vector<long long> road;
};

int escalera64(long long* S, Escalon* E, int n, int k) {
    
    for (int j = 0; j < k; j++){
        if (E[S[j]-1].value != -1){
            E[S[j]-1].value = 1;
            E[S[j]-1].road.push_back(S[j]);
        }
    }
    long long s;
    for (int i = 0, j = 0; i < n; i++, j = 0) 
        if (E[i].value != -1) 
            while (j < k && (s=S[j++]) <= i) {
                if (E[i-s].value != 0 && E[i-s].value != -1){
                    //if (E[i].value + E[i-s].value < E[i].value) printf("OVERFLOW");
                    E[i].value += E[i - s].value;
                    vector<long long> r = E[i - s].road;
                    r.push_back(i+1);
                    if (E[i].road.empty() || r.size() < E[i].road.size() + 1) 
                        E[i].road = r;
                }
            }
        
    
    return E[n-1].value;
}

int main() {
    
    srand(time(nullptr));
    
    // Parametros de entrada
    int p = 2;
    int largoEscalera = 8;
    
    // Creacion de vector con escalones
    Escalon* E = new Escalon[largoEscalera]; //n
    for (int i = 0; i < largoEscalera; i++) {
        Escalon e = Escalon();
        e.value = 0;
        E[i]=e;
    }
    
    // Destruidos
    int d = 2; // Cuantos eslabones random destruidos
    int r = 0;
    for (int i=0;i<d;i++) {
        do {
            r=rand()%largoEscalera;
        } while (E[r].value == -1);
        E[r].value = -1;
    }
    
    
    // Generacion de saltos respecto a P
    int k = int(log2(largoEscalera) / log2(p)+1);
    long long* S = new long long [k];
    for (int i = 0; i < k; i++)
        S[i] = pow(p, i);
    
    /* Escribir en pantalla */
    // Escribir la entrada
    printf("E (largo): %d", largoEscalera);
    printf("\nS: {");
    for (int i=0;i<k;i++) printf("%lld, ", S[i]);
    
    //Ejecutar
    printf("}\nSoluciones posibles: ");
    auto inicio = chrono::high_resolution_clock::now();
    escalera64(S, E, largoEscalera, k);
    auto final = chrono::high_resolution_clock::now();;
    
    // Escribir los Resultados
    printf("%lld",E[largoEscalera-1].value);
    if (largoEscalera < 101){
        printf("\nResultados: [");
        for (int i = 0; i < largoEscalera; i++) {
            printf("%lld", E[i].value);
            if (i < largoEscalera - 1) printf(", ");
        }
        printf("]");
    }
    printf("\nEjemplo de camino mas corto: [");
    for (int i = 0; i < E[largoEscalera-1].road.size(); i++) {
        printf("%lli", E[largoEscalera-1].road[i]);
        if (i < E[largoEscalera-1].road.size() - 1) printf(", ");
    }
    printf("]\n");
    
    auto duration = chrono::duration_cast<chrono::nanoseconds>(final-inicio);
    printf("Tiempo de ejecucion: %f", duration.count()*pow(10,-9));
    
    
    delete[] E;
    delete[] S;
    return 0;
}