# Sorting Algorithms
# Neil Denning

'''
Tim,
So, the selection sort is at the bottom. These here are my attempts at "bubble sort".


FYI- I ended up sorting from the last index to the first index. I kept getting out of range errors going forward.
I used two "for loops", one nested inside the other to sort.
The first "for loop" swaps values if the condition is true (if left value is geater than right value)
starting at the last index. Comparing the "last" to the "second to last". If it is "true", it swaps.
After that it decrements down. *note that if it does swap and decrement down it skips the next index on purpose.
This is the point of the second loop. it catches what the first loop skipped. Super cool!!
I know this isn't exactly what the assignment was, but I had fun writing this, and figuring it out
on the white board. I finally feel like I am getting some of the logic better even if this isn't correct.
I'll study Michaels example to understand the behavior. When I first tried going forward I kept 
getting "out of index range" errors that's why I decided to start from the end of the list and bubble backwards. 
Is that a thing? Backwards bubble sort? lol !
Below are all my test cases and examples from "Michael" and Online "Joe James".
Cool Cool!  
'''
# How to SWAP VALUES in Python

'''
this is how we would write it in JS
var arr = [1,3,5,7];
var temp = arr[0];
arr[0] = arr[1];
arr[1] = temp;
'''

'''here is how in python'''

arr = [1,3,5,7]
arr[0], arr[1], arr[2], arr[3] = arr[3], arr[2], arr[1], arr[0]
# print(arr)

'''the above code is neat for small cases, but for large volumes of changes we need a conditional loop.'''

x = [1,3,11,9,5,7,10,6,14,2,12,4,8,15,13]  #This lst is out of order 1-15.
def bubbleSort_nrd_error(lst):
    for val in range(0,len(lst)+1,1):
        if lst[val] > lst[val+1]: #  Error-index out of range
            lst[val],lst[val+1] = lst[val+1],lst[val]
    return lst

# print(bubbleSort_nrd([1,3,11,9,5,7,10,6,14,2,12,4,8,15,13]))
#  Error-index out of range-

'''See below for next attempt!'''

''' looks like we need a nested conditional loop.'''

x = [1,22,3,16,11,18,9,24,5,7,17,23,10,6,21,25,14,2,12,20,4,8,15,19,13]  #This lst is out of order 1-15.
def bubbleSort_nrd(lst):
    for val in range(len(lst)-1,0,-1):
        if lst[val] < lst[val-1]: # Going from back to front not out of range anymore
            lst[val-1],lst[val] = lst[val],lst[val-1] 
        for val in range(len(lst)-1,0,-1):
            if lst[val] < lst[val-1]: # Going from back to front not out of range anymore
                lst[val-1],lst[val] = lst[val],lst[val-1]     
    return lst
    # print(val)
'''
print(bubbleSort_nrd([5,2,4,8,1,3,6,9,7])) this exact list took 86 moves out of 170 to sort. 
print(bubbleSort_nrd([7,9,1,8,4,3,6,2,5])) this exact list took 130 moves out of 181 to sort. 

Joe James selection sort 
print(selection_sort_jj([7,9,1,8,4,3,6,2,5])) this exact list took 128 moves out of 130 to sort.
try to get results like this.

Insertion sort [5,2,4,8,1,3,6,9,7] same list used 83 of 83 moves. This sort wins!!!<<<

'''
# print(bubbleSort_nrd([1,22,3,16,11,18,9,24,5,7,17,23,10,6,21,25,14,2,12,20,4,8,15,19,13]))
''' Original, by me. This made me really happy even thought it's not exactly what I was supposed to do.
 I came up with the above code on my own. '''
'''the above codes works!! yay lol lol '''
# print(bubbleSort_nrd([1,3,11,9,5,7,10,6,14,2,12,4,8,15,13]))
# first output       [1,2,3,11,9,5,7,10,6,14,4,12,8,13,15]
# --------------------------------------------------------------------------------------------|
''' This is going to be "my sort" with michaels print updates during iterations.
 add print statements to see the progress during the function.
 Haven't gotten to this yet..'''

# def bubbleSort_nrdAlt(lst):
#     for val in range(len(lst)-1,0,-1):
#         if lst[val] < lst[val-1]: # Going from back to front not out of range anymore
#             lst[val-1],lst[val] = lst[val],lst[val-1] 
#         for val in range(len(lst)-1,0,-1):
#             if lst[val] < lst[val-1]: # Going from back to front not out of range anymore
#                 lst[val-1],lst[val] = lst[val],lst[val-1]     
#     return lst
    # print(val)

# print(bubbleSort_nrdAlt([1,22,3,16,11,18,9,24,5,7,17,23,10,6,21,25,14,2,12,20,4,8,15,19,13]))

'''This attempt is to merge michaels example into mine. I'm attempting to use the first for loop
 starting at index zero and go forward not backwards.
 Haven't gotten to this yet either..soon'''
# 
# def bubbleSort_nrd(lst):
#     for val in range(len(lst)-1,0,-1):
#         if lst[val] < lst[val-1]: # Going from back to front not out of range anymore
#             lst[val-1],lst[val] = lst[val],lst[val-1] 
#         for val in range(len(lst)-1,0,-1):
#             if lst[val] < lst[val-1]: # Going from back to front not out of range anymore
#                 lst[val-1],lst[val] = lst[val],lst[val-1]     
#     return lst
    # print(val)

