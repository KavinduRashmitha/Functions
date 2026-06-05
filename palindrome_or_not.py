"***This is a Function to Findout whether the Give text is Palindrome or Not***"
def IsPalindrome(text):
    is_palindrom=True
    f_word=text[:]
    b_word=text[::-1]
    if (f_word)!=(b_word):
        is_palindrom=False
    return is_palindrom

word=input("Enter the text: ")
print(IsPalindrome(word))