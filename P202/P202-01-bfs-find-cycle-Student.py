##############################################################################
#
#  Python3 program to detect cycle in an undirected graph using BFS.
#
############################################################################## 
"""
   We do a BFS traversal of the given graph. 
   
   1. For every visited vertex ‘v’, if there is an adjacent ‘u’ such that u 
      is already visited and u is not parent of v, then there is a cycle 
      in graph. 
      
   2. If we don’t find such an adjacent for any vertex, we say that there is 
      no cycle. 
      
   We use a parent array to keep track of parent vertex for a vertex so 
   that we do not consider visited parent as cycle.
      
   The assumption of this approach is that there are no parallel edges 
   between any two vertices.
   
"""



# Driver Code 


