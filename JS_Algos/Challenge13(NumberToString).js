

//Write a function that takes an array of numbers and replaces any negative values within the array
//with the string 'Dojo'. 
//For example if array [-1,-3,2], your function will return ['Dojo','Dojo',2].

var arrXD = [2,8,-3,0,7-2,13,1,-1];

function  numToStr(arr)
{
    var x = 0;
    for(var n = 0; n < arr.length; n++)
    {
        if(arr[n] < x)
        {
            arr[n] = 'Dojo';
        }
    }

    return arr;
}
console.log(numToStr(arrXD));

// the above code runs clean in JS BIN and Coding Dojo App.



//the code below belongs to challenge 10..
// function noNeg(arr) 
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

// the code below is the coding dojo sample

function numToStr(arr)
{
    for(var i = 0; i < arr.length; i++)
    {
        if(arr[i] < 0)
        {
            arr[i] = "Dojo";  // Coding Dojo used " "  instead of ' '.
        }
    }
    return arr;
}