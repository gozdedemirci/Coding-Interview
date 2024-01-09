''' Heaps are a type of tree data structure that satisfy the heap property. There are two types of heaps: max heaps and min heaps. In a max heap, the key at the root node must be the maximum key of all keys present in the heap. The same must be true for min heaps. '''

def get_left_child(i):
    return 2 * i + 1

def get_right_child(i):
    return 2 * i + 2

def min_heapify(array, i):
    ''' Min heapify is a helper function that maintains the min heap property.'''
    left = get_left_child(i)
    right = get_right_child(i)
    smallest = i

    if left < len(array) and array[left] < array[i]:
        smallest = left

    if right < len(array) and array[right] < array[smallest]:
        smallest = right

    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest)

def build_min_heap(array):
    ''' Build min heap is a helper function that converts an array into a min heap.'''
    for i in range(len(array) // 2 - 1, -1, -1):
        min_heapify(array, i)

def heap_sort(array):
    ''' Heap sort is a comparison-based sorting algorithm that uses a max heap to sort an array in O(n log n) time.'''
    build_min_heap(array)
    sorted_array = []

    for i in range(len(array) - 1, -1, -1):
        array[0], array[i] = array[i], array[0]
        sorted_array.append(array.pop())
        min_heapify(array, 0)

    return sorted_array 

def insert(array, key):
    ''' Insert is a helper function that inserts a key into a heap.'''
    array.append(key)
    i = len(array) - 1

    while i > 0 and array[i] < array[(i - 1) // 2]:
        array[i], array[(i - 1) // 2] = array[(i - 1) // 2], array[i]
        i = (i - 1) // 2

def heap_minimum(array):
    ''' Heap minimum is a helper function that returns the minimum key of a min heap.'''
    return array[0]

def decrease_key(array, i, key):
    ''' Decrease key is a helper function that decreases the value of a key in a heap.'''
    if key > array[i]:
        return None

    array[i] = key

    while i > 0 and array[i] < array[(i - 1) // 2]:
        array[i], array[(i - 1) // 2] = array[(i - 1) // 2], array[i]
        i = (i - 1) // 2

def delete(array, i):
    ''' Delete is a helper function that deletes a key from a heap.'''
    decrease_key(array, i, float('-inf'))
    extract_min(array)

def max_heapify(array, i):
    ''' Max heapify is a helper function that maintains the max heap property.'''
    left = get_left_child(i)
    right = get_right_child(i)
    largest = i

    if left < len(array) and array[left] > array[i]:
        largest = left

    if right < len(array) and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, largest)

def build_max_heap(array):
    ''' Build max heap is a helper function that converts an array into a max heap.'''
    for i in range(len(array) // 2 - 1, -1, -1):
        max_heapify(array, i)

def heap_maximum(array):
    ''' Heap maximum is a helper function that returns the maximum key of a max heap.'''
    return array[0]


if __name__ == "__main__":
    import random
    random_array = [random.randint(0, 100) for i in range(10)]

    print('Random array:', random_array)
    build_min_heap(random_array)
    print('Min heap:', random_array)
    print('Sorted array:', heap_sort(random_array))

    random_array = [random.randint(0, 100) for i in range(10)]
    print('Random array:', random_array)
    build_max_heap(random_array)
    print('Max heap:', random_array)

    print('Heap maximum:', heap_maximum(random_array))
    insert(random_array, 101)
    print('Insert 101:', random_array)

