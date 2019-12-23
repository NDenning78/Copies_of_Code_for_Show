function findAvg(arr)
{
    var nrd = 0;
    
    for(var n = 0; n < arr.length; n++)
    {
        nrd += arr[n];
    }
    return nrd / arr.length;
}

// this function will find the average of an array.

function findAvg2(arr2)
{
    var nrd2 = 0;
    var arr2 = [1,2,3,4,5,6,7,8,9,10,100];
    
    for(var r = 0; r < arr2.length; r++)
    {
        nrd2 += arr[r];
    }
    return nrd2 / arr2.length;
}
