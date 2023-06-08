#include <iostream>
#include <vector>

using namespace std;

void fuerza_bruta(vector<bool> &E, vector<int> &X, vector<int> S, const int c);
long long fuerza_bruta_cont(vector<bool> &E, const int n, vector<int> &X, const int c);
long long escalera64(vector<long long> &D, vector<bool> &E, const int n, vector<int> &X, const int c);
template <typename S> void print_vector(vector<S> &vec);

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

    // if (n < 10) fuerza_bruta(E, X, S, 0);
    // cout << "N° Soluciones: " << fuerza_bruta_cont(E, n, X, 0) << endl;

    // Usando PD
    vector<long long> D(n, INT64_MIN);
    cout << "N° Soluciones: " << escalera64(D, E, n, X, 0) << endl;

    return EXIT_SUCCESS;
}

void fuerza_bruta(vector<bool> &E, vector<int> &X, vector<int> S, const int c){
    for (int x: X){
        if (c + x < E.size() && E[c + x - 1]){
            S.push_back(c + x);
            fuerza_bruta(E, X, S, c + x);
            S.pop_back();
        }
        else if (c + x == E.size()){
            S.push_back(c + x);
            print_vector(S);
            S.pop_back();
        }
    }
}

long long fuerza_bruta_cont(vector<bool> &E, const int n, vector<int> &X, const int c){
    long long ac = 0;
    for (int x: X){
        if (c + x < n && E[c + x - 1])
            ac += fuerza_bruta_cont(E, n, X, c + x);
        
        else if (c + x == n)
            return ++ac;
    }
    return ac;
}

long long escalera64(vector<long long> &D, vector<bool> &E, const int n, vector<int> &X, const int c){
    if (D[c] > INT64_MIN)
        return D[c];

    long long ac = 0;
    for (int x: X){
        if (c + x < n && E[c + x - 1])
            D[c] = (ac+=escalera64(D, E, n, X, c + x));
        
        else if (c + x == n)
            return D[c]=++ac;
    }
    return ac;
}

template <typename S> void print_vector(vector<S> &vec){
    for (S n: vec) cout << n << " ";
    cout << endl;
}