def length_of_last_word(word):
    #convert string into a list
    word = word.split()

    if len(word) == 0:
        return 0

    else:
        return len(word[-1]) #-1 refers to the rightmost index

print(length_of_last_word(""))

print(length_of_last_word("Hello world!"))

print(length_of_last_word("Hello"))
