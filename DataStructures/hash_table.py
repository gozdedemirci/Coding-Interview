''' A hash table is a data structure that maps keys to values for highly efficient lookup. It is a mapping of keys to values. Similar to a dictionary or a map in other languages. '''

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

# The hash function uses the remainder operator to get a remainder between 0 and 10. This remainder is then used as the index into the hash table.
# The collision resolution technique is linear probing with a plus 1 rehash function. The put function (put(key, data)) assumes that there will eventually be an empty slot unless the key is already present in the self.slots. It computes the original hash value and if that slot is not empty, iterates the rehash function until an empty slot occurs. If a nonempty slot already contains the key, the old data value is replaced with the new data value.
        
    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))
        
        if self.slots[hash_value] == None:
            ''' If the slot is empty, the key and data are placed in the slot. If the slot contains a different key, the search continues with the next slot (using linear probing).'''
            self.slots[hash_value] = key
            self.data[hash_value] = data
        
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            
            else:
                next_slot = self.rehash(hash_value, len(self.slots))

                control = 1                
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                    control += 1
                    if control == len(self.slots):
                        print('Hash table is full.')
                        break
                
                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                
                else:
                    self.data[next_slot] = data


# The hash function uses the remainder operator to get a remainder between 0 and 10. This remainder is then used as the index into the hash table.
    def hash_function(self, key, size):
        return key % size # remainder operator
    
    def rehash(self, old_hash, size):
        return (old_hash + 1) % size
    
    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        
        data = None
        stop = False
        found = False
        position = start_slot
        
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            
            else:
                position = self.rehash(position, len(self.slots))
                
                if position == start_slot:
                    stop = True
        
        return data
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)


if __name__ == "__main__":
    hashtable = HashTable()

    hashtable[54] = 'cat'
    hashtable[26] = 'dog'
    hashtable[93] = 'lion'
    hashtable[17] = 'tiger'
    hashtable[77] = 'bird'
    hashtable[31] = 'cow'
    hashtable[44] = 'goat'
    hashtable[55] = 'pig'
    hashtable[20] = 'chicken'

    print(hashtable.slots)
    print(hashtable.data)

    hashtable[20] = 'duck'
    print(hashtable.data)

    hashtable[52] = 'wolf'
    hashtable[42] = 'fox'
    print(hashtable.slots)
    print(hashtable.data)

    hashtable[30] = 'wolf'
    hashtable[40] = 'bear'
    print(hashtable.slots)
    print(hashtable.data)
