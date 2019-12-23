var arr = [5,3,4,1];

for(var x = 0; x < arr.length; x++) // this "for loop" tells the comp to run through the array indexes first to last. 
{
    for(var y = arr.length -1; y >= x; y--) // this "for loop" states that var "y" is equal to array length -1. sames as the last index.
                                            // it states as long as "y" is greater than or equal to x then run the braces below, if statement. 
    {
        if(arr[x] > arr[y])  // this if statement states if array index x is greater than array index y, run the braces below.
        {
            var temp = arr[y]; // these 3 lines of code are meant to swap values. var temp is a temporary value holder.
            arr[y] = arr[x]; // this line sets array index [y] (array length -1 or last index) to array [x] (0 or first index).
            arr[x] = temp;  // this line sets array index [x] (0 or first index) to be the value of our var temp.  
        }
    }
}

console.log(arr);
//new array after first for loop (Y) [1,3,4,5]


//array[0] > array[3] same as- if 5 > 1 true-swap values
///        new array is [1,3,4,5]
//array[0] > array[2] same as- if 1 > 4   not true/return to y--
//array[0] > array[1] same as- if 1 > 3  not true/return to y--
//array[0] > array[0] same as- if 1 > 1  not true/ return to y--
//array[1] > array[3] same as- if 3 > 5  not true/ return to y--
//array[1] > array[2] same as- if 3 >4  not true/ return to y--
//array[1] > array[1] same as- if 3 > 3 not true/ return to y--
//array[2] > array[3] same as- if 4 > 5  not true/ return to y--
//array[2] > array[2] same as- if 4 > 4  not true/ return to y--
//array[3] > array[3] same as- if 5 > 5 not true
