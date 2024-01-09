'''
   Given two strings A and B, return whether or not A can be shifted some number of times to get B. 
'''

## Input: A = 'abcde'; B = 'cdeab' --> can be shifted

def shifting(A, B):
    # check if length of A and B are equal
    if len(A) != len(B):
        return False
    
    # check if A and B are equal
    if A == B:
        return True
    
    # check if A can be shifted to get B
    for i in range(len(A)):
        if A[i:] + A[:i] == B:
            return True
    return False

print(shifting('abcde', 'cdeab'))