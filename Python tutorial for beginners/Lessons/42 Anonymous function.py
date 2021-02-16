# If you have some simple actions(One-liner) to do, and you want to do that action without defining and calling that
# function. We can use lambda in that scenario.
def sq(x):
    return x * x


print(sq(5))

sqr = lambda a: a * a  # This is the syntax for lambda functions.

print(sqr(5))