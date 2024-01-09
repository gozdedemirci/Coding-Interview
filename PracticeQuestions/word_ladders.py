from collections import defaultdict
def get_mods(word):
    # val_list = ['d','o','g']
    for letter_i in range(len(word)):
        val_list = list(word)
        val_list[letter_i] = '_'
        key = ''.join(val_list)
        yield key
        
def create_mapping(wordList):
    mapping = defaultdict(set)
    for word in wordList:
        for key in get_mods(word):
            mapping[key].add(word)
    return mapping


def create_graph(mapping):
    # d_g = {dog, dag}
    # _og = [dog, log,cog]

    # dog : {}
    # dag : [dog]
    # log : [dog,cog]
    # cog : [dog,log]

    graph_dic = defaultdict(set)
    for value in mapping.values():
        # value = [dog,dag]
        for v in value:
            graph_dic[v]=graph_dic[v].union(value)
    for key, value in graph_dic.items():
        graph_dic[key] = value - {key}

    return graph_dic


def bfs(beginWord, endWord, wordList):
    wordList.append(beginWord)
    mapping = create_mapping(wordList)
    mapping_graph = create_graph(mapping)

    visited = list()
    queue = []
    output = 0

    queue.append((beginWord,1))

    while queue:
        word,w_idx = queue[0]
        queue = queue[1:]
        if word in visited:
            continue
        visited.append(word)
        # print(f'{visited=}')

        # print(f'{word=}')
        # print(f'{queue=}')
        if word == endWord:
            print(f'final= {visited=}')
            return w_idx
    
        # print(f'{output=}')
        for child in mapping_graph[word]:
            # print(f'{child=}')
            if child in visited:
                continue
            else:
                queue.append((child,w_idx+1))
    
    return 0


beginWord = "dog"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(f"beginWord = {beginWord}, endWord = {endWord}, wordList = {wordList}") 
print(bfs(beginWord, endWord, wordList))
