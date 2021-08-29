# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    permutations = []
    if len(sequence) == 1:
        permutations.append(sequence)
        return permutations        #gives me a list of a single letter
        
    else:
        #chops off first letter
        prev_sequence = sequence[1:len(sequence)]
        first_letter = sequence[0]
        
        #list of permutations without first letter
        temp_permutations = get_permutations(prev_sequence)
    
        
        #for each permutation in the previous list
        for perm in temp_permutations:
            
            #+1 to ensure loop reaches length of perm
            for i in range(len(perm) + 1):
                
                #adds to each possible slot
                possible_perm = perm[0:i] + first_letter + perm[i:(len(perm) + 1)]
                permutations.append(possible_perm)
    
        return permutations
            
        


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    print(get_permutations("a"))
    print(get_permutations("ab"))
    print(get_permutations("abc"))

