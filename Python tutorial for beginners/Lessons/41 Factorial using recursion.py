# Here we are trying to implement factorial program using recursion.
# First we know that 5! = 5*4*3*2*1, then if you closely see, 5! = 5*4!, then 4! = 4*3! and so on.
# So, key to solving the problem witg recursion is breaking down and also knowing what is the end condition.
# Best explanation for a recursion.
# https://www.youtube.com/watch?v=TqqQld6m6A0&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=45

def factorial(x):
    if x == 1:
        return 1

    ans = x * factorial(x-1)
    return ans


print(factorial(5))
