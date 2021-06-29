def length_of_last_word(word):
    try:
        #convert string into a list
        word = word.split()

        if len(word) == 0:
            return 0

        else:
            return len(word[-1]) #-1 refers to the rightmost index
    except TypeError:
        print("Wrong type!")
        raise