# print(bubbleSort_nrd([1,22,3,16,11,18,9,24,5,7,17,23,10,6,21,25,14,2,12,20,4,8,15,19,13]))
# --------------------------------------------------------------------------------------------|

#  Platform Bubble Sort
# arr = [1,22,3,16,11,18,9,24,5,7,17,23,10,6,21,25,14,2,12,20,4,8,15,19,13]
# def bubbleSort_cd(arr):
#     count = 0
#     for j in range(len(arr)-1):
#         print("\n\n", "-"*50, "Iteration", j)
#         for i in range(len(arr)-1-j):
#             count += 1
#             print("\n","*"*80, "\nindex ", i, "value",  arr[i])
#             print("\n","*"*80, "\ncomparing", arr[i], arr[i+1])
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 print("swapped", arr[i], arr[i+1])
#                 print("array is now", arr)
#             else:
#                 print("no need to swap", arr[i], arr[i+1])
#         print("# of evaluations", count)
#     return arr

# print(bubbleSort_cd(arr))


'''Platform Example - Michaels BubbleSort below'''

arr = [5,1,6,3,4,7,2]
def bubbleSort_cd(arr):
    count = 0
    for j in range(len(arr)-1):
        print("\n\n", "-"*50, "Iteration", j)
        for i in range(len(arr)-1-j):
            count += 1
            print("\n","*"*80, "\nindex ", i, "value",  arr[i])
            print("\n","*"*80, "\ncomparing", arr[i], arr[i+1])
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                print("swapped", arr[i], arr[i+1])
                print("array is now", arr)
            else:
                print("no need to swap", arr[i], arr[i+1])
        print("# of evaluations", count)
    return arr

print(bubbleSort_cd(arr))


'''Selection Sort Attempt One'''


# def selection_sort_nrd(lst):
#     min_val = lst[0]    
#     for i in range(len(lst)):
#         if min_val > lst[i]:
#             min_val = lst[i]
#             print(min_val)
#     return min_val

# print(selection_sort_nrd([22,3,16,11,18,9,24,5,7,17,23,10,6,21,25,14,2,12,20,4,8,1,15,19]))

'''FAILED Attempt-'''

'''online example of selection sort-"Joe James" '''

def selection_sort_jj(A):
    for i in range (0, len(A) - 1):
        minIndex = i
        for j in range (i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j  # I don't understand how the "j" works and not [j]..T-Diagram!!
        if minIndex != i:
            A[i], A[minIndex] = A[minIndex], A[i]
    return A
print(selection_sort_jj([5,2,4,1,3]))
# print(selection_sort_jj([22,3,16,11,18,9,24,5,7,17,23,10,6,21,25,14,2,12,20,4,8,1,15,19]))

'''
After spending a couple hours on the whiteboard using a t-diagram and making notes I understand this 
selection sort better. The first "for loop" is using the indices which is set by "range (0, len(lst) -1)" which is equivalent
to saying range 0-4 for the above example [5,2,4,1,3]. This will allow us to iterate 5 times (the length of the list) starting at 
index 0 (0,1,2,3,4). Each index iteration allows us to do something. In this case, we are looking for the minimum value. At the end of the 
iteration from loop 2 with the minimum value detected, we then swap it with its position and the first index. After this we set the
minimum value variable to be equal to "j" which is the current idex in loop2.. This is only inside loop2. After this we exit loop 2 and check another "if" statement still inside loop1.
This is looking to see if our minimun variable that was just set to "j" is != "i". My second iteration came back false. It was "equal". Which meant
on my second iteration I didn't need to swap any values. It turned out the minimum value was already in the right place. This ended loop1 iteration 1 and we 
can go back up to loop 1 where we are using "i" to increment up and go back into our loop 1 allowing us access to loop 2 again. By incrementing "i" 
and using it (i+1) to set the start range for loop 2 we are protecting the swapped value in the previous loop2..This cycle repeats, finding the minimum value and swapping it 
with the current range start position, until the range start position has incremented to the range stop position. After repeating all these steps the function will
return the list "arguement/parameter" sorted from lowest to highest, left to right. 

After repeating these steps with a new T-Diagram row or section for each iteration I was able to track and follow the behavior to really break down the steps
and follow along. I'm keeping it up on the board for a few days and I took pictures. I hope my explanation reads ok. 
Below is my version of the function. It is the same as "Joe James". This is not original by me. I just changed variable names, not the instructions.
This was fun!! 
Back to Flask!! good times!! Thanks!
'''


def selection_sort_nrd2(lst):
    for idx in range(len(lst)-1):
        min_val = idx
        for val in range(idx+1, len(lst)):
            if lst[val] < lst[min_val]:
                min_val = val
        if min_val != idx:
            lst[idx], lst[min_val] = lst[min_val], lst[idx]
    return lst
print(selection_sort_nrd2([22,3,16,11,18,9,24,5,7,17,23,10,6,]))

            

