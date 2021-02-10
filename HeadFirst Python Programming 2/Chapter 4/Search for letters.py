import Functions


def searchForLetters(word, letter='aeiou'):  # 'aeiou' is default parameter (If not given during call, will be default).
    """This function gives letters that are present in both words"""
    return set(word).intersection(set(letter))


print(searchForLetters('aswin', 'ap'))

print(searchForLetters('aswin'))  # Default parameter 'aeiou' will be used for letter.

print(searchForLetters(letter='abcs', word='aswin'))
# In Python, it is also possible to refer to arguments by their argument name,
# and when you do, positional ordering no longer applies. This is known as keyword assignment.
