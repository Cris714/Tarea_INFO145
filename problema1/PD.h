#include <vector>

using namespace std;

long long escalera_PD_rec(vector<long long> &D, vector<bool> &E, const int n, vector<int> &X, const int c){
    if (D[c] != -1)
        return D[c];

    long long ac = 0;
    for (int x: X){
        if (c + x < n && E[c + x - 1])
            D[c] = (ac+=escalera_PD_rec(D, E, n, X, c + x));
        
        else if (c + x == n)
            return D[c]=++ac;
    }
    return ac;
}

long long escalera_PD(vector<bool> &E, vector<int> &X){
    int c = 0, n = E.size();
    vector<long long> D(n, -1);
    return escalera_PD_rec(D, E, n, X, c);
}