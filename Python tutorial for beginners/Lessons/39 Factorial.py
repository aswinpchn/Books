# 3! = 3*2*1
# 5! = 5*4*3*2*1

def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact = fact * i
    return fact


print(factorial(5))
