#include <iostream>
#include <cmath>
#include <unordered_set>
#include <vector>
#include <chrono>

using namespace std;

struct Escalon {
    int value;
    vector<vector<int>> road;

    Escalon() : value(0) {}
};

vector<Escalon> escalera64(const unordered_set<int>& S, vector<Escalon>& E, const unordered_set<int>& D) {
    for (int i = 0; i < E.size(); ++i) {
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
    vector<Escalon> E(largoEscalera);
    unordered_set<int> D;
    int p = 2;
    unordered_set<int> S;
    for (int i = 0; i <= log2(largoEscalera) / log2(p); ++i) {
        S.insert(pow(p, i));
    }

    auto start = chrono::high_resolution_clock::now();
    escalera64(S, E, D);
    auto end = chrono::high_resolution_clock::now(); 
    auto duration = chrono::duration_cast<chrono::milliseconds>(end - start); // Calcular duración en milisegundos

    cout << "E: " << largoEscalera << "\n";
    cout << "D: " << D.size() << "\n";
    cout << "S: ";
    for (const auto& s : S) {
        cout << s << " ";
    }
    cout << "\n";
    cout << "Salida: " << E.back().value << "\n";
    cout << "Tiempo transcurrido: " << duration.count() << " ms\n"; // Imprimir tiempo transcurrido

    return 0;
}
