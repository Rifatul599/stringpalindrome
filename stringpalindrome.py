def palindrome(string):
    reversed_string=string[::-1]
    if string==reversed_string:
        return True
    else:
        return False

word="mom"
if palindrome(word):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")