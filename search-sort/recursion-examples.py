"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)


# Test cases

print get_fib(9)
print get_fib(11)







# iterative
def getFib(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    first = 0
    second = 1
    next = first + second
    for i in range(2,position,1):
        first = second
        second = next
        next = first + second
    return next



print '+++++++++'
print 'iterative'
print getFib(0)
print getFib(1)
print getFib(2)
print getFib(3)
print getFib(4)
print getFib(5)
print getFib(9)
print getFib(11)

