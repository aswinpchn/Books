person1 = {
    'name': 'aswin',
    'age': 24
}

print(person1['name'])  # Access a key value of the dictionary.

for k in person1:
    print(k)  # name age. Just looping through the Keys

print(sorted(person1))  # ['age', 'name']. Sorting the keys and returning them as a list. 'Sorted' is the method here.

print(person1.items())  # dict_items([('name', 'aswin'), ('age', 24)])
# items method returns a sorted set of key value paris in the Dictionary.

dic = {}
print(dic)  # {}

for k, v in person1.items():
    print(k, v)
# The key value pair returned by the items method can be accessed by two
# loop variables to elegantly iterate the dictionary.


# Program to give a frequency dictionary of vowels of a given word
word = 'testingword'
vowels = ['a', 'e', 'i', 'o', 'u']
dictionary = {}

for letter in word:
    if letter in vowels:
        if letter in dictionary:  # Check if letter is already key of the dictionary
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1

print(dictionary)
