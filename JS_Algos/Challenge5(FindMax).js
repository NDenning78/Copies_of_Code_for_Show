// Find MAX 
// Neil Denning

function findMax(arr){
    var max
}



//---------------------------------------------------------------//



function findMax(arr)
{
    var max = arr[0];
    for(var n = 0; n < arr.length; n++)
    {
        if(max < arr[n])
        {
            max = arr[n];
        }
    }
    return max;
}

//for this challenge we were provided a set of arrays and asked to find the max value within the arrays.
// to practice: write your own set of arrays and for loops to log different outputs.

function findMax2(arr2)
{
    var arr2 = [3,8,-1,9];
    var max2 = arr2[0];

    for(var r = 0; r < arr2.length; r++)
    {
        if(max2 < arr2[r])
        {
            max2 = arr2[r];
        }
    }
    return max2;
}
// this function will return the max number in var arr2 array.