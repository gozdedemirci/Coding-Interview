from linked_list import SinglyLinkedList
''' 
Stack is a linear data structure that follows the Last In First Out (LIFO) principle. '''

class Stack_Array:
    ''' It stores items in last-in, first-out (LIFO) order. '''
    def __init__(self):
        ''' Initialize the stack. '''
        self.stack = []
        self.size = 0

    def is_empty(self):
        ''' Return True if the stack is empty. '''
        return len(self.stack) == 0
    
    def push(self, value):
        ''' Add an element to the top of the stack. '''
        self.stack.append(value)
        self.size += 1

    def pop(self):
        ''' Remove an element from the top of the stack. '''
        if self.is_empty():
            return None
        else:
            removed = self.stack[-1]
            self.stack = self.stack[:self.size - 1]
            self.size -= 1
            return removed

    def peek(self):
        ''' Return the top element of the stack. '''
        if self.is_empty():
            return None
        else:
            return self.stack[-1]
        
    def print_stack(self):
        ''' Print the stack. '''
        print(self.stack)

class Stack_LinkedList:
    def __init__(self):
        self.stack = SinglyLinkedList()

    def is_empty(self):
        return self.stack.size == 0
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            removed = self.stack.tail.node
            self.stack.remove_at_index(self.stack.size - 1)
            return removed
        
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack.tail.node
    
    def print_stack(self):
        self.stack.print()
        

if __name__ == "__main__":
    # stack = Stack_Array()
    stack = Stack_LinkedList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())
    stack.print_stack()
    print(stack.pop())
    stack.print_stack()

     