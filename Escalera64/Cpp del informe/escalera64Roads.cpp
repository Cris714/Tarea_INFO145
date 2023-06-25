#include <iostream>
#include <cmath>
#include <unordered_set>
#include <vector>
#include <chrono>
#include <algorithm>

using namespace std;

struct Escalon {
    int value;
    vector<vector<int>> road;

    Escalon() : value(0) {}
};

vector<Escalon> escalera64(const unordered_set<int>& S, vector<Escalon>& E, const unordered_set<int>& D) {
    for (int i = 0; i < (int)E.size(); ++i) {
        if (D.find(i + 1) == D.end()) {
            if (S.find(i + 1) != S.end()) {
                E[i].value += 1;
                E[i].road.push_back({i + 1});
            }
            for (const auto& s : S) {
                if (i - s >= 0) {
                    E[i].value += E[i - s].value;
                    for (const auto& path : E[i - s].road) {
                        vector<int> new_path = path;
                        new_path.push_back(i + 1);
                        E[i].road.push_back(new_path);
                    }
                }
            }
        }
    }
    return E;
}

int main() {
    int largoEscalera = 30;
    unordered_set<int> D;
    int p = 2;
    int d = 0;

    cout << "Largo de la escalera (n): ";
    cin >> largoEscalera;
    vector<Escalon> E(largoEscalera);
    cout << "Potencia saltos (p): ";
    cin >> p;
    cout << "Escalones rotos totales (r):";
    cin >> d;
    for (int i = 0; i < d; i++) {
        int e = rand() % (largoEscalera) + 1;
        while (D.find(e) != D.end()) {
            e = rand() % (largoEscalera) + 1;
        }
        D.insert(e);
    }


    unordered_set<int> S;
    for (int i = 0; i <= log2(largoEscalera) / log2(p); ++i) {
        S.insert(pow(p, i));
    }

    auto start = chrono::high_resolution_clock::now();
    escalera64(S, E, D);
    auto end = chrono::high_resolution_clock::now(); 
    auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start); // Calcular duración en milisegundos

    cout << "E: " << largoEscalera;
    
    cout << "\nD: ";
    for (int d : D) {
        cout << d << " ";
    }

    cout << "\nS: ";
    for (const auto& s : S) {
        cout << s << " ";
    }
    cout << "\n";
    cout << "Salida: " << E.back().value << "\n";
    cout << "Tiempo transcurrido: " << duration.count() << " \n"; // Imprimir tiempo transcurrido

    return 0;
}
