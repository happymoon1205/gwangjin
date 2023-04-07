class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None 
        self.data = data
    
    def __repr__(self):
        return str(self.data)
    
class BinarySearchTree:
    
    def __init__(self):
        self.__root = None 
    
    def insert(self, data, method='iterative'):
        if method in 'recursion':
            self.__root = self._insert_rec(self.__root, data)
        else:
            self._insert_iter(data)
    
            
    def _insert_rec(self, node, data):
        if not node:
            node = Node(data)
        else:
            if node.data > data:
                node.left = self._insert_rec(node.left, data)
            else:
                node.right = self._insert_rec(node.right, data)
    
    def _insert_iter(self,data):
        if not self.__root:
            self.__root = Node(data)
            return 
        
        new_node = Node(data)
        
        curr = self.__root
        parent = None 
        
        while(curr != None):
            parent = curr
            if curr.data > data:
                curr = curr.left 
            else:
                curr = curr.right 
        
        if parent.data > data:
            parent.left = new_node 
        else:
            parent.right = new_node   

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(25)
    bst.insert(14)
    bst.insert(30)
    bst.insert(23)
    bst.insert(18)
    bst.insert(11)
    bst.insert(21)
    bst.insert(15)
    bst.insert(11)