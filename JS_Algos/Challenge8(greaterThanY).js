// This challenge is to write a function that takes an array 
// and returns the number of values that are greater thstn Y.
// state an array with values.
// state a value for Y.
//the function will determine how many values are greater than Y.


function greaterY(arr, Y)
{
    var countY = 0;

    for(var n = 0; n < arr.length; n++)
    {
        if(arr[n] > Y)
        {
            countY++;
        }
    }
    return countY;
}
console.log(greaterY([1,2,5,7,20], 9));  
// thie above function runs clean in JS BIN.



function greaterY1(arr1, Y1)
{
    var arr1 = [1,2,5];
    var Y1 = 1;
    var count1 = 0;

    for(n = 0; n < arr1.length; n++)
    {
        if(arr1[n] > Y1)
        {
            count1++;
        }
    }
    return count1;
}
console.log(greaterY([1,4,8,14,18,11,9,-4], 7)); 
// pay attention to console.log(__) , for this function to log output 
// the array and Y values need to be entered into the function (__).


function greaterY2(arr2, Y2)
{
    var arr2 = [1,3,5,7,20];
    var Y2 = 12;
    var count2 = 0;

    for(r = 0; r < arr2.length; r++)
    {
        if(arr2[r] > Y2)
        {
            count2++;
        }
    }
    return count2;
}


function greaterY3(arr3, Y3)
{
    var arr3 = [-1];
    var Y3 = 0;
    var count3 = 0;

    for(d = 0; d < arr3.length; d++)
    {
        if(arr3[d] > Y3)
        {
            count3++;
        }
    }
    return count3;
}

greaterY1()
greaterY2()
greaterY3()

// these should all run together and return the number of values in each array
// that are greater than var Y in each function.