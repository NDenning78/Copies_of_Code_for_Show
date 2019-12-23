



function sumAllArr(arr)
{
    var sumDojo = 0;

    for(var n = 0; n < arr.length; n++)
    {
        sumDojo += arr[n]
    }
    return sumDojo;
}
sumAllArr();


//for this challenge we were provided a set of arrays and asked to sum the values within the arrays.
// to practice: write your own set of arrays and for loops to log different outputs.

// coding dojo example below

function iterArr(arr)
{
    var sum = 0;
    
    for(var i = 0; i < arr.length; i++)
    {
        sum = sum + arr[i];
    }
    return sum;
}
iterArr([1,2,5]) // this should call the function to run with [1,2,5] as the array.

