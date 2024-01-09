''' A Trie is a tree-like data structure that stores a set of strings.'''

class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        ''' Insert a word into the trie. '''
        current_node = self.root
        
        for char in word:
            ''' Traverse the trie until we reach the end of the word. '''
            if char not in current_node:
                ''' If the character is not in the trie, then add it. '''
                current_node[char] = {}
            
            current_node = current_node[char]
        
        current_node['*'] = True
    
    def search(self, word):
        ''' Return True if the word is in the trie. '''
        current_node = self.root
        
        for char in word:
            ''' Traverse the trie until we reach the end of the word. '''
            if char not in current_node:
                ''' If the character is not in the trie, then return False. '''
                return False
            
            current_node = current_node[char]
        
        if '*' in current_node:
            ''' If the word is in the trie, then return True. '''
            return True
        
        return False
    
    def startsWith(self, prefix):
        ''' Return True if there is a word in the trie that starts with the given prefix. '''
        current_node = self.root
        
        for char in prefix:
            ''' Traverse the trie until we reach the end of the prefix. '''
            if char not in current_node:
                ''' If the character is not in the trie, then return False. '''
                return False
            
            current_node = current_node[char]
        
        return True
    
    def remove(self, word):
        ''' Remove a word from the trie. '''
        current_node = self.root
        
        for char in word:
            ''' Traverse the trie until we reach the end of the word. '''
            if char not in current_node:
                ''' If the character is not in the trie, then return False. '''
                return False
            
            current_node = current_node[char]
        
        if '*' in current_node:
            ''' If the word is in the trie, then remove it. '''
            del current_node['*']
            return True
        
        return False
    
    def print(self):
        ''' Print the trie. '''
        current_node = self.root
        self.print_helper(current_node)

    def print_helper(self, current_node):
        ''' Print the trie using a helper function. '''
        for key in current_node:
            if key == '*':
                break
            else:
                print(key)
            self.print_helper(current_node[key])

if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')
    trie.insert('app')
    trie.insert('ap')

    trie.print()
    print(trie.search('app'))

    print(trie.search('bob'))

    print(trie.startsWith('app'))

    print(trie.remove('le'))
    trie.print()
    trie.insert('home')
    trie.print()