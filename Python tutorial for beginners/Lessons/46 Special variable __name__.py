import Calc

print(__name__)  # (__main__) When __name__ is printed in the main function, __main__ will get printed.
print(Calc.func())  # (Calc) If __name__ is printed by any module other than main we will get the module's name.

# At times you may have the need to identify entry level code. Using __name__, you can do that.
if __name__ == '__main__':
    print('This is the entry file')
