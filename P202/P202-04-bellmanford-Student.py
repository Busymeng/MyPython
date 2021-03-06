##############################################################################
##  Shortest Path - Bellman Ford Algorithm
##----------------------------------------------------------------------------





##----------------------------------------------------------------------------			
node1 = Node("A");
node2 = Node("B");
node3 = Node("C");
node4 = Node("D");
node5 = Node("E");
node6 = Node("F");
node7 = Node("G");
node8 = Node("H");

edge1 = Edge(5,node1,node2);
edge2 = Edge(8,node1,node8);
edge3 = Edge(9,node1,node5);
edge4 = Edge(15,node2,node4);
edge5 = Edge(12,node2,node3);
edge6 = Edge(4,node2,node8);
edge7 = Edge(7,node8,node3);
edge8 = Edge(6,node8,node6);
edge9 = Edge(5,node5,node8);
edge10 = Edge(4,node5,node6);
edge11 = Edge(20,node5,node7);
edge12 = Edge(1,node6,node3);
edge13 = Edge(13,node6,node7);
edge14 = Edge(3,node3,node4);
edge15 = Edge(11,node3,node7);
edge16 = Edge(9,node4,node7);

edge17 = Edge(1,node1,node2);
edge18 = Edge(1,node2,node3);
edge19 = Edge(-3,node3,node1);

node1.adjacencies_list.append(edge1);
node1.adjacencies_list.append(edge2);
node1.adjacencies_list.append(edge3);
node2.adjacencies_list.append(edge4);
node2.adjacencies_list.append(edge5);
node2.adjacencies_list.append(edge6);
node8.adjacencies_list.append(edge7);
node8.adjacencies_list.append(edge8);
node5.adjacencies_list.append(edge9);
node5.adjacencies_list.append(edge10);
node5.adjacencies_list.append(edge11);
node6.adjacencies_list.append(edge12);
node6.adjacencies_list.append(edge13);
node3.adjacencies_list.append(edge14);
node3.adjacencies_list.append(edge15);
node4.adjacencies_list.append(edge16);

vertex_list = (node1,node2,node3, node4, node5, node6, node7, node8);
edge_list = (edge1,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9,\
             edge10,edge11,edge12,edge13,edge14,edge15,edge16);
edge_list = (edge17, edge18, edge19);

algorithm = BellmanFord();
algorithm.calculate_shortest_path(vertex_list, edge_list, node1);
algorithm.get_shortest_path_to(node7);
