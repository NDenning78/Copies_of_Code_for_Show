


# Fibonacci 4 ways

'''
Create a function to generate Fibonacci numbers. In this famous mathmatical sequence,
each nuber is the sum of the previous two, starting with values 0 and 1. Your function
should accept one argument, an index into the sequence (where 0 corresponds to the 
intitial value, 4 corresponds to the value four later, etc). 
Examples: fibonacci(0) = 0(given), fibonacci(1) = 1(given), fibonacci(2) = 1 (fib(0) + fib(1),or 0+1),
fibonacci(3) = 2 (fib(1) + fib(2), or 1+1), fibonacci(4) = 3 (1+2), fibonacci(5) = 5 (2+3), 
fibonacci(6) = 8 (3+5), fibonacci(7) = 13 (5+8), etc.
'''
    # start with 0 and 1
        # what does it mean to start with 0 and 1?
    # to get to the next number add the previous two numbers together
        # how can I know which numbers are the 2 previous numbers?
        # what does it mean to "get to" the next number?
    # stop when I have idx + 1 total values
        # how do I stop?
        # how do I start?

# First Way
def fibonacci_nrd(idx):
    if idx == 0:
        return 0
    if idx == 1:
        return 1
    a = 0
    b = 1
    for idx in range(idx - 1):
        c = a + b
        a = b
        b = c
        print("current: {}, a: {}, b: {}".format(c, a, b))
    return c
    
print(fibonacci_nrd(8))


# Second Way
def fibonacci_2(idx):    
    results = [0,1]
    if idx <= 1:
        return results[idx]
    for i in range(2, idx + 1):
        results.append(results[i -1] + results[i - 2])
    return results[len(results) - 1]

print(fibonacci_2(8))
print(fibonacci_2(5))
print(fibonacci_2(3))
print(fibonacci_2(1))
print(fibonacci_2(0))

#  Third Way RECURSION
# Dont Run This!! Too many callstacks..function in a function.
# def rfib(index):
#     if(index == 0):
#         return 0
#     if(index == 1):
#         return 1
#     else:
#         return rfib(index-1) + rfib(index-2)

# print(fibonacci_2(4))
# print(fibonacci_2(1))
# print(fibonacci_2(0))

# This one is safe to run. And it's really clean!!
# RECURSION
def recurfib(idx, a=0, b=1):
    if idx == 0:
        return a
    return recurfib(idx - 1, b, a + b)

print(recurfib(8))




