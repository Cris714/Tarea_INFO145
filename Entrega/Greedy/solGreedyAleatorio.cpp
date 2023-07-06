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
    unordered_map<unsigned int, vector<pair<unsigned int, int>>> Ad;

    void add_edge(unsigned int src, unsigned int dest, int weight) {
        Ad[src].push_back(make_pair(dest, weight));
    }
};
//Se crea la clase Grafo para los grafos no dirigidos que usan las islas
class Grafo {
public:
    unordered_map<unsigned int, vector<pair<unsigned int, int>>> Ad;

    void add_edge(unsigned int src, unsigned int dest, int weight) {
        Ad[src].push_back(make_pair(dest, weight));
        Ad[dest].push_back(make_pair(src, weight));
    }
};

//Se declaran las funciones que se van a usar
unordered_map<unsigned int, int> bfs(Grafo& graph, unsigned int source);
unordered_map<unsigned int, int> dijkstra(GrafoD& graph, unsigned int source);
tuple<int, int, int> puertosIslas(GrafoD& Puertos, unsigned int s, Grafo& Islas, unsigned int z, vector<tuple<unsigned int, unsigned int, int>>& costoBarco, vector<unsigned int>& Puertosh, vector<unsigned int>& Islash);
void creaConexiones(vector<unsigned int> &nodos, vector<tuple<unsigned int, unsigned int, int>> &costosPuertos);
void print(vector<tuple<unsigned int,unsigned int,int>> costosPuertos, vector<tuple<unsigned int,unsigned int,int>> costosIslas, vector<tuple<unsigned int,unsigned int,int>> costoBarco);
void creaConexionesDigrafo(vector<unsigned int> nodos, vector<tuple<unsigned int, unsigned int, int>> &costoPuertos);


