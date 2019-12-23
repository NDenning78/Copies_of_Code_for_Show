




function squareVal1(arr1)
{
    var arr1 = [1,2,3];
    for(var n =0; n < arr1.length; n++)
    {
        arr1[n] =  arr1[n] * arr1[n];
    }
    return arr1;
}


function squareVal2(arr2)
{
    var arr2 = [-1,3,6];
    for(var r =0; r < arr2.length; r++)
    {
        arr2[r] =  arr2[r] * arr2[r];
    }
    return arr2;
}


function squareVal3(arr3)
{
    var arr3 = [0];
    for(var d =0; d < arr3.length; d++)
    {
        arr3[d] =  arr3[d] * arr3[d];
    }
    return arr3;
}


squareVal1()
squareVal2()
squareVal3()

// these functions will return the square of each array index. 