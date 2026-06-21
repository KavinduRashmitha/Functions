'''Checks Wheather the text is Palindrome or not'''
def IsPalindrome(text):
    isPalindrome=True
    for i in range(len(text)):
        if text[i]!=text[len(text)-1-i]:
            isPalindrome=False
            break
    return isPalindrome

word=input("Enter the word: ")
print(IsPalindrome(word))