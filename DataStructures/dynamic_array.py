'''
Dynamic Array
'''

class DynamicArray:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.length = 0
        self.data = [None] * capacity

    def is_empty(self):
        return self.length == 0
    
    def resize(self):
        '''Resize the array to double its capacity.'''
        self.capacity *= 2
        new_data = [None] * self.capacity

        if self.data is not None:
            '''Copy the data from the old array to the new array. Takes O(n) time.'''
            for i in range(self.length):
                new_data[i] = self.data[i]

        self.data = new_data
    
    def access(self, index):
        '''Access an element in the array in O(1) time.'''
        if index < 0 or index >= self.length:
            return None
        else:
            return self.data[index]
        
    def append(self, value):
        '''Add an element to the end of the array in O(1) time.'''
        if self.length == self.capacity:
            self.resize()
        
        self.data[self.length] = value
        self.length += 1

    def insert_at_index(self, index, value):
        '''Insert an element at the given index in O(n) time.'''
        if index < 0 or index >= self.length:
            '''If inserting the element is not possible, then return None.'''
            return None

        if self.length == self.capacity:
            self.resize()

        for i in range(self.length, index, -1):
            '''Shift the elements to the right. Takes O(n) time.'''
            self.data[i] = self.data[i - 1]

        self.data[index] = value
        self.length += 1

    def delete_at_index(self, index):
        '''Delete an element at the given index in O(n) time.'''
        if index < 0 or index >= self.length:
            '''If deleting the element is not possible, then return None.'''
            return None

        for i in range(index, self.length):
            '''Shift the elements to the left. Takes O(n) time.'''
            self.data[i] = self.data[i + 1]

        self.length -= 1


if __name__ == '__main__':
    new_array = DynamicArray(capacity=3)

    new_array.append(1)
    new_array.append(2)
    new_array.append(3)

    print(new_array.data)

    new_array.insert_at_index(1, 4)

    print(new_array.data)

    new_array.delete_at_index(3)

    print(new_array.data)