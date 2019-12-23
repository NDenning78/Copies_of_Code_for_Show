# Functions Intermediate II
# Neil Denning

# I'll practice and keep trying to understand the syntax, the code, and the behavior, but
# I'm going to start this track over from the beginning..I'm really confused. 
# I'll do my best to recap and keep going with flask. good times!!


#  
# 
# -----------------------------------------------------|  
# 1. Update values in dictionary lists.


# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# 1 . 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x = [ [5,2,3], [10,8,9] ]
# def change_val(lst):
#     lst = 15
#     return lst

# result_1 = change_val(x)
# print(result_1)

x = [ [5,2,3], [10,8,9] ] # this is like multidimensional arrays. List inside of a list.<<<<<---BEHAVIOR
# x[[1][0]] = 15   # first identify the variable name, then the index, then the following index of the inner list. no commas, no seperation. <<<<<---BEHAVIOR
# variable, index, index. <<<<<---BEHAVIOR
# print(x)


# 1. 2. Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},    # this is a list with two lists inside.  <<<<<---BEHAVIOR
     {'first_name' : 'John', 'last_name' : 'Rosales'}       # two items at two indexes with two key value pairs inside.  <<<<<---BEHAVIOR

]
# students.last_name[0] = "Bryant"
students[0]['last_name'] = "Bryant" # first identify the variable name, then the index, then the name of the key or value. <<<<<---BEHAVIOR 


# 1. 3. In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],    # this is a list with two items inside as well , but a little different.  <<<<<---BEHAVIOR
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']   #the keys have lists of values. to access the values you have to identify  <<<<<---BEHAVIOR
                                                #the variable, then key by name 'soccer', then the index of the value. <<<<<---BEHAVIOR
}
# sports_directory[1][0] = "Andres"   this was mine!! so close- instead of [1] it should be 'soccer'. same place different name..
# sports_directory['soccer'][0] = "FunTimes!!"
# print(sports_directory)
sports_directory['soccer'][0] = "Andres" # we state the name of the variable, the 'key' of the list, and then the value of 'key' list by index number.  <<<<<---BEHAVIOR
# print(sports_directory)


# 1. 4. Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ] # this has one item at index zero..not two indexes..pay attention to how the {} made it one item... <<<<<---BEHAVIOR
# z['y'] = 30
z[0]['y'] = 30 # this looks at index zero, which we now see is the {} as one item at index zero, then it specifies 'y' key inside {} to have value of '30'. <<<<<---BEHAVIOR
# print(z)

#  I failed at all of these...the solution showed me how. I'll practice.
#  it makes sense.
# -----------------------------------------------------|  

# 2. Iterate through a list of dictionaries
# Create a function iterateDictionary(some_list) that, given a list of 
# dictionaries, the function loops through each dictionary in the list 
# and prints each key and the associated value. 
# For example, given the following list:
# I couldn't see how to write this at all.

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},    # this is another list inside of a list. There are 4 indexes or items in the dictionary called students.<<<<<---BEHAVIOR
         {'first_name' : 'John', 'last_name' : 'Rosales'},      # each inner list has two key value pairs. <<<<<---BEHAVIOR
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},      # to access these values you have to state the name of the dictionary, then the key name, and then the value. <<<<<---BEHAVIOR
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
students[2]['first_name'] = "Coding"
students[2]['last_name'] = 'Dojo'
# print(students[2])
#  after the solution and making notes and comments to myself about the behavior I was able to write students[2].

def iterate_dictionary(some_list):
    for curr_dict in some_list: # this iterates thru the list provided as an arguement to parameter 'some_list'
        display_str = ''
        for curr_key in curr_dict.keys():
            # display_str += f"{curr_key}-{curr_dict[curr_key]}"
            display_str += ("{}{}".format(curr_key, curr_dict[curr_key]))
        display_str = display_str[:len(display_str)]
        print(display_str)

# iterate_dictionary(students)
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},    # this is another list inside of a list. There are 4 indexes or items in the dictionary called students.<<<<<---BEHAVIOR
         {'first_name' : 'John', 'last_name' : 'Rosales'},      # each inner list has two key value pairs. <<<<<---BEHAVIOR
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},      # to access these values you have to state the name of the dictionary, then the key name, and then the value. <<<<<---BEHAVIOR
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ] 
def iterate_dictionary(some_list):
    for idx in range(len(some_list)): # this iterates thru the list provided as an arguement to parameter. the iterator is the 'key'.
        student_dict = some_list[idx]
        # **build a string 
        for key in some_list[idx]:
            # print(some_list[idx][key])
            print(key, '-', some_list[idx][key])
            # ** add to that string ^^^
        # * print that string

# iterate_dictionary(students)

# bonus**

 

# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

'''
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
'''


# -----------------------------------------------------|  
# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, 
# given a list of dictionaries and a key name, the function prints 
# the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# def iterate_dictionary2(key, some_list):
#     for curr_dict in some_list:
#         print(curr_dict[key])

def iterate_dictionary2(key_name, some_list):
    for idx in range(len(some_list)):
        print(some_list[idx][key_name])


# iterate_dictionary2('first_name', students)
# iterate_dictionary2('last_name', students)

# Michael
# John
# Mark
# Kb 

# Jordan
# Rosales
# Guillen
# Tonel


# -----------------------------------------------------|  
# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values 
# are all lists, prints the name of each key along with the size of its list, 
# and then prints the associated values within each key's list. For example:

# def printInfo():
# I need so much help understanding this..I'll keep practing and watching the videos over and over. I'm waiting for a major ahah moment!
 
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# def print_info(some_dict):
#     for key in some_dict.keys():
#         # print(f"{len(some_dict[key])}{key.upper()}")
#         print("{},{}".format(len(some_dict[key]), key.upper()))
#         for item in some_dict[key]:
#             print(item)
#         print('\n')

def printInfo_helpme(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key.upper())
        for val in some_dict[key]:
            print(val)

printInfo_helpme(dojo)
# print_info(dojo)

# output:
'''
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago 
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
'''

# -----------------------------------------------------|  
# I have so much to still comprehend about this weeks material..I don't know how much JS helped. It might have made it harder on my brain.
# Either way, I'll practice practice practice..I'm trying to find time to read the algo book, do the algo app, stay current on lectures and assignments, 
# but the more I learn the more confused I'm getting. I need it to click together somehow, in my brain..I hope it happens soon!! 
# ttyl Tim!
# THE END..