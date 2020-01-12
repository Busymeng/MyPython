
class Node(object):

	def __init__(self, name):
		self.name = name;
		#we store the neighbors of a given node (so all nodes that are 
        #accessible from the actual one)
		self.adjacency_list = [];
		#whether we have already visited this node or not
		self.visited = False;
		#reference to the previous node we have visited before 
		#we can use BFS for path-finding so predecessor may be useful
		self.predecessor = None;
		
class BreadthFirstSearch(object):

	def bfs(self, start_node):
	
		#we use a queue (in this case with array representation)
		queue = [];
		queue.append(start_node);
		start_node.visited = True;
		
		#BFS we use queue; for DFS we use a stack BUT usually we implement it 
        #with recursion while the queue is not empty
		while queue:
		
			actual_node = queue.pop(0);
			
			print("{:s} ".format(actual_node.name));
			
			#we visit all the neighbors of actual_node
			for neighbor in actual_node.adjacency_list:
				#of course we do not want to visit the same nodes over and 
                #over again
				if not neighbor.visited:
					neighbor.visited = True;
					#we want to visit the neighbors of the neighbor as well
					queue.append(neighbor);

if __name__ == "__main__":					
	
	node1 = Node("A");
	node2 = Node("B");
	node3 = Node("C");
	node4 = Node("D");
	node5 = Node("E");

	node1.adjacency_list.append(node2);
	node1.adjacency_list.append(node3);
	node2.adjacency_list.append(node4);
	node4.adjacency_list.append(node5);

	bfs = BreadthFirstSearch();
	bfs.bfs(node1);