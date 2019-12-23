# The “Basic 13”
# These are Coding Dojo’s foundation “Basic 13” algorithm challenges. Can you finish these in less than two minutes each?   


# Print 1-255
# Print1To255()
# Print all the integers from 1 to 255. 
for num in range (1,256):
    print(num)

 
# Print Ints and Sum 0-255
# PrintIntsAndSum0To255()
# Print integers from 0 to 255, and with each integer print the sum so far. 
sum = 0 
for num in range(0,5):
    sum=num+sum
    print(num,sum)

 
# Find and Print Max
# PrintMaxOfArray(arr)
# Given an array, find and print its largest element. 
def print_max(arr):
    max = arr[0]
    for idx in range (0,len(arr),1):
        if max < arr[idx]:
            max=arr[idx]
    print(max)

print_max([3,5,4,2])

# Array with Odds
# ReturnOddsArray1To255()
# Create an array with all the odd integers between 1 and 255 (inclusive).  
def odd_arr():
    arr= []
    for num in range (1,255):
        if num % 2 == 1:
            arr.append(num)
    print(arr)

odd_arr()

# Greater than Y
# ReturnArrayCountGreaterThanY(arr, y)
# Given an array and a value Y, count and print the number of array values greater than Y. 
def greater_than_y(arr, y):
    count = 0
    for i in range (0,len(arr),1):
        if arr[i] > y:
            count = count+1
    print(count)

greater_than_y([3,2,5,1], 2)
    

# Max, Min, Average
# PrintMaxMinAverageArrayVals(arr)
# Given an array, print the max, min and average values for that array.
def max_min_avg(arr):
    val_max = arr[0]
    val_min = arr[0]
    val_sum = 0
    for i in range (0,len(arr),1):
        if val_max < arr[i]:
            val_max = arr[i]
        if val_min > arr[i]:
            val_min = arr[i]
        val_sum = val_sum + arr[i]
    val_avg = val_sum / len(arr)
    print(val_max)
    print(val_min)
    print(val_avg)
    print("Max: " + str(val_max) + " || ", "Min: " + str(val_min) + " || ", "Avg: " + str(val_avg) + " || ")

max_min_avg([2,1,4,5])

# Swap String For Array Negative Values
# SwapStringForArrayNegativeVals(arr)
# Given an array of numbers, replace any negative values with the string 'Dojo'.
def neg_val(arr):
    for i in range (0,len(arr),1):
        if arr[i] < 0:
            arr[i]= "dojo"
    print(arr)

neg_val([4,-6,3,-2])


# Print Odds 1-255
# PrintOdds1To255()
# Print all odd integers from 1 to 255. 
def odd_num():
    for i in range (1,255):
        if i % 2 == 1:
            print(i)

odd_num()

# Iterate and Print Array
# PrintArrayVals(arr)
# Iterate through a given array, printing each value. 
def it_print(arr):
    for i in range (0,len(arr),1):
        print(arr[i])

it_print([3,5,6,2])


# Get and Print Average
# PrintAverageOfArray(arr)
# Analyze an array’s values and print the average. 
def print_avg(arr):
    sum=0
    avg=arr[0]
    for i in range (0,len(arr),1):
        sum=sum+arr[i]
    avg=sum/len(arr)
    print(avg)

print_avg([7,3,4,6])


# Square the Values
# SquareArrayVals(arr)
# Square each value in a given array, returning that same array with changed values. 
def sq_val(arr):
    for i in range (0,len(arr),1):
        arr[i]=arr[i]*arr[i]
    print(arr)

sq_val([5,8,2,4])


# EXTRA Swapping
def swap(arr):
    # for i in range (0,len(arr),1):
    temp=arr[0]
    arr[0]=arr[len(arr)-1]
    arr[len(arr)-1]=temp
    print(arr)

swap([5,8,2,4])


# Zero Out Negative Numbers
# ZeroOutArrayNegativeVals(arr)
# Return the given array, after setting any negative values to zero. 
def neg_num(arr):
    for i in range (0,len(arr),1):
        if arr[i] < 0:
            arr[i]=0
    print(arr)

neg_num([10,-4,3,-55])


# Shift Array Values
# ShiftArrayValsLeft(arr)
# Given an array, move all values forward (to the left) by one index, dropping the first value and leaving a 0 (zero) value at the end of the array.
# def shift_val(arr):
#     for i in range (0,len(arr),1):
#         if arr[i]