int main(int argc, char** argv) {
    //Se inicializan las variables
    vector<tuple<unsigned int, unsigned int, int>> costosPuertos;
    vector<tuple<unsigned int, unsigned int, int>> costosIslas;
    GrafoD Puertos;         //Grafo dirigido con los puertos
    Grafo Islas;            //Grafo no dirigido con las islas
    unsigned int Pi;                //Capital continental del Pais
    unsigned int Ii;                //Capital continental del archipielago
    vector<tuple<unsigned int, unsigned int, int>> costoBarco; //Costos de ir de los puertos a las islas
    vector<unsigned int> Puertosh;  //Puertos habilitados para viajar en barco
    vector<unsigned int> Islash;    //islas habilitadas para viajar en barco
    int n, k, m; //n = num ciudades, m = num islas, k = num ciudades con puertos.
    
    if(argc != 5)
	{
        cout << "Para definir parámetros ejecutar como: ./prog n k m seed" << endl;
        exit(1);
    }
    
    // Inicializacion de parametros
    n = atoi(argv[1]);
    k = atoi(argv[2]);
    m = atoi(argv[3]);
    srand(atoi(argv[4]));

    // Generar los nodos del grafo izquierdo con sus indices impares
    vector<unsigned int> nodosI;
    while ((int)nodosI.size() < n){
        unsigned int o = rand();
        o |= 1;
        nodosI.push_back(o);
    }

    // Generar los nodos del grafo derecho con sus indices pares
    vector<unsigned int> nodosD;
    while ((int)nodosD.size() < m){
        unsigned int o = rand();
        o = o>>1;
        nodosD.push_back(o<<1);
    }

    // Se crean conexiones hasta hacerlos grafos conexos por separado, luego a cada uno se le
    // agregan aristas de mas
    creaConexionesDigrafo(nodosI, costosPuertos);
    creaConexiones(nodosD, costosIslas);
    int maxExtraConnections = rand();
    for (int i = 0; i < (int)(maxExtraConnections%nodosI.size()/3); i++)
        costosPuertos.push_back(tuple<unsigned int, unsigned int, int> 
        (nodosI[i+1], nodosI[i+3], rand()%21));
    
    
    for (int i = 0; i < log2(rand()%nodosD.size())*2; i++){
        unsigned int nodo_1 = rand()%nodosD.size();
        unsigned int nodo_2 = rand()%nodosD.size();
        if (nodo_1 == nodo_2) continue;
        costosIslas.push_back(tuple<unsigned int, unsigned int, int> 
        (nodosD[nodo_1], nodosD[nodo_2], rand()%21));
    }

    // Se determina cuales son los puertos e islas habilitadas
    vector<unsigned int> puertos;
    vector<unsigned int> islasHabilitadas;
    vector<bool> checkeadosPuertos(nodosI.size(), false);
    for (int i = 0; i<k; i++){
        int index = rand()%(nodosI.size());
        while (index == 0 || checkeadosPuertos[index] == true){
            index = rand()%(nodosI.size());
        }
        checkeadosPuertos[index] = true;
        puertos.push_back(nodosI[index]);
    }
    vector<bool> checkeadosIslas(nodosD.size(),false);
    for (int i = 0; i < log2(m); i++){
        int index = rand()%(nodosD.size());
        while (index == 0 || checkeadosIslas[index] == true){
            index = rand()%(nodosD.size());
        }
        checkeadosIslas[index] = true;
        islasHabilitadas.push_back(nodosD[index]);
    }

    // Se conecta cada puerto con cada isla habilitada generando un costo arbitrario ya sea positivo o negativo
    for (unsigned int p : puertos){
        for (unsigned int i : islasHabilitadas){
            int costo = rand() % 31 * (rand() % 2 == 0 ? -1 : 1);
            costoBarco.push_back(tuple<unsigned int, unsigned int, int>(p, i, costo));
        }
    }

    // Se determina el nodo inicial y el nodo destino
    Pi = nodosI[0];
    Ii = nodosD[0];

    if (n <= 100) print(costosPuertos,costosIslas,costoBarco);
    cout << endl << "Nodo inicial: " << Pi << "\nNodo final: " << Ii;
    cout << endl;
    
    // Se agregan los vertices y aristas calculados a nuestra estructura de grafos y digrafos
    for (auto& [puerto1, puerto2, costop] : costosPuertos) {
        Puertos.add_edge(puerto1, puerto2, costop);
    }
    for (auto& [isla1, isla2, costop] : costosIslas) {
        Islas.add_edge(isla1, isla2, costop);
    }

    // Se calcula el costo minimo y la transicion del grafo central (puerto-islaHabilitada)
    auto [min_cost, besti, bestj] = puertosIslas(Puertos, Pi , Islas, Ii, costoBarco, puertos, islasHabilitadas);
    //Se imprimen los resultados: el costo minimo de capital a capital, y cuales son el puerto y la isla que se uso 
    cout << "Costo Mínimo: " << min_cost << endl;
    cout << "Mejor puerto habilitado: " << get<0>(costoBarco[besti-1]) << endl;
    cout << "Mejor isla habilitada: " << get<1>(costoBarco[bestj-1]) << endl;

    return 0;
}

// Escribe en pantalla las transiciones
void print(vector<tuple<unsigned int,unsigned int,int>> costosPuertos, vector<tuple<unsigned int,unsigned int,int>> costosIslas, vector<tuple<unsigned int,unsigned int,int>> costoBarco){
    for (tuple<unsigned int,unsigned int,int> puertos : costosPuertos){
        cout << "('" << get<0>(puertos) << "', '" << get<1>(puertos) << "', " << get<2>(puertos) << "),";
        cout << endl;
    }
    for (tuple<unsigned int,unsigned int,int> puertos : costosIslas){
        cout << "('" << get<0>(puertos) << "', '" << get<1>(puertos) << "', " << get<2>(puertos) << "),";
        cout << endl;
    }
    for (tuple<unsigned int,unsigned int,int> puertos : costoBarco){
        cout << "('" << get<0>(puertos) << "', '" << get<1>(puertos) << "', " << get<2>(puertos) << "),";
        cout << endl;
    }
}

