from linked_list import SinglyLinkedList

'''
Queue is a linear data structure that follows the First In First Out (FIFO) principle. '''
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        ''' Add an element to the back of the queue. Takes O(1) time.'''
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            ''' Remove an element from the front of the queue. Takes O(n) time. Since the elements need to be shifted to the left.'''
            popped = self.queue[0]
            self.queue = self.queue[1:]

        return popped
    
    def display(self):
        print(self.queue)
    
    def size(self):
        return len(self.queue)
    
class Queue_LinkeList:
    def __init__(self):
        self.queue = SinglyLinkedList()
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.queue.size == 0:
            return None
        removed = self.queue.head.node
        self.queue.remove_at_index(0)
        return removed
    
    def display(self):
        self.queue.print()
    
    def size(self):
        return self.queue.size
    
if __name__ == "__main__":
    queue = Queue_LinkeList()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.display()
    queue.dequeue()
    queue.display()
    print(queue.size())
    queue.enqueue(4)
    queue.display()
    queue.dequeue()
    queue.dequeue()
    queue.display()