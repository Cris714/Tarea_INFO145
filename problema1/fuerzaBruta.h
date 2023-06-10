#include <iostream>
#include <vector>

using namespace std;

long long fuerza_bruta_rec(vector<bool> &E, const int n, vector<int> &X, const int c){
    long long ac = 0;
    for (int x: X){
        if (c + x < n && E[c + x - 1])
            ac += fuerza_bruta_rec(E, n, X, c + x);
        
        else if (c + x == n)
            ++ac;
    }
    return ac;
}

long long fuerza_bruta(vector<bool> &E, vector<int> &X){
    int c = 0, n = E.size();
    return fuerza_bruta_rec(E, n, X, c);
}


// CODIGO PARA IMPRIMIR TODAS LAS SOLUCIONES (SOLO SE PUEDE CON FUERZA BRUTA)

template <typename S> void print_vector(vector<S> &vec){
    for (S n: vec) cout << n << " ";
    cout << endl;
}

void soluciones_rec(vector<bool> &E, vector<int> &X, vector<int> S, const int c){
    for (int x: X){
        if (c + x < E.size() && E[c + x - 1]){
            S.push_back(c + x);
            soluciones_rec(E, X, S, c + x);
            S.pop_back();
        }
        else if (c + x == E.size()){
            S.push_back(c + x);
            print_vector(S);
            S.pop_back();
        }
    }
}

void soluciones(vector<bool> &E, vector<int> &X){
    int c = 0, n = E.size();
    vector<int> S;
    soluciones_rec(E, X, S, c);
}