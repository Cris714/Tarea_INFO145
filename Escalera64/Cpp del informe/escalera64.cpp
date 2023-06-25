#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int escalera64(vector<int>& S, vector<int>& E, vector<int>& D) {
    /* Calcula la cantidad de sumas de permutaciones de S que lleguen a E[-1] sin pasar por D */
    for (int s : S) {
        E[s-1] = 1;
    }
    for (int d : D) {
        E[d-1] = -1;
    }

    for (int i = 0; i < E.size(); i++) {
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
    srand(time(nullptr));

    int largoEscalera = 20;
    vector<int> E(largoEscalera, 0);
    vector<int> D;
    int p = 2;
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
    cout << "\nSalida: " << escalera64(S, E, D) << endl;

    return 0;
}
