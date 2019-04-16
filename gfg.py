class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                      for row in range(vertices)] 
  
    def makeGraph(self, edges):
    	for edge in edges:
    		u, v, x = edge
    		self.graph[u - 1][v - 1] = x
    	#print(self.graph)

    def printSolution(self, dist): 
        print("Vertex tDistance from Source")
        for node in range(self.V): 
            print(node,"t",dist[node])
  
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 
  
        # Initilaize minimum distance for next node 
        min = 10000000
        #print(sptSet)

        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V): 
        	#print(dist[v], sptSet[v])
        	if dist[v] < min and sptSet[v] == False: 
        		min = dist[v] 
        		min_index = v 
        try:
            return min_index 
        except:
            return None
  
    # Funtion that implements Dijkstra's single source  
    # shortest path algorithm for a graph represented  
    # using adjacency matrix representation 
    def dijkstra(self, src, sink=3): 
  
        dist = [10000000] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  		
        for cout in range(self.V): 
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 
  
            # Put the minimum distance vertex in the  
            # shotest path tree 
            if u is not None:
                sptSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                if u is not None and self.graph[u][v] > 0 and sptSet[v] == False and \
                   	dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v] 
        dist = [-1 if a == 10000000 else a for a in dist]
        print(dist[sink])
        #self.printSolution(dist) 
  
n, m = map(int, input().split(' '))
weights = []
for i in range(m):
    weights.append(list(map(int, input().split(' '))))
source, sink = map(int, input().split(' '))

#print(weights)
# Driver program 
g  = Graph(4) 
g.makeGraph(weights)#[[1, 2, 1], [4, 1, 2], [2, 3, 2], [1, 3, 5]])
g.dijkstra(source - 1, sink - 1)