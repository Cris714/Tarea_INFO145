#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>
#include <queue>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

string puertosIslas(vector<vector<int>> &G, char s, vector<vector<int>> &Gp, char z);
vector<vector<int>> Dijkstra(const vector<vector<int>>& graph, int source);

int main(int argc, char** argv){
  if(argc != 4 || atoi(argv[1])< atoi(argv[2]))
	{
		cout << "Error. Debe ejecutarse como ./runStrings n k m con k<n" << endl;
		exit(EXIT_FAILURE);
	}
  int n, k, m; //n = num ciudades, m = num islas, k = num ciudades con puertos.
  n=atoi(argv[1]);
  k=atoi(argv[2]);
  m=atoi(argv[3]);
  
  
  
  return 0;
}

puertosIslas(vector<vector<int>> &G, char s, vector<vector<int>> &Gp, char z) {
  Extraer cada costo C(s,pi) de s a pi luego de ejecutar Dijkstra(G,s,w)
  Sea Puertos = {C(s, p1), C(s,p2),..., C(s,pk)}
  Islas = Vacio
  for j = 1 to log m do {
    C(qj , z) = extraer el costo de qj a z luego de ejecutar Dijkstra(Gp,qj,wp)
    Islas = Islas ∪ C(qj , z)
  }
  minCost = +inf
  besti = 0
  bestj = 0
  for i = 1 to k do {
    for j = 1 to log m do {
      costo = C(s,pi) + costoBarco(pi , qj ) + C(qj ,z)
      if (costo < minCost){
        minCost = costo
        besti = i
        bestj = j
      }
    }
  }
  return {minCost, besti, bestj }
  // se extrae el camino de s a besti de la matriz generada en Dijkstra(G, s, ω)
  // y el camino desde bestj a z de la matriz generada en Dijkstra(G′, qj , ω′)
}




vector<vector<int>> Dijkstra(const vector<vector<int>>& graph, int source) {
    int n = graph.size();
    vector<vector<int>> distance(n, vector<int>(n, INF));
    vector<bool> visited(n, false);

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    distance[source][source] = 0;
    pq.push({0, source});

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        if (visited[u]) continue;
        visited[u] = true;

        for (int v = 0; v < n; ++v) {
            if (graph[u][v] != 0) {
                int w = graph[u][v];

                if (distance[source][u] + w < distance[source][v]) {
                    distance[source][v] = distance[source][u] + w;
                    pq.push({distance[source][v], v});
                }
            }
        }
    }

    return distance;
}

int asignaPesos() {
    int n, m;
    cout << "Ingrese el número de nodos: ";
    cin >> n;
    cout << "Ingrese el número de aristas: ";
    cin >> m;

    vector<vector<int>> graph(n, vector<int>(n, 0));

    cout << "Ingrese las aristas en el formato: nodo_a nodo_b peso\n";
    for (int i = 0; i < m; ++i) {
        int a, b, w;
        cin >> a >> b >> w;
        graph[a][b] = w;
        graph[b][a] = w;
    }

    vector<vector<int>> distances;
    for (int i = 0; i < n; ++i) {
        distances.push_back(Dijkstra(graph, i));
    }

    cout << "Distancias mínimas desde cada nodo:\n";
    for (int i = 0; i < n; ++i) {
        cout << "Desde el nodo " << i << ":\n";
        for (int j = 0; j < n; ++j) {
            cout << "Nodo " << j << ": " << distances[i][i][j] << "\n";
        }
        cout << "\n";
    }

    return 0;
}
