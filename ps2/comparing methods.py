
def compare(other_word, my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    #Method 1: iteration
    #Matches length of words
    j = 0
    if len(other_word) != len(my_word):
        j = 1
        pass
    
    #Checks each letter
    else:
        for i in range(len(my_word)):
            if my_word[i] == other_word[i]:
                continue
            elif (my_word[i] != other_word[i]) and (my_word[i] == "_"):
                continue
            else:
                j += 1
    
    #Returns true if match
    if j == 0:
        return True
    else: 
        pass
    
    
    
    #Method 2: Zipping
    i = 0
    for x, y in zip(other_word, my_word):
        if x == y:
            continue
        elif x != y and y == "_":
            continue
        else:
            i += 1
            
    if len(other_word) != len(my_word):
        pass
    elif i == 0:
        return True
