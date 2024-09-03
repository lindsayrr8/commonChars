
# This program asks the user to input two strings and prints:
# --- the characters that occur in both strings.
# --- the characters that occur in one string but not the other.
# --- the letters that don't occur in either string.



def main():

    
    # Creates two empty sets to hold the strings
    # & gets two words as user input; converts inputs to lower.
    setOne = set(input("Enter a word: ").lower())
    setTwo = set(input("Enter a second word: \n").lower())
    
    # Finds common characters between the two words.
    commonChars = (setOne.intersection(setTwo))
    
    # Finds difference in characters between the two words.
    differentChars = (setOne.difference(setTwo))

    # Creates a set of the alphabet to evaluate any characters
    # that are not present in the strings.
    alphabet = set("abcdefghijklmnopqrstuvqxyz")

    # Creates a set that combines both strings as one.
    bothWords = (setOne.union(setTwo))

    # New set to evaluate any missing alphabetical characters:
    missingChars = (alphabet.union(differentChars))
    
    # Prints the resulting sets to the user.
    print("The characters the words have in common: ",commonChars if commonChars else "None")
    print(" ")
    print("The difference between the characters: ",differentChars if differentChars else "None")
    print(" ")
    print("The remaining characters not used: ", missingChars)



main()
