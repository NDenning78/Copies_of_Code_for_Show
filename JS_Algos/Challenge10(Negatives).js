// this challenge is to write a function that replaces 
// any negative value in an array with the value of 0.

var arr2 = [1,-5,10,-2,3,13,-1,9,-47];

function noNeg(arr)
{
    var x = 0;
    for(var n = 0; n < arr.length; n++)
    {
        if(arr[n] < x)
        {
            arr[n] = x;
        }
    }

    return arr;
}
consolle.log(noNeg(arr2));

// the above code runs clean in JS BIN.