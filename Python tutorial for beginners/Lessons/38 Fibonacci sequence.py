# 0 1 1 2 3 5 8...

# Return nth fibonacci number. First is 0, second is 1, third is 1
def fibonacci(num):

    if num == 1:
        return 0

    if num == 2:
        return 1

    first = 0
    second = 1
    for i in range(3, num+1):
        sum = first + second
        first = second
        second = sum
    return sum


print(fibonacci(6))
