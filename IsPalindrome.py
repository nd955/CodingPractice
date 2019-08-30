def is_palindrome(word):
    for i in range(int(len(word)/2)):
        if word[i] != word[len(word)-1-i]:
            return False
    return True

print(is_palindrome(""))