# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if get_guessed_word(secret_word, letters_guessed) == secret_word:
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    user_word = ""
    for char in secret_word:
        if char in letters_guessed:
            user_word += str(char)
        else:
            user_word += "_ "
        
    return user_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    new_string = ""
    for char in string.ascii_lowercase:
        if char in letters_guessed:
            continue
        else:
            new_string += char
            
    return new_string

    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #Starting
    guesses = 6
    letters_guessed = ""
    previous_guesses = ""
    print("I am thinking of a", len(secret_word), "letter long secret word!")
    
    #Running, while word not guessed yet
    while is_word_guessed(secret_word, letters_guessed) is False:
        #Guiding messages
        print("---------------------------")
        print("You have", guesses, "guesses left!")
        print("The word is", get_guessed_word(secret_word, letters_guessed))
        print("Available letters are:", get_available_letters(previous_guesses))
        
        
        #Receiving letter
        user_guess = input("Guess a letter: ")
        user_guess = user_guess.lower()
        
        #Repeating letters
        while user_guess in previous_guesses:
            print("You already guessed that letter!")
            user_guess = input("Guess another letter: ")
        
        #More than one letter
        while len(user_guess) > 1:
            print("Hey! You can only guess one letter at a time!")
            user_guess = input("Guess another letter: ")
            
        #Invalid letter
        while user_guess not in string.ascii_lowercase:
            print("That's not a valid letter!")
            user_guess = input("Guess another letter: ")
        
        #Recording previous guesses
        previous_guesses += user_guess
        
        
        #Adding letter to user's guesses
        if user_guess in secret_word:
            letters_guessed += user_guess
            print("Good guess!")
            print("---------------------------")
        else:
            print("Oops! That's not one of the letters!")
            print("---------------------------")
            guesses -= 1
        
        #Ending at 0 lives
        if guesses == 0:
            break
        
    if guesses == 0:
        print("You've lost!")
        print(secret_word, "was the word.")
    elif is_word_guessed(secret_word, letters_guessed) is True:
        print("Congrats, you win! The word was", secret_word + ".")
        
            
            

        
    
    
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



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
        


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matched = []
    temp_word = my_word.replace(" ", "")
    
    #Comparing with each word
    for word in wordlist:
        other_word = word
        x = compare(other_word, temp_word)
        if x == True:
            matched.append(word)
            
    return matched


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
       #Starting
    guesses = 6
    letters_guessed = ""
    previous_guesses = ""
    print("I am thinking of a", len(secret_word), "letter long secret word!")
    print("Type * if you need a hint!")
    
    #Running, while word not guessed yet
    while is_word_guessed(secret_word, letters_guessed) is False:
          
        #Guiding messages
        print("---------------------------")
        print("You have", guesses, "guesses left!")
        print("The word is", get_guessed_word(secret_word, letters_guessed))
        print("Available letters are:", get_available_letters(previous_guesses))
        
        
        #Receiving letter
        user_guess = input("Guess a letter: ")
        user_guess = user_guess.lower()
        
        #Repeating letters
        while user_guess in previous_guesses:
            print("You already guessed that letter!")
            user_guess = input("Guess another letter: ")
        
        #More than one letter
        while len(user_guess) > 1:
            print("Hey! You can only guess one letter at a time!")
            user_guess = input("Guess another letter: ")
            
        #Invalid letter
        while user_guess not in string.ascii_lowercase:
            if user_guess == "*":
                print("Okay! Here's some hints. Possible words are...")
                print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
                user_guess = input("Guess another letter: ")
            else:     
                print("That's not a valid letter!")
                user_guess = input("Guess another letter: ")
        
        #Recording previous guesses
        previous_guesses += user_guess
        
        
        #Adding letter to user's guesses
        if user_guess in secret_word:
            letters_guessed += user_guess
            print("Good guess!")
            print("---------------------------")
        else:
            print("Oops! That's not one of the letters!")
            print("---------------------------")
            guesses -= 1
        
        #Ending at 0 lives
        if guesses == 0:
            break
        
    if guesses == 0:
        print("You've lost!")
        print(secret_word, "was the word.")
    elif is_word_guessed(secret_word, letters_guessed) is True:
        print("Congrats, you win! The word was", secret_word + ".")
        total_score = guesses * len(secret_word)
        print("Total score is:", total_score)
         


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    secret_word = choose_word(wordlist)
   #secret_word = "apple"
    #hangman(secret_word)
    hangman_with_hints(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
