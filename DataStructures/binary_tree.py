'''
Binary trees are trees where each node has at most two children. They are hierarchical data structures.'''

class BinaryTree:
    def __init__(self, data):
        self.key = data
        self.left_child = None
        self.right_child = None
    
    def insert_left(self, newNode):
        ''' Insert a node to the left of the current node. If there is already a node there, push it down one level and make the new node the left child.'''
        if self.left_child == None:
            self.left_child = BinaryTree(newNode)
        
        else:
            new_node = BinaryTree(newNode)
            new_node.left_child = self.left_child
            self.left_child = new_node
    
    def insert_right(self, newNode):
        ''' Insert a node to the right of the current node. If there is already a node there, push it down one level and make the new node the right child.'''
        if self.right_child == None:
            self.right_child = BinaryTree(newNode)
        
        else:
            new_node = BinaryTree(newNode)
            new_node.right_child = self.right_child
            self.right_child = new_node
    
    def get_right_child(self):
        ''' Return the right child of the current node. '''
        return self.right_child
    
    def get_left_child(self):
        ''' Return the left child of the current node. '''
        return self.left_child

    def set_root_val(self, obj):
        ''' Set the value of the current node. '''
        self.key = obj
    
    def get_root_val(self):
        ''' Return the value of the current node. '''
        return self.key

    def preorder(self):
        ''' Print the tree using preorder traversal. '''
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()
        
    def inorder(self):
        ''' Print the tree using inorder traversal. '''
        if self.left_child:
            self.left_child.inorder()
        print(self.key)
        if self.right_child:
            self.right_child.inorder()

    def postorder(self):
        ''' Print the tree using postorder traversal. '''
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.key)

# class BinarySearchTree:
#     ## todo
#     break

if __name__ == '__main__':
    tree = BinaryTree('a')

    print(tree.get_root_val())
    print(tree.get_left_child())
    tree.insert_left('b')
    print(tree.get_left_child())
    print(tree.get_left_child().get_root_val())
    tree.insert_right('c')
    print(tree.get_right_child())
    print(tree.get_right_child().get_root_val())
    tree.get_right_child().set_root_val('hello')
    tree.insert_right('d')
    tree.insert_right('hey')
    print(tree.get_right_child().get_root_val())
    print("-------------------- Preorder --------------------")
    tree.preorder()
    print("-------------------- Inorder --------------------")
    tree.inorder()
    print("-------------------- Postorder --------------------")
    tree.postorder()