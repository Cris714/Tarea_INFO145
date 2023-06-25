#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>
#include <deque>
#include <limits>
#include <tuple>
#include <functional>
#include <algorithm>
#include <unordered_set>
#include <cmath>
using namespace std;
//Se crea la clase GrafoD para  los grafos dirigidos que se usan en los puertos
class GrafoD {
public:
    unordered_map<char, vector<pair<char, int>>> Ad;

    void add_edge(char src, char dest, int weight) {
        Ad[src].push_back(make_pair(dest, weight));
    }
};
//Se crea la clase Grafo para los grafos no dirigidos que usan las islas
class Grafo {
public:
    unordered_map<char, vector<pair<char, int>>> Ad;

    void add_edge(char src, char dest, int weight) {
        Ad[src].push_back(make_pair(dest, weight));
        Ad[dest].push_back(make_pair(src, weight));
    }
};

//Se declaran las funciones que se van a usar
unordered_map<char, int> bfs(Grafo& graph, char source);
unordered_map<char, int> dijkstra(GrafoD& graph, char source);
tuple<int, int, int> puertosIslas(GrafoD& Puertos, char s, Grafo& Islas, char z, vector<tuple<char, char, int>>& costoBarco, vector<char>& Puertosh, vector<char>& Islash);
bool estaEnVector(vector<char> vector, char elemento);
tuple<GrafoD, char, Grafo, char, vector<tuple<char, char, int>>, vector<char>, vector<char>> creaGrafo(int n, int k, int m, int logm);

