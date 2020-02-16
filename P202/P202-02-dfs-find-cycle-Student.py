# Python Program to detect cycle in an undirected graph 
"""
   We do a DFS traversal of the given graph. 
   
   1. For every visited vertex ‘v’, if there is an adjacent ‘u’ such that u is 
      already visited and u is not parent of v, then there is a cycle in graph. 
   2. If we don’t find such an adjacent for any vertex, we say that there is 
      no cycle. 
      
   The assumption of this approach is that there are no parallel edges 
   between any two vertices.

"""








#-----------------------------------------------------------------------------
# Create a graph given in the above diagram 
g = Graph(5) 
g.addEdge(1, 0) 
g.addEdge(0, 2) 
g.addEdge(2, 1) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 

if g.isCyclic(): 
	print("Graph contains cycle")
else : 
	print("Graph does not contain cycle ")
    
    
#-----------------------------------------------------------------------------    
g1 = Graph(3) 
g1.addEdge(0,1) 
g1.addEdge(1,2) 


if g1.isCyclic(): 
	print("Graph contains cycle")
else : 
	print("Graph does not contain cycle ")

