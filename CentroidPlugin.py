import networkx

def centroid(GG):
 n = len(GG.nodes())#10
 
 G = []
 f = []
 F = {}
 #F = []
 C = []
 V = []
 for i in range(n):
   G.append([])
   f.append([])
   #F.append(0)
   C.append(0)
   V.append([])
   for j in range(n):
      G[i].append(0)#float("inf"))
      f[i].append(float("inf"))#0)
      V[i].append(0)


 # From Smart and Slater, 1999
 def addEdge(G, x, y, w):
   G[x][y] = w
   G[y][x] = w

 for key in GG.adj:
      for key2 in GG.adj[key]:
         if ('weight' in GG.adj[key][key2] and GG.adj[key][key2]['weight'] != 0):
            addEdge(G, list(GG.nodes()).index(key), list(GG.nodes()).index(key2), GG.adj[key][key2]['weight'])
         else:
            addEdge(G, list(GG.nodes()).index(key), list(GG.nodes()).index(key2), 1)
 #addEdge(G, 0, 1)
 #addEdge(G, 1, 2)
 #addEdge(G, 1, 5)
 #addEdge(G, 1, 9)
 #addEdge(G, 2, 3)
 #addEdge(G, 2, 4)
 #addEdge(G, 3, 4)
 #addEdge(G, 4, 6)
 #addEdge(G, 5, 6)
 #addEdge(G, 6, 7)
 #addEdge(G, 6, 8)

 # All Pairs
 for k in range(n):
   for j in range(n):
      for i in range(n):
         if (i != j and j != k):
            if (G[i][j] < G[i][k]*G[k][j]):
               G[i][j] = G[i][k]*G[k][j]


 for u in range(n):
   for v in range(n):
    #print("++++++++++++++++++++++")
    #print("COMPARING TO NODE: "), 
    #print(list(GG.nodes())[v])
    if (u != v):
      Vuv = 0
      Vvu = 0
      #print("For other node: ", v
      for w in range(n):
       if (w != u and w != v):
         if (G[w][u] > G[w][v]):
            #print("Node ", GG.nodes()[w], " is closer to ", GG.nodes()[u], " than ", GG.nodes()[v]
            Vuv += 1
            V[u][v] += 1
         elif (G[w][v] > G[w][u]):
            #print("Node ", GG.nodes()[w], " is closer to ", GG.nodes()[v], " than ", GG.nodes()[u]
            Vvu += 1
            V[v][u] += 1
         #else:
         #   print("Node ", GG.nodes()[w], " is the same distance to ", GG.nodes()[v], " as ", GG.nodes()[u]
      #print(Vuv, " ", PUT BACK FOR TABLE
      f[u][v] = Vuv - Vvu
    #else:
    #print("X"), 
    #print(" "),
    #print("++++++++++++++++++++++")
   #F[u] = min(f[u])
   F[list(GG.nodes())[u]] = min(f[u])

 #print("Better Options: ")
 #for i in range(n):
 #  print(i), 
 #  print(": "), 
 return F
 #print(max(F))


class CentroidPlugin:
   def input(self, filename):
      self.GGG = networkx.read_gml(filename)
      
   def run(self):
      F = centroid(self.GGG)
      curmax = "notset"
      for key in F:
         if (curmax == "notset" or F[key] > curmax):
            self.centroids = [key]
            curmax = F[key]
         elif F[key] == curmax:  # Ties
            self.centroids.append(key)

   
   def output(self, filename):
      print("Centroids: "),
      print(self.centroids)




