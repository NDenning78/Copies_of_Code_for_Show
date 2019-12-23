# For Loop Basic II
# Neil Denning

# Tim, The last two I couldn't get at all. The maximum and minimum I got halfway, I got the easy part I guess, 
# the max and min, not the False for an empty list. I left my attempt down below, commented out.
# I had to copy the solution to study and analyze the behavior. I'll keep studying and 
# writing test cases to get more comfortable..thanks!
# -----------------------------------------------------|  
# 1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#    Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = "big"
    return lst

x = biggie_size([-1,3,5,-5])
# print(x)

# -----------------------------------------------------|  
# 2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
#    (Note that zero is not considered to be a positive number).
#    Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#    Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] > 0:
            count += 1
    lst[len(lst)-1] = count
    return lst

x = count_positives([1,6,-4,-2,-7,-2])
# print(x)

# -----------------------------------------------------|  
# 3. Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
#    Example: sum_total([1,2,3,4]) should return 10
#    Example: sum_total([6,3,-2]) should return 7
def sum_total(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return sum

x = sum_total([1,2,3,4])
# print(x)

# -----------------------------------------------------|  
# 4. Average - Create a function that takes a list and returns the average of all the values.
#    Example: average([1,2,3,4]) should return 2.5
def average(lst):
    sum = 0
    avg = lst[0]
    for i in range(len(lst)):
        sum = sum + lst[i]
    avg = sum / len(lst)
    return avg

x = average([10,20,30,40])
# print(x)

def ret_avg(lst):
    sum=0
    avg=lst[0]
    for i in range (0,len(lst),1):
        sum=sum+lst[i]
    avg=sum/len(lst)
    return avg

# x = ret_avg([1,2,3,4])
# print(x)
# so this was working but my terminal wasn't displaying the decimal so I thought it wasn't working. 
# I need to figure out how to see the decimal. google...be back.
# -----------------------------------------------------|  
# 5. Length - Create a function that takes a list and returns the length of the list.
#    Example: length([37,2,1,-9]) should return 4
#    Example: length([]) should return 0
def list_length(lst):
    count = 0
    for i in range(len(lst)):
        count = count + 1
    return count

x = list_length([37,2,1,-9])
# print(x)

def list_length_alt(lst):
    return len(lst)
x = list_length_alt([37,2,1,-9])
# print(x)

# -----------------------------------------------------|  
# 6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#    Example: minimum([37,2,1,-9]) should return -9
#    Example: minimum([]) should return False

# def minimum(arr):
#     min = arr[0]
#     if arr = []:
#         print("False")
# #     else:
# #         for i in range(len(arr)):
# #             if min > arr[i]:
# #                 min = arr[i]
        
# #     return min

# x = minimum([37,2,1,-9])
# y = minimum([])
# print(x)
# print(y)

#  The above code is me trying to figure it out--I had the logic, just not the way to write it- more practice!
#  I was able to write the min and max below but not the if/false statement for the emtpy list. 
#  Below is the solution for comparison and study reference.

def minimum(lst):
    if len(lst) == 0:
        return False

    result = lst[0]
    for val in lst:
        if val < result:
            result = val
    return result

# print(minimum([37,2,1,-9]))
# print(minimum([]))

def minimum_todd(nums_list):
    if len(nums_list) == 0:
        return False
    else:
        min = nums_list[0]
        for idx in range(len(nums_list)):
            if nums_list[idx] < min:
                min = nums_list[idx]
        return min
# print(minimum_todd([37,2,1,-9])) 
# print(minimum_todd([]))


def minimum_nrd(lst):
    if len(lst) == 0:
        return [False, "Empty List"]
    else:
        min_val = lst[0]
        for val in range(0, len(lst), 1):
            if min_val > lst[val]:
                min_val = lst[val]
        return min_val
# print(minimum_nrd([37,2,1,-9])) 
# print(minimum_nrd([]))

 
# -----------------------------------------------------|  
# 7. Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
#    Example: maximum([37,2,1,-9]) should return 37
#    Example: maximum([]) should return False
# def maximum(arr):
#     max = arr[0]
#     for i in range(len(arr)):
#         if max < arr[i]:
#             max = arr[i]
#     return max

# x = maximum([37,2,1,-9])
# print(x)

def maximum(lst):
    if len(lst) == 0:
        return False 

    result = lst[0]
    for val in lst:
        if val > result:
            result = val
    return result

# print(maximum([37,2,1-9]))
# print(maximum([]))
#    for now I'm writing it out long ways in some places until I am more comfortable 
#    with the behavior. I see how I have still been using arr instead of lst.

def maximum(lst):
    if len(lst) == 0:
        return False
    max_val = lst[0]
    for val in range(0,len(lst),1):
        if max_val < val:
            max_val = val
    return max_val

# print(maximum([37,2,1,-9]))
# print(maximum([]))

#  this is after watching the walkthrough..I like this one below.
def maximum_nrd(lst):
    if len(lst) == 0:
        return [False, "Empty List"]
    else:
        max_val = lst[0]
        for val in range(0, len(lst), 1):
            if max_val < lst[val]:
                max_val = lst[val]
        return max_val
# print(maximum_nrd([37,2,1-9]))
# print(maximum_nrd([]))

# -----------------------------------------------------|  
# 8. Ultimate Analysis - Create a function that takes a list and returns a dictionary 
#    that has the sumTotal, average, minimum, maximum and length of the list.
#    Example: ultimate_analysis([37,2,1,-9]) should return 
#    {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
#    Here we are returning a dictionary (object) with key value pairs.


#  This one was especially hard. This is the solution below. I'm using  it to study. 
#  I have only watched day one lectures, maybe this in in day two.
#  Those are next, after this assignment I was going to watch and get ready for class.


def ultimate_analysis(lst):
    # handle
    result = {
        'sum_total': None,
        'maximum': None,
        'minimum': None,
        'average': None,
        'length': 0
    }
    if len(lst) == 0:
        return result
    else:
        result['sum_total'] = 0
        result['maximum'] = lst[0]
        result['minimum'] = lst[0]
    
    for val in lst:
        if val > result['maximum']:
            result['maximum'] = val
        elif val < result['minimum']:
            result['minimum'] = val

        result['sum_total'] += val
        result['length'] += 1
    result['average'] = result['sum_total'] / len(lst)

    return result

# print(ultimate_analysis([37, 2, 1, -9]))
# print(ultimate_analysis([]))

#  this is still a copy of the solution. I just changed the variable name from result 
#  to dict_items for my brain to track and comprehend the behavior. 
def ultimate_analysis(lst):
    # handle
    dict_items = {
        'sum_total': None,
        'maximum': None,
        'minimum': None,
        'average': None,
        'length': 0
    }
    if len(lst) == 0:
        return dict_items
    else:
        dict_items['sum_total'] = 0
        dict_items['maximum'] = lst[0]
        dict_items['minimum'] = lst[0]
    
    for val in lst:
        if val > dict_items['maximum']:
            dict_items['maximum'] = val
        elif val < dict_items['minimum']:
            dict_items['minimum'] = val

        dict_items['sum_total'] += val
        dict_items['length'] += 1
    dict_items['average'] = dict_items['sum_total'] / len(lst)

    return dict_items

# print(ultimate_analysis([37, 2, 1, -9]))
# print(ultimate_analysis([]))


def ultimate_analysis_nrd(lst):
    sumTotal = sum_total(lst)
    average = ret_avg(lst)
    minimum = minimum_nrd(lst)
    maximum = maximum_nrd(lst)
    len_ = list_length_alt(lst)
    analysis = {
        'sumTotal': sumTotal,
        'average': average,
        'minimum': minimum,
        'maximum': maximum,
        'length': len_        
    }
    return analysis

# print(ultimate_analysis_nrd([37, 2, 1, -9]))

# -----------------------------------------------------|  
# 9. Reverse List - Create a function that takes a list and return that list with values reversed. 
#    Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#    Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]


#    I couldn't see this one at all. This is the solution. I'll study the behavior this weekend. 

def reverse_list(lst):
    half_len = int(len(lst) / 2)
    for i in range(half_len):
        # this is a neat way to do a python swap, a temp is equally valid
        lst[i] , lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return lst

# some robust test cases
# print(reverse_list([37, 2, 1, -9]))
# print(reverse_list([37, 2, 1, -9, 5]))
# print(reverse_list([]))
# print(reverse_list([1]))
# print(reverse_list([1, 2]))

def reverse_list_nrd(lst):
           



# some robust test cases
# print(reverse_list([37, 2, 1, -9]))
# print(reverse_list([37, 2, 1, -9, 5]))
# print(reverse_list([]))
# print(reverse_list([1]))
# print(reverse_list([1, 2]))