'''
Write a function that can take a string and return a list of bigrams.
'''

## Input Ex: 'Have free hours and love children?'

def bigram(sentence):
    # split sentence into words
    words = sentence.split()

    # create a list of bigrams
    bigrams = []
    for i in range(len(words)-1):
        if i+1 < len(words):
            bigrams.append(words[i] + ' ' + words[i+1])
    return bigrams

print(bigram('Have free hours and love children?'))