//Funcion Breadth-First Search modificada para que funcione con los pesos de las aristas del grafo, en lugar de la cantidad de nodos en las islas
unordered_map<char, int> bfs(Grafo& graph, char source) {
    unordered_set<char> visited;
    deque<pair<char, int>> queue;

    unordered_map<char, int> bfs_cost;
    queue.push_back(make_pair(source, 0));
    bfs_cost[source] = 0;

    while (!queue.empty()) {
        char vertex = queue.front().first;
        int depth = queue.front().second;
        queue.pop_front();

        visited.insert(vertex);

        for (auto& neighbor : graph.Ad[vertex]) {
            char next_vertex = neighbor.first;
            if (visited.find(next_vertex) == visited.end()) {
                queue.push_back(make_pair(next_vertex, depth + 1));
                visited.insert(next_vertex);
                bfs_cost[next_vertex] = depth + 1;
            }
        }
    }

    return bfs_cost;
}
//Funcion de Dijstra para calcular el costo minimo de los puertos
unordered_map<char, int> dijkstra(GrafoD& graph, char source) {
    unordered_map<char, int> distances;
    priority_queue<pair<int, char>, vector<pair<int, char>>, greater<pair<int, char>>> pq;

    distances[source] = 0;
    pq.push(make_pair(0, source));

    while (!pq.empty()) {
        int dist = pq.top().first;
        char vertex = pq.top().second;
        pq.pop();

        if (dist > distances[vertex]) {
            continue;
        }

        for (auto& neighbor : graph.Ad[vertex]) {
            char next_vertex = neighbor.first;
            int edge_weight = neighbor.second;

            int new_dist = dist + edge_weight;

            if (distances.find(next_vertex) == distances.end() || new_dist < distances[next_vertex]) {
                distances[next_vertex] = new_dist;
                pq.push(make_pair(new_dist, next_vertex));
            }
        }
    }

    return distances;
}
//Funcion para calcular la ruta mas barata de capital a capital(las capitales son s y z)
tuple<int, int, int> puertosIslas(GrafoD& Puertos, char s, Grafo& Islas, char z, vector<tuple<char, char, int>>& costoBarco, vector<char>& Puertosh, vector<char>& Islash) {
    unordered_map<char, int> puertos_cost = dijkstra(Puertos, s);

    unordered_map<char, int> islas_cost;

    for (char isla : Islash) {
        islas_cost[isla] = bfs(Islas, isla)[z];
    }

    int min_cost = numeric_limits<int>::max();
    int besti = 0;
    int bestj = 0;

    for (int i = 0; i < Puertosh.size(); i++) {
        for (int j = 0; j < Islash.size(); j++) {
            int costo = puertos_cost[Puertosh[i]];
            for (auto& x : costoBarco) {
                if (get<0>(x) == Puertosh[i] && get<1>(x) == Islash[j]) {
                    costo += get<2>(x);
                }
            }
            costo += islas_cost[Islash[j]];

            if (costo < min_cost) {
                min_cost = costo;
                besti = i+1;
                bestj = j+1;
            }
        }
    }

    return make_tuple(min_cost, besti, bestj);
}
//Funcion para saber si un elemento esta en un vector
bool estaEnVector(vector<char> vector, char elemento) {
    return std::find(vector.begin(), vector.end(), elemento) != vector.end();
}
//Esta funcion crea los datos necesarios para poder ejecutar el programa cuando se dan argumentos en la entrada
tuple<GrafoD, char, Grafo, char, vector<tuple<char, char, int>>, vector<char>, vector<char>> creaGrafo(int n, int k, int m, int logm) {
    GrafoD Puertos;
    Grafo Islas;
    vector<char> Puertosh;
    vector<char> Islash;
    vector<tuple<char,char,int>> costoBarco;
    srand(time(NULL));
    
    //Se empieza creando los simbolos que usaran los puertos.. en este caso los simbolos del alfabeto
    vector<char> puertos_symbols;
    for (int i = 0; i < n; i++) {
        puertos_symbols.push_back('A' + i);
    }
    //Aqui se rellena el GrafoD Puertos con valores aleatorios
    vector<tuple<char, char, int >> costosPuertos;
    for (int i = 0; i < n; i++){
        for(int j = 0; j < n ; j++){
            // Generar un número aleatorio entre 0 y 99
            int random_num = rand() % 100;
            int random_costo = rand()% 30 +1;
        // Verificar si el número aleatorio es menor que 60 (probabilidad del 60%)
            if (random_num < 60 &&  i != j) {
                costosPuertos.push_back(make_tuple(puertos_symbols[i],puertos_symbols[j],random_costo));
            }
        }
    }
    for (auto& [puerto1, puerto2, costop] : costosPuertos) {
            Puertos.add_edge(puerto1, puerto2, costop);
    }

    // Se crean símbolos aleatorios para Islas en este caso los simbolos numericos
    vector<char> islas_symbols;
    for (int i = 0; i < m; i++) {
        islas_symbols.push_back('0' + i);
    }
    //Se rellena el Grafo Islas con valores aleatorios
    vector<tuple<char, char, int >> costosIslas;
    for (int i = 0; i < m; i++){
        for(int j = i; j < m ; j++){
            // Generar un número aleatorio entre 0 y 99
            int random_num = rand() % 100;
            int random_costo = rand()% 30 +1;
        // Verificar si el número aleatorio es menor que 60 (probabilidad del 60%)
            if (random_num < 60 &&  i != j) {
                costosIslas.push_back(make_tuple(islas_symbols[i],islas_symbols[j],random_costo));
            }
        }
    }
    for (auto& [islas1, islas2, costoi] : costosIslas) {
            Islas.add_edge(islas1, islas2, costoi);
    }

    // Seleccionar símbolo para Pi y Ii que son las capitales
    int randomP = rand()%n;
    int randomI = rand()%m;
    char Pi = puertos_symbols[randomP];
    char Ii = islas_symbols[randomI];


    // Se agregan símbolos aleatorios a los conjuntos Puertosh e Islash que son los puertos e islas habilitados para tener barcos
    int cont= 0;
    while(cont < k) {
        int random_num = rand() % n;
        if(puertos_symbols[random_num]!=Pi && !estaEnVector(Puertosh,puertos_symbols[random_num])){
            Puertosh.push_back(char(puertos_symbols[random_num]));
            cont++;
        }
    }

    cont= 0;
    while(cont <logm) {
        int random_num = rand() % n;
        if(islas_symbols[random_num]!=Pi && !estaEnVector(Islash,islas_symbols[random_num])){
            Islash.push_back(char(islas_symbols[random_num]));
            cont++;
        }
    }
    
    
    //Se le ponen costos aleatorios a los viajes entre los puertos y las islas
    for(int i = 0; i<k; i++){
        for(int j=0; j<logm; j++){
            int random_num = rand() % 60 - 30;
            costoBarco.push_back(make_tuple(Puertosh[i],Islash[j],random_num));
        }
    }
    return make_tuple(Puertos, Pi, Islas, Ii, costoBarco, Puertosh, Islash);
}

