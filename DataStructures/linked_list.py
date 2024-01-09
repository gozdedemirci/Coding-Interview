'''
Linked list organizes its items sequentially. Each item is called nodes and each node has a 'value' and 'pointer' information. 
Pointers saves the next node information in singly linkedlist. 
However, if we deal with doubly linkedlist, then tehre are two pointers: previous and next node informatio.
'''

class Node:
    def __init__(self, value):
        self.node = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        '''Add the new node to the end of the list.'''
        new_node = Node(value)

        if self.head == None:
            '''If head is none, then the linkedlist is empty. So, we need to set the head and tail to the new node.'''
            self.head = new_node
            self.tail = new_node

        else:
            '''If the linkedlist is not empty, then we need to add the new node to the end of the list.'''
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def prepend(self, value):
        '''Add the new node to the beginning of the list.'''
        new_node = Node(value)

        if self.head == None:
            '''If head is none, then the linkedlist is empty. So, we need to set the head and tail to the new node.'''
            self.head = new_node
            self.tail = new_node

        else:
            '''If the linkedlist is not empty, then we need to add the new node to the beginning of the list.'''
            new_node.next = self.head
            self.head = new_node
        
        self.size += 1

    def access(self, index):
        '''Access the value of the node at the given index.'''
        if index < 0 or index >= self.size or self.head == None:
            '''If getting the element is not possible, then return None.'''
            return None

        current_node = self.head
        current_index = 0

        while current_index != index:
            '''Traverse the linkedlist until we reach the given index. Takes O(n) time.'''
            current_node = current_node.next
            current_index += 1

        return current_node.node
    
    def insert_at_index(self, index, value):
        '''Insert the new node at the given index.'''
        if index < 0 or index >= self.size:
            '''If inserting the element is not possible, then return None.'''
            return None

        new_node = Node(value)

        if index == 0:
            '''If the index is 0, then we need to prepend the new node.'''
            self.prepend(value)

        elif index == self.size - 1:
            '''If the index is the last index, then we need to append the new node.'''
            self.append(value)

        else:
            '''If the index is in the middle, then we need to traverse the linkedlist until we reach the given index. Takes O(n) time.'''
            current_node = self.head
            current_index = 0

            while current_index != index - 1:
                current_node = current_node.next
                current_index += 1

            new_node.next = current_node.next
            current_node.next = new_node

        self.size += 1


    def remove_at_index(self, index):
        '''Remove the node at the given index.'''
        if index < 0 or index >= self.size:
            '''If removing the element is not possible, then return None.'''
            return None

        if index == 0:
            '''If the index is 0, then we need to remove the head. Takes O(1) time.'''
            self.head = self.head.next

        elif index == self.size - 1:
            '''If the index is the last index, then we need to remove the tail.'''
            current_node = self.head
            current_index = 0

            while current_index != index - 1:
                current_node = current_node.next
                current_index += 1

            current_node.next = None
            self.tail = current_node

        else:
            '''If the index is in the middle, then we need to traverse the linkedlist until we reach the given index. Takes O(n) time.'''
            current_node = self.head
            current_index = 0

            while current_index != index - 1:
                current_node = current_node.next
                current_index += 1

            current_node.next = current_node.next.next

        self.size -= 1

    def print(self):
        '''Print the linkedlist.'''
        current_node = self.head

        while current_node != None:
            print(current_node.node, end=' ')
            current_node = current_node.next

        print()

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    ### to be continue.

if __name__ == "__main__":
    linkedlist = SinglyLinkedList()

    linkedlist.append(1)
    linkedlist.append(2)
    linkedlist.append(3)
    linkedlist.append(4)
    linkedlist.append(5)

    linkedlist.print()

    linkedlist.prepend(0)
    linkedlist.prepend(-1)

    linkedlist.print()

    print(linkedlist.access(0))
    print(linkedlist.access(5))

    linkedlist.insert_at_index(0, -5)
    linkedlist.insert_at_index(5, 8)
    linkedlist.insert_at_index(10, 5) # it's not gonna show up in the linkedlist because the index is out of range. 

    linkedlist.print()

    linkedlist.remove_at_index(0)
    linkedlist.remove_at_index(5)
    linkedlist.remove_at_index(10) # it's not affect anything in the linkedlist because the index is out of range.

    linkedlist.print()