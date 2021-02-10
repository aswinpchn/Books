# Function annotation is a way of informing the users, what the function accepts as an argument
# and what the function returns.

# Here. Using the annotations, we can be used to document
# what type is expected as input and what type will be the output
def vowelsPresent(word: str) -> set:
    """Return any vowels found in a supplied word."""  # These are called docstrings, used as comments.
    vowels = set('aeiou')
    vowels_present_in_the_word = vowels.intersection(set(word))
    return vowels_present_in_the_word


print(vowelsPresent('aswin'))

# vowelsPresent(word: str) -> set
#     Return any vowels found in a supplied word.
print(help(vowelsPresent))
