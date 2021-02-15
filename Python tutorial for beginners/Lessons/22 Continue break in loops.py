# Continue and break keywords work as in other languages.

for i in range(10):
    if i == 3:  # In python there is no curly braces, so to write empty conditions, we have to use 'pass' in python.
        pass
    print(i)

for i in range(10):
    if i == 9:  # Break will break from the loop instantly.
        print(i, 'is 9')
        break
    print(i)

for i in range(10):
    if i == 5:  # continue will just redirect control to for loop instantly.
        print(i, 'is 5')
        continue
    print(i)