int main(int argc, char** argv) {
    GrafoD Puertos;
    Grafo Islas;
    char Pi;
    char Ii;
    vector<tuple<char, char, int>> costoBarco;
    vector<char> Puertosh;
    vector<char> Islash;
    bool ar = true;
    int n, k, m,logm; //n = num ciudades, m = num islas, k = num ciudades con puertos.
    if(argc != 4)
	{
		cout << "Usando valores por defecto para validación..." << endl;
        cout << "Para definir parámetros ejecutar como: ./prog n k m" << endl;
    }
    else{
        ar = false;
    }
    if(ar){//Se asignan los valores del informe
        vector<tuple<char, char, int>> costosPuertos = { make_tuple('S', 'A', 2), make_tuple('S', 'D', 8), make_tuple('A', 'S', 3), make_tuple('A', 'B', 1), make_tuple('A', 'D', 3), make_tuple('B', 'S', 4), make_tuple('B', 'C', 6), make_tuple('C', 'B', 5), make_tuple('C', 'D', 9), make_tuple('D', 'B', 2), make_tuple('D', 'C', 2) };

        for (auto& [puerto1, puerto2, costop] : costosPuertos) {
            Puertos.add_edge(puerto1, puerto2, costop);
        }
        vector<tuple<char, char, int>> costosIslas = { make_tuple('1', '4', 2), make_tuple('1', '2', 1), make_tuple('2', '4', 3), make_tuple('Z', '2', 12), make_tuple('Z', '5', 2), make_tuple('Z', '3', 5), make_tuple('Z', '6', 2), make_tuple('Z', '8', 3), make_tuple('2', '3', 5), make_tuple('4', '5', 1), make_tuple('4', '6', 4), make_tuple('6', '7', 3), make_tuple('7', '8', 7), make_tuple('3', '7', 4) };

        for (auto& [islas1, islas2, costoi] : costosIslas) {
            Islas.add_edge(islas1, islas2, costoi);
        }
        Puertosh = { 'C', 'D' };
        Islash = { '1', '2', '3' };
        costoBarco = { make_tuple('C', '1', -4), make_tuple('C', '2', 9), make_tuple('C', '3', 7), make_tuple('D', '1', 12), make_tuple('D', '2', -3), make_tuple('D', '3', 21) };
        Pi = 'S';
        Ii = '1';
    }
    else{//Aqui se ocupan los valores del argumento y se llama a la funcion creaGrafo() para crear valores al azar
        n = atoi(argv[1]);
        k = atoi(argv[2]);
        m = atoi(argv[3]);
        logm = log2(m);
        auto [createdPuertos, createdPi, createdIslas, createdIi, createdcostoBarco, createdPuertosh, createdIslash] = creaGrafo(n, k, m, logm);
        Puertosh = createdPuertosh;
        Islash = createdIslash;
        Puertos = createdPuertos;
        Pi = createdPi;
        Islas = createdIslas;
        createdIi = Ii;
        createdcostoBarco = costoBarco;
    }
    auto [min_cost, besti, bestj] = puertosIslas(Puertos, Pi , Islas, Ii, costoBarco, Puertosh, Islash);
    //Se imprimen los resultados: el costo minimo de capital a capital, y cuales son el puerto y la isla que se uso 
    cout << "Costo Mínimo: " << min_cost << endl;
    cout << "Mejor puerto habilitado: " << besti << endl;
    cout << "Mejor isla habilitada: " << bestj << endl;

    return 0;
}