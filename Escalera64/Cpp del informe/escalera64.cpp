#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <algorithm>

using namespace std;

int escalera64(vector<int>& S, vector<int>& E, vector<int>& D) {
    /* Calcula la cantidad de sumas de permutaciones de S que lleguen a E[-1] sin pasar por D */
    for (int s : S) {
        E[s-1] = 1;
    }
    for (int d : D) {
        E[d-1] = -1;
    }

    for (int i = 0; i < (int)E.size(); i++) {
        if (E[i] != -1) {
            for (int s : S) {
                if (i - s >= 0 && E[i - s] != -1) {
                    E[i] += E[i - s];
                }
            }
        }
    }

    return E[E.size() - 1];
}

int main() {

   

    int largoEscalera = 20;
    vector<int> D;
    int p = 2;
    int d;

    cout << "Largo de la escalera (n): ";
    cin >> largoEscalera;
    vector<int> E(largoEscalera, 0);
    cout << "Potencia saltos (p): ";
    cin >> p;
    cout << "Escalones rotos totales (r):";
    cin >> d;
    int seed;
    cout << "Ingrese una semilla para la generacion aleatoria: ";
    cin >> seed;
    srand(seed);

    for (int i = 0; i < d; i++) {
        int e = rand() % (largoEscalera) + 1;
        while (std::find(D.begin(), D.end(), e) != D.end()) {
            e = rand() % (largoEscalera) + 1;
        }
        D.push_back(e);
    }


    vector<int> S;
    for (int i = 0; i <= log2(E.size()) / log2(p); i++) {
        S.push_back(pow(p, i));
    }

    cout << "E: ";
    for (int e : E) {
        cout << e << " ";
    }
    cout << "\nD: ";
    for (int d : D) {
        cout << d << " ";
    }
    cout << "\nS: ";
    for (int s : S) {
        cout << s << " ";
    }

    auto inicio = chrono::high_resolution_clock::now();
    auto e = escalera64(S, E, D);
    auto final = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::nanoseconds>(final-inicio);
    cout << "\nSalida: " << e << "\nTiempo transcurrido en nanosegundos: " << duration.count() << endl;


    return 0;
}
