
''' Binary Search Trees are binary trees where the left child is less than the parent and the right child is greater than the parent. This allows for efficient searching of the tree. '''

class Node:
    def __init__(self, key, val, left=None, right=None, parent=None):
        ''' Initialize the node. '''
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        ''' Return True if the node has a left child. '''
        return self.left_child
    
    def has_right_child(self):
        ''' Return True if the node has a right child. '''
        return self.right_child
    
    def is_left_child(self):
        ''' Return True if the node is a left child. '''
        return self.parent and self.parent.left_child == self
    
    def is_right_child(self):
        ''' Return True if the node is a right child. '''
        return self.parent and self.parent.right_child == self
    
    def is_root(self):
        ''' Return True if the node is the root. '''
        return not self.parent
    
    def is_leaf(self):
        ''' Return True if the node is a leaf. '''
        return not (self.right_child or self.left_child)
    
    def has_any_children(self):
        ''' Return True if the node has any children. '''
        return self.right_child or self.left_child
    
    def has_both_children(self):
        ''' Return True if the node has both children. '''
        return self.right_child and self.left_child
    

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        ''' Return the number of nodes in the tree. '''
        return self.size
    
    def __len__(self):
        ''' Return the number of nodes in the tree. '''
        return self.size
    
    def put(self, key, val):
        ''' Insert a node into the tree. '''
        if self.root:
            self._put(key, val, self.root)
        
        else:
            self.root = Node(key, val)
        
        self.size += 1

    def _put(self, key, val, current_node):
        ''' Insert a node into the tree. '''
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            
            else:
                current_node.left_child = Node(key, val, parent=current_node)
        
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            
            else:
                current_node.right_child = Node(key, val, parent=current_node)

    def __setitem__(self, k, v):
        ''' Insert a node into the tree. '''
        self.put(k, v)

    def get(self, key):
        ''' Return the value of the node with the given key. '''
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        ''' Return the value of the node with the given key. '''
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)
        
    def __getitem__(self, key):
        ''' Return the value of the node with the given key. '''
        return self.get(key)
    
    def __contains__(self, key):
        ''' Return True if the tree contains a node with the given key. '''
        if self._get(key, self.root):
            return True
        else:
            return False
        
    def delete(self, key):
        ''' Delete the node with the given key. '''
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            
            else:
                raise KeyError('Error, key not in tree')
        
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        
        else:
            raise KeyError('Error, key not in tree')
        
    def __delitem__(self, key):
        ''' Delete the node with the given key. '''
        self.delete(key)

    def remove(self, current_node):
        ''' Remove the given node. '''
        if current_node.is_leaf():
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            
            else:
                current_node.parent.right_child = None
        
        elif current_node.has_both_children():
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.key = successor.key
            current_node.payload = successor.payload
        
        else:
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                
                else:
                    current_node.replace_node_data(current_node.left_child.key,
                                                    current_node.left_child.payload,
                                                    current_node.left_child.left_child,
                                                    current_node.left_child.right_child)
            
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                                    current_node.right_child.payload,
                                                    current_node.right_child.left_child,
                                                    current_node.right_child.right_child)
                    
    def find_successor(self):
        ''' Find the successor of the current node. '''
        successor = None
        if self.has_right_child():
            successor = self.right_child.find_min()
        
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right_child = None
                    successor = self.parent.find_successor()
                    self.parent.right_child = self
        
        return successor
    
    def find_min(self):
        ''' Find the minimum node in the tree. '''
        current_node = self
        while current_node.has_left_child():
            current_node = current_node.left_child
        
        return current_node
    
    def splice_out(self):
        ''' Remove the given node. '''
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            
            else:
                self.parent.right_child = None
        
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                
                else:
                    self.parent.right_child = self.left_child
                    self.left_child.parent = self.parent
            
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                
                else:
                    self.parent.right_child = self.right_child
                    self.right_child.parent = self.parent

    def replace_node_data(self, key, value, left_child, right_child):
        ''' Replace the data of the current node with the given data. '''
        self.key = key
        self.payload = value
        self.left_child = left_child
        self.right_child = right_child
        
        if self.has_left_child():
            self.left_child.parent = self
        
        if self.has_right_child():
            self.right_child.parent = self

    def preorder(self):
        ''' Print the tree using preorder traversal. '''
        self._preorder(self.root)

    def _preorder(self, current_node):
        ''' Print the tree using preorder traversal. '''
        if current_node:
            print(current_node.key)
            self._preorder(current_node.left_child)
            self._preorder(current_node.right_child)

    def inorder(self):
        ''' Print the tree using inorder traversal. It will print the nodes in ascending order.'''
        self._inorder(self.root)

    def _inorder(self, current_node):
        ''' Print the tree using inorder traversal. '''
        if current_node:
            self._inorder(current_node.left_child)
            print(current_node.key)
            self._inorder(current_node.right_child)

    def postorder(self):
        ''' Print the tree using postorder traversal. '''
        self._postorder(self.root)
    
    def _postorder(self, current_node):
        ''' Print the tree using postorder traversal. '''
        if current_node:
            self._postorder(current_node.left_child)
            self._postorder(current_node.right_child)
            print(current_node.key) # print(current_node.payload)
    


if __name__ == "__main__":
    tree = BinarySearchTree()

    tree.put(10, 'a')
    tree.put(5, 'b')
    tree.put(15, 'c')
    tree.put(3, 'd')
    tree.put(7, 'e')

    print(tree[10])
    print(tree[5])

    print('---')
    tree.inorder()
    print('---')
    tree.preorder()
    print('---')
    tree.postorder()