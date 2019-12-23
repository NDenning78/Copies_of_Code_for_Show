# # Python Fundamentals
# # Neil Denning


# # These are lessons examples

# # Code BLock Key Words -below

# #  def (functions)
# # if, elif, else (conditional statements)
# # for, while (loops)
# # Class (classes)
# # --------------------------------------------------------------|


# x = 10
# if x > 50:
# 	print("bigger than 50")
# else:
# 	print("smaller than 50")

# --------------------------------------------------------------|
# class EmptyClass:
#     pass


# for val in my_string:
#     pass

# --------------------------------------------------------------|
#  DATA TYPES 

#  PRIMITIVE data types = boolen values, numbers, strings.

# boolean
is_hungry = True
has_freckles = False

# numbers
age = 35 # storing an int
weight = 160.57 # storing a float

# strings
name = "Joe Blue"

# --------------------------------------------------------------|
# COMPOSITE data types = tuples, lists, dictionaries

# tuples
dog = ('Bruce', 'cocker spaniel', 19, False)
# print(dog[0])		# output: Bruce


# dog[1] = 'dachshund'	
# ERROR: cannot be modified ('tuple' object does not support item assignment)

# lists
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
# print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
# print(ninjas)	# output: ['Francis', 'Oliver']

# dictionaries
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists
new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
# print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
# print(w)		# output: 160.2
# print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        


# --------------------------------------------------------------|
# COMMON FUNCTIONS
# print(type("2.63"))		# output: <class 'float'>
# print(type(new_person))		# output: <class 'dict'>

# print(len(new_person))		# output: 4 (the number of key-value pairs)
# print(len('Coding Dojo'))	# output: 11

# Type casting or explicit type conversion

# print("Hello" + 42)			
# the above code will output: TypeError

# print("Hello" + str(42))		# output: Hello 42

total = 35
user_val = "26"

# total = total + user_val		
# the above code will output: TypeError

total = total + int(user_val)
# print(total)
# print(type(total))		# total will be 61

# --------------------------------------------------------------|
# CONDITIONAL STATEMENTS
# x = 12
# if x > 50:
# 	print("bigger than 50")
# else:
# 	print("smaller than 50")
# # because x is not greater than 50, the second print statement is the only one that will execute

# x = 55
# if x > 10:
# 	print("bigger than 10")
# elif x > 50:
# 	print("bigger than 50")
# else:
# 	print("smaller than 10")
# # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

# if x < 10:
# 	print("smaller than 10")
# nothing happens, because the statement is false   



# --------------------------------------------------------------|
#  LOOPS
# def loops_examples():
	# for x in range(0, 10, 1):
		# for x in range(0, 10):	# increment of +1 is implied
			# for x in range(10):	# increment of +1 and start at 0 is implied
			# BE CAREFUL. NOT SURE WHAT THIS WILL DO. 
			# THREE NESTED FOR LOOPS.

# for x in range(0, 10, 2):
#     print(x)
# # output: 0, 2, 4, 6, 8


# for x in range(5, 1, -3):
#     print(x)
# # output: 5, 2


# # FOR LOOPS THRU LISTS (Objects)
# my_list = ["abc", 123, "xyz"]
# for i in range(0, len(my_list)):
#     print(i, my_list[i])
# # output: 0 abc, 1 123, 2 xyz
    
    
# # OR 
    
# for v in my_list:
#     print(v)
# output: abc, 123, xyz



#  FOR LOOPS THRU DICTIONARIES

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    # print(k)

# output: name, language

    print(my_dict[k])




my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python




# another way to iterate through the keys
my_dict = { "name": "Noelle", "language": "Python" }
for key in my_dict.keys():
     print(key)



#to iterate through the values
my_dict = { "name": "Noelle", "language": "Python" }
for val in my_dict.values():
     print(val)




#to iterate through both keys and values
my_dict = { 'name':'Noelle', "language": "Python" }
for key, val in my_dict.items():
     print(key, " = ", val)



# --------------------------------------------------------------|
# WHILE LOOPS 
# WHILE
for count in range(0,5):
    print("looping - ", count)

lst = [2,4,6]
for count in lst:
    print("looping - ", count)

count = 0
while count < 5:
    print("looping - ", count)
    count += 1
#  The "for" and "while" loop above run the same.

# while <expression>:
    # do something, including progress towards making the expression False. Otherwise we'll never get out of here!

# ELSE
y = 3
while y > 0:
    print(y)
    y = y - 3
else:
    print("Final else statement")

# LOOP CONTROL
# BREAK >>> REFER TO DIAGRAM CHART
for val in "string":
    if val == "n":
        break
    print(val)
# output: s, t, r

# CONTINUE >>> REFER TO DIAGRAM CHART
for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement")
# output: 3, 2, 1

# # --------------------------------------------------------------|
# #  FUNCTIONS

def add(a,b):	# function name: 'add', parameters: a and b
    x = a + b	# process
    return x	# return value: x

new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
print(new_val)    # the result of the add function gets sent back to and saved into new_val, so we will see 8

# Parameters and Arguements

def say_hi(name):
    print("Hi, " + name)

# invoking the function 3 times, passing in one argument each time
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')

# Returning Values
def say_hi(name):
    return "Hi " + name
greeting = say_hi("Michael") # the returned value from say_hi function gets assigned to the 'greeting' variable
print(greeting) # this will output 'Hi Michael'

def add(a, b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2
print(sum1)
print(sum2)
print(sum3)


# --------------------------------------------------------------|
#  DEFAULT PARAMETERS 

def beCheerful(name='', repeat=4):		# set defaults when declaring the parameters

	# print(f"good morning {name}\n" * repeat)  # this one runs python 3.7

	print("good morning {}".format(name) * repeat)  # this runs on python 2.7

beCheerful()				# output: good morning (repeated on 2 lines)
beCheerful("Tim"+" ", repeat=1)		        # output: good morning tim (repeated on 2 lines)
beCheerful(name="John"+" ")			# output: good morning john (repeated on 2 lines)
beCheerful(repeat=3)			# output: good morning (repeated on 6 lines)
beCheerful(name="Michael"+" Time to go! ", repeat=2)	# output: good morning michael (repeated on 5 lines)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
beCheerful(repeat=3, name="kb")		# output: good morning kb (repeated on 3 lines)

 



# # --------------------------------------------------------------|
 






# # --------------------------------------------------------------|
 





