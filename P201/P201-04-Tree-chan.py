##############################################################################
##  Problems about list
##----------------------------------------------------------------------------
"""
   * Make a list that can store the number reversely.
     1,2,3,4,5 --> [5,4,3,2,1]
"""
##  Approach 1

import time
start = time.time()
count = 10**5
nums = []
for i in range(count):
    nums.append(i)
nums.reverse()
end = time.time()
print(end-start)


##  Approach 2

import time
start = time.time()
count = 10**5
nums = []
for i in range(count):
    nums.insert(0,i)
end = time.time()
print(end-start)



##  Reasons
"""
   * Python list is not the traditional linked list.
     - It is an array or more specifically a dynamic array or vector.
     - It can allocate an array that is too big and then reallocate it 
       whenever it overflows.
     - If we can ensure that we always move to an array that is bigger than
       last by a fixed percentage (20% or even 100%), the average cost is 
       negligible.
"""



##############################################################################
##  Binary Search Tree
##----------------------------------------------------------------------------

class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
		

class BinarySearchTree(object):
    
    def __init__(self):
        self.root = None
        

    def insert(self, data):        
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_node(data,self.root)
    
    
    def insert_node(self, data, node):       
        if data < node.data:
            if node.left:
                self.insert_node(data,node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insert_node(data,node.right)
            else:
                node.right = Node(data)
                
    
    
    def remove_node(self, data, node):
        pass
    
    
    def get_predecessor(self, node):
        pass
    

    def remove(self, data):
        pass
            
    
    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)
        
    def get_min(self, node):
        if node.left:
            return self.get_min(node.left)
        return node.data
    
   
    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)
    
    
    def get_max(self, node):
        if node.right:
            return self.get_max(node.right)
        return node.data
    
    
    def traverse(self):
        pass
    
    
    def traverse_in_order(self, node):
        pass
    
    
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(20)
bst.get_min_value()
bst.get_max_value()