//Funcion Breadth-First Search modificada para que funcione con los pesos de las aristas del grafo, en lugar de la cantidad de nodos en las islas
unordered_map<unsigned int, int> bfs(Grafo& graph, unsigned int source) {
    unordered_set<unsigned int> visited;
    deque<pair<unsigned int, int>> queue;

    unordered_map<unsigned int, int> bfs_cost;
    queue.push_back(make_pair(source, 0));
    bfs_cost[source] = 0;

    while (!queue.empty()) {
        unsigned int vertex = queue.front().first;
        int dist = queue.front().second;
        queue.pop_front();

        visited.insert(vertex);

        for (auto& neighbor : graph.Ad[vertex]) {
            unsigned int next_vertex = neighbor.first;
            int edge_weight = neighbor.second;

            if (visited.find(next_vertex) == visited.end()) {
                queue.push_back(make_pair(next_vertex, dist + edge_weight));
                visited.insert(next_vertex);
                bfs_cost[next_vertex] = dist + edge_weight; // Aqui se usa la distancia en lugar de la cantidad de nodos recorridos
            }
        }
    }

    return bfs_cost;
}
//Funcion de Dijstra para calcular el costo minimo de los puertos
unordered_map<unsigned int, int> dijkstra(GrafoD& graph, unsigned int source) {
    unordered_map<unsigned int, int> distances;
    priority_queue<pair<int, unsigned int>, vector<pair<int, unsigned int>>, greater<pair<int, unsigned int>>> pq;
    
    // Inicializar todas las distancias con infinito
    for (auto const& vertexPair : graph.Ad ) {
        unsigned int vertex = vertexPair.first;
        distances[vertex] = 99999999; // Indica infinito
    }
    
    distances[source] = 0;
    pq.push(make_pair(0, source));

    while (!pq.empty()) {
        int dist = pq.top().first;
        unsigned int vertex = pq.top().second;
        pq.pop();

        if (dist > distances[vertex]) {
            continue;
        }

        for (auto& neighbor : graph.Ad[vertex]) {
            unsigned int next_vertex = neighbor.first;
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
tuple<int, int, int> puertosIslas(GrafoD& Puertos, unsigned int s, Grafo& Islas, unsigned int z, vector<tuple<unsigned int, unsigned int, int>>& costoBarco, vector<unsigned int>& Puertosh, vector<unsigned int>& Islash) {
    // Ejecutar Dijkstra en el grafo izquierdo (Digrafo)
    unordered_map<unsigned int, int> puertos_cost = dijkstra(Puertos, s);

    // Ejecutar bfs-peso desde cada isla habilitada hasta el destino final
    unordered_map<unsigned int, int> islas_cost;
    for (unsigned int isla : Islash) {
        islas_cost[isla] = bfs(Islas, isla)[z];
    }

    // Guardar los indices de los puertos e islas habilitadas cuya suma genere el menor peso (solo una transicion)
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

    // Devolver la tupla con el menor coste y los indices calculados
    return make_tuple(min_cost, besti, bestj);
}

// Crea conexiones de nodos entregadso en el primer parametro, de manera que se forme un grafo conexo y sin ciclos, lo agrega al vector
// entregado por referencia en el segundo parametro
void creaConexiones(vector<unsigned int> &nodos, vector<tuple<unsigned int, unsigned int, int>> &costosPuertos){
    unordered_set<unsigned int> visitados;
    visitados.insert(nodos[0]);

    for (unsigned int i = 1; i < nodos.size(); i++) {
        unsigned int nodo = nodos[i];
        unsigned int conectar = nodos[rand() % i];  // Se selecciona un nodo ya conectado al azar

        while (visitados.find(conectar) == visitados.end()) {
            conectar = nodos[rand() % i];  // Se selecciona otro nodo ya conectado al azar hasta encontrar uno válido
        }

        visitados.insert(nodo);
        costosPuertos.push_back(make_tuple(nodo, conectar, rand() % 21));
    }
}

// Genera las transiciones de un digrafo que tiene un camino desde el inicial a todos los nodos.
void creaConexionesDigrafo(vector<unsigned int> nodos, vector<tuple<unsigned int, unsigned int, int>> &costoPuertos){

    unsigned int v1 = nodos.back();
    while (nodos.pop_back(), nodos.size() != 0){
        unsigned int v2 = nodos.back();
        costoPuertos.push_back(make_tuple(v2,v1,rand() % 21));
        v1 = v2;
    }
}
