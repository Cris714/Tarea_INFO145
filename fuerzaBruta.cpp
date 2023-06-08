#include <iostream>
#include <vector>

using namespace std;

void fuerza_bruta(vector<bool> &E, vector<int> &X, vector<int> S, const int c);
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

    fuerza_bruta(E, X, S, 0);

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

template <typename S> void print_vector(vector<S> &vec){
    for (S n: vec) cout << n << " ";
    cout << endl;
}