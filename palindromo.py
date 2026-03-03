# Goal is to figure out if a word is a palindrome like "ana" and return true or false

def palindrome(word):
    # While the length "Word" is > 1 continue loop
    while len(word) > 1:
        # Compares fist char and last char and returns a false if word is not palindrome
        if word[0] == word[-1]:
            # Deleting characters from original list so the loop checks for next set of values
            del word[0]
            del word[-1]
        else:
            # if there is no match, it stops the loop
            print("Your Word Is Not A Palindrome :C")
            return False
    # If loop finishes then the word is a palindrome so we can print and return true
    print("Your Word Is a Palindrome!")
    return True

# Calls for the function, puts the characters in lower case, and puts them all in a list separetly
user_input = input("Please Enter Your Word: ")
user_input = user_input.lower()
char_list = list(user_input.replace(" ", ""))

palindrome(char_list)

# Todo esto se pudo resolver en un return word == word[::-1] acorde a gemini