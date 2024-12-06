#function for the palindrome
def isPalindrome(userInput, start=0, end=None):
    # creating different endpoints based on length of user's input
    # also avoids the recurssion process
    if end is None:
        end = len(userInput) - 1
    # blank input is not palindrome
    if userInput == "":
        return False

    # confirms when string is palindrome
    if start >= end:
        return True

    #while loop ignoring non-alphabetic characters and case
    while start < end and not userInput[start].isalpha():
        start += 1
    while start < end and not userInput[end].isalpha():
        end -= 1

    # confimrs when string is not palindrome
    if userInput[start].lower() != userInput[end].lower():
        return False

    # recurssion
    return isPalindrome(userInput, start + 1, end - 1)

#function to count the vowels and consonants
def countVowelsConsonants(userInput, index=0, vowelCount=0, consonantCount=0):
  
    # recurssion is finished, return values
    if index == len(userInput):
        return vowelCount, consonantCount

    # excluding non-alphabetic strings, vowel and consonant count
    if userInput[index].isalpha():
        if userInput[index].lower() in 'aeiou':
            vowelCount += 1
        else:
            consonantCount += 1

    # recurssion
    return countVowelsConsonants(userInput, index + 1, vowelCount, consonantCount)

# main. user input + conditions for output
def main():
    userInput = input("Enter a string: ")

    if isPalindrome(userInput):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

    vowels, consonants = countVowelsConsonants(userInput)
    if vowels > consonants:
        print("The string has more vowels than consonants.")
    else:
        print("The string has more or equal consonants than vowels.")

main()
