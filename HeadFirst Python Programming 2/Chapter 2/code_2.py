# This program is to print to list of vowels are in the given word. [Unique vowels only].

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Enter the word you want to check for vowels!")
# This will prompt the user to give their input.
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

vowels.pop()

print(found)


