def words(input):
    # first check splits the input and eliminates the whitespaces
    data = input.split()
    # initializing an empty dictionary to hold the final value
    occurrences = {}
    # this set contains the unique values present in the list data
    unique_word = set(data)

    # the loop picks all the unique elements and checks against data list
    for word in unique_word:
        count = 0
        # second loop to compare first loop variable
        for y in data:
            # this check compares the looping variable
            if word == y:
                count = count + 1
                # the check below identifies an integer in a string, if true the string is casted to an integer
                if word.isdigit() == True:
                    word = int(word)

        occurrences[word] = count

    return occurrences
