import heapq

class Graph:
    def __init__(self):
        V = {}
        Ad = {}
    def Ad(self):
        return self.Ad
    def V(self):
        return self.V

class node:
    def __init__(self):
        self.col = "WHITE"
        self.dist = float("INF")
        self.anc = ""
    def __lt__(self, x):
        return (self.dist < x.dist)
    
def w(Ad):
    return 1

def BST(G:Graph, s:node, w) :
    
    s.col = "Gray"
    s.dist = 0
    s.anc = ""
    Q = []
    heapq.heappush(Q, s)
    while (len(Q)!=0):
        u = heapq.heappop(Q)
        for v in G.Ad[u]:
            if(v.col =="WHITE"):
                v.col = "GRAY"
                v.dist = w(G.Ad[u]) + u.dist
                v.anc = u
                heapq.heappush(Q, v)
        u.col = "BLACK"


