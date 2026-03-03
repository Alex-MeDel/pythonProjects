# Write a function that takes a string and returns the first character that does not repeat. Example: "swiss" -> "w"
def find_first_unique(word):
    # 1. Get string from the user then put it all in lower case
    word = word.lower()

    # 2. Count how many times each letter appears and put it in a dictionary
    counts = {}
    for char in word: 
        if char in counts:
            counts[char] += 1
        else: 
            counts[char] = 1
    print (counts)

    # 3. for each character in the original string check counts and the very first character that counts 1 wins, print this character

    for char in word:
        if counts[char] == 1:
            return char

user_word = input("Please Enter The Word: ")
result = find_first_unique(user_word)
if result:
    print(f"The first character that does not repeat is: {result}!")
else: 
    print("All Characters Repeat!!")
