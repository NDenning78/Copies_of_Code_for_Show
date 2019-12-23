// Intro To Programming //

function doubleArrayVals(arr) 
{
    for (var i = arr.length-1; i >= 0; i--) 
    {
        arr.push(arr[i]);
    }  
    return arr;
}
    
var myArr = ["apple", "peach", "pear"];
console.log(doubleArrayVals(myArr));
