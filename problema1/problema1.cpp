#include <iostream>
#include <vector>
#include <chrono>

#include "fuerzaBruta.h"
#include "PD.h"

using namespace std;

double timer(long long &t, vector<bool> &E, vector<int> &X, long long (*fn)(vector<bool>&, vector<int>&));

int main(int argc, char** argv){
    int n, r, p;

    if (argc != 4){ // valores por defecto para prueba
        cout << "Usando valores por defecto para validación..." << endl;
        cout << "Para definir parámetros ejecutar como: ./prog n r p" << endl;
        n = 10;
        r = 3;
        p = 2;
    }
    else{ // asigna elementos si se pasaron argumentos en el programa
        n = atoi(argv[1]);
        r = atoi(argv[2]);
        p = atoi(argv[3]);
    }

    int index, jmp = 1;
    long long t;
    double fb_time, pd_time;
    vector<bool> E(n, true); // vector que representa la escalera
    vector<int> S, X; // vectores auxiliares: S <- traza de solucion | X <- saltos posibles

    // inicialización de E para ejecución con argumentos
    if (argc == 4){
        for (int i = 0; i < r; i++){
            while (!E[index=rand()%(n-2)]);
            E[index] = false;
        }
    }
    else
        E[3] = E[4] = E[7] = false;

    // inicialización de X
    do X.push_back(jmp);
    while((jmp*=p) <= n);

    // imprime soluciones para n pequeño
    if (n < 10) soluciones(E, X);

    // Usando fuerza bruta
    cout << " - Fuerza bruta: " << endl;
    fb_time = timer(t, E, X, &fuerza_bruta);
    cout << "N Soluciones: " << t << endl;
    cout << "Tiempo: " << fb_time << " [s]" << endl;
    cout << endl;

    // Usando PD
    cout << " - Programacion dinamica: " << endl;
    pd_time = timer(t, E, X, &escalera_PD);
    cout << "N Soluciones: " << t << endl;
    cout << "Tiempo: " << pd_time << " [s]" << endl;
    cout << endl;

    return EXIT_SUCCESS;
}

double timer(long long &t, vector<bool> &E, vector<int> &X, long long (*fn)(vector<bool>&, vector<int>&)){
    typedef chrono::high_resolution_clock Clock;
    auto t1 = Clock::now();
    t = fn(E, X);
    auto t2 = Clock::now();
    return (t2 - t1).count()/1e9;
}