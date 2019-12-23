function oddNumbers() // create an array with only odd numbers between 1-50.
{
    var arr = [];

    for(var n = 1; n < 50; n++)
    {
        if(n % 2 !== 0)
        {
            arr.push(n);
        }
    }
    return arr;
}

// this function will create an array with only odd numbers. the range can be changed. 