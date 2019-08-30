def reverse_string(word):
    reversed_word = ""
    for i in range(len(word)):
        reversed_word += word[len(word)-1-i]

    return reversed_word

print("hi")