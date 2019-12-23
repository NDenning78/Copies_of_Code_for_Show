function findMax(arr)
{
    var max = arr[0];
    for(var x = 0; x < arr.length; x++)
    {
        if(max < arr[x])
        {
            max = arr[x];
        }
    }
    return max;
}