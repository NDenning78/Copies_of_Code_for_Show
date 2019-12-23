# Python Functions Intermediate I
# Neil Denning


# Tim..I didn't enjoy this as much at first.lol..I feel like I must have missed something on the platform..
# I'll go back over everything and keep practicing. The solution makes sense afterwards, but I can't see it on my own before hand. 
# I like it when I can read and comprehend the lesson on the platform before the challenge and at least get part of the challenge.. 
# Sometimes I think I get it, then something will show me I don't. hah
# good times!! ttyl. Thanks.

# import random
# def randInt(min=   0, max= 100  ):
#     num = random.random()
#     return num
#print(randInt()) # should print a random integer between 0 to 100
#print(randInt(max=50)) # should print a random integer between 0 to 50
#print(randInt(min=50)) # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500


# from random import *

# def main():

#     number = random()
#     print("My first random number using random() function: ", number)

# main()

# import random 
# random.random()

# x = 0
# while x < 10:

# This makes a number, but not random. After seeing the 
# solution it makes sense how the first random number would be used to generate the next. 

def randInt_nrd():
    random_int = None
    for int in range(0,101,3):
        if int % 11 == 1:
            random_int = int
    return random_int
    
# print(randInt_nrd())

# print(randInt()) 	# should print a random integer between 0 to 100
#print(randInt(max=50)) # should print a random integer between 0 to 50
#print(randInt(min=50)) # should print a random integer between 50 to 100
#print(randInt(min=50, max=500)) # should print a random integer between 50 and 500


import random

def randint(min=0, max=100): # function parameters defined with value.
  possible_range = max - min   # variable defined with parameter values as 
  return round(random.random() * possible_range + min)

# print(randint())
# print(randint(max=50))
# print(randint(min=50))
# print(randint(min=50, max=150))

# '''
# This is mostly just a math problem.
# First, we start by getting the possible range of numbers.
# The range will be used to multiply the number created by random, which is between 0 and 1.
# Multiplying this number will give us a number that is no greater than the range, but no less than 0.
# For instance, if we're given 20 and 70, the range is 50, so we'll first start by getting a number between 0 and 50.
# If the minimum is greater than 0, we have to make sure the number cannot be less than the minimum, so we must add the minimum value to our calculated random number.
# Since we've already accounted for the range, if we add 20 (our min from the example) to a number between 0 and 50, then mathematically it cannot be lower than 20 or higher than 70.
# Then we just round to get an integer instead of a float.
# '''


import random
def randInt(min=0, max=100):
  num = random.random() * max
  return round(num)
print(randInt())
print(randInt(max=50))
print(randint(min=50))