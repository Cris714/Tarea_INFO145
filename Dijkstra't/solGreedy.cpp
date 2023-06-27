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
#include <chrono>
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
void print(vector<tuple<char,char,int>> costosPuertos, vector<tuple<char,char,int>> costosIslas, vector<tuple<char,char,int>> costoBarco);
tuple<GrafoD, char, Grafo, char, vector<tuple<char, char, int>>, vector<char>, vector<char>> creaGrafo(int n, int k, int m, int logm);


int main(int argc, char** argv) {
    //Se inicializan las variables
    GrafoD Puertos;         //Grafo dirigido con los puertos
    Grafo Islas;            //Grafo no dirigido con las islas
    char Pi;                //Capital continental del Pais
    char Ii;                //Capital continental del archipielago
    vector<tuple<char, char, int>> costoBarco; //Costos de ir de los puertos a las islas
    vector<char> Puertosh;  //Puertos habilitados para viajar en barco
    vector<char> Islash;    //islas habilitadas para viajar en barco
    bool ar = true;
    int n, k, m,logm; //n = num ciudades, m = num islas, k = num ciudades con puertos.
    if(argc != 5)
	{
		cout << "Usando valores por defecto para validación..." << endl;
        cout << "Para definir parámetros ejecutar como: ./prog n k m seed" << endl;
    }
    else{
        ar = false;
    }
    if(ar){//Se asignan los valores del informe
        srand(atoi(argv[4]));

        vector<tuple<char, char, int>> costosPuertos = {
            make_tuple('A', 'C', 25),
            make_tuple('A', 'E', 10),
            make_tuple('A', 'G', 3),
            make_tuple('B', 'A', 25),
            make_tuple('B', 'C', 1),
            make_tuple('B', 'E', 25),
            make_tuple('C', 'B', 4),
            make_tuple('C', 'D', 10),
            make_tuple('C', 'F', 5),
            make_tuple('C', 'G', 6),
            make_tuple('D', 'A', 1),
            make_tuple('D', 'B', 27),
            make_tuple('D', 'C', 3),
            make_tuple('D', 'E', 21),
            make_tuple('D', 'F', 16),
            make_tuple('E', 'B', 26),
            make_tuple('E', 'C', 23),
            make_tuple('E', 'G', 7),
            make_tuple('F', 'A', 2),
            make_tuple('F', 'B', 1),
            make_tuple('F', 'D', 10),
            make_tuple('F', 'E', 15),
            make_tuple('G', 'B', 6),
            make_tuple('G', 'D', 3),
            make_tuple('G', 'E', 14)
        };

        for (auto& [puerto1, puerto2, costop] : costosPuertos) {
            Puertos.add_edge(puerto1, puerto2, costop);
        }

        vector<tuple<char, char, int>> costosIslas = {
            make_tuple('0', '1', 5),
            make_tuple('0', '2', 21),
            make_tuple('0', '3', 14),
            make_tuple('0', '4', 16),
            make_tuple('1', '2', 21),
            make_tuple('2', '3', 28),
            make_tuple('2', '4', 24),
            make_tuple('2', '6', 16),
            make_tuple('3', '5', 15),
            make_tuple('3', '6', 16)
        };

        for (auto& [islas1, islas2, costoi] : costosIslas) {
            Islas.add_edge(islas1, islas2, costoi);
        }

        Puertosh = { 'C', 'D' };
        Islash = { '3', '6' };

        costoBarco = {
            make_tuple('D', '3', 9),
            make_tuple('D', '6', 5),
            make_tuple('C', '3', 15),
            make_tuple('C', '6', 17)
        };

        Pi = 'S';
        Ii = '1';

        print(costosPuertos, costosIslas, costoBarco);
        cout << "Nodo inicial: " << Pi << "\nNodo final: " << Ii << endl;

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
        Ii = createdIi;
        costoBarco = createdcostoBarco;
    }
    
    auto [min_cost, besti, bestj] = puertosIslas(Puertos, Pi , Islas, Ii, costoBarco, Puertosh, Islash);
    //Se imprimen los resultados: el costo minimo de capital a capital, y cuales son el puerto y la isla que se uso 
    cout << "Costo Mínimo: " << min_cost << endl;
    cout << "Mejor puerto habilitado: " << get<0>(costoBarco[besti]) << endl;
    cout << "Mejor isla habilitada: " << get<1>(costoBarco[bestj]) << endl;

    return 0;
}

void print(vector<tuple<char,char,int>> costosPuertos, vector<tuple<char,char,int>> costosIslas, vector<tuple<char,char,int>> costoBarco){
    for (tuple<char,char,int> puertos : costosPuertos){
        cout << "('" << get<0>(puertos) << "', '" << get<1>(puertos) << "', " << get<2>(puertos) << "),";
        cout << endl;
    }
    for (tuple<char,char,int> puertos : costosIslas){
        cout << "('" << get<0>(puertos) << "', '" << get<1>(puertos) << "', " << get<2>(puertos) << "),";
        cout << endl;
    }
    for (tuple<char,char,int> puertos : costoBarco){
        cout << "('" << get<0>(puertos) << "', '" << get<1>(puertos) << "', " << get<2>(puertos) << "),";
        cout << endl;
    }
}

//Funcion Breadth-First Search modificada para que funcione con los pesos de las aristas del grafo, en lugar de la cantidad de nodos en las islas
unordered_map<char, int> bfs(Grafo& graph, char source) {
    unordered_set<char> visited;
    deque<pair<char, int>> queue;

    unordered_map<char, int> bfs_cost;
    queue.push_back(make_pair(source, 0));
    bfs_cost[source] = 0;

    while (!queue.empty()) {
        char vertex = queue.front().first;
        int dist = queue.front().second;
        queue.pop_front();

        visited.insert(vertex);

        for (auto& neighbor : graph.Ad[vertex]) {
            char next_vertex = neighbor.first;
            int edge_weight = neighbor.second;

            if (visited.find(next_vertex) == visited.end()) {
                queue.push_back(make_pair(next_vertex, dist + edge_weight));
                visited.insert(next_vertex);
                bfs_cost[next_vertex] = dist + edge_weight;
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

    for (int i = 0; i < (int)Puertosh.size(); i++) {
        for (int j = 0; j < (int)Islash.size(); j++) {
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
        int random_num = rand() % m;
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