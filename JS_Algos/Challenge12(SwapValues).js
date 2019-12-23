


var arr2 = [1,5,10,-2];
function swap(arr)
{
    var temp = arr[0];
    arr[0] = arr[arr.length - 1];
    arr[arr.length - 1] = temp;
    return arr;
}
console.log(swap(arr2));
// the above code runs clean in JS BIN


// below is the "coding dojo" code
// [1,5,10,-2]
var arrX = [1,5,10,-2];
function swap(arr)
{
    var temp = arr[0];  // this creates a variable called temp that is equal to arr[0].
    arr[0] = arr[arr.length - 1]; // this makes index 0 equal to the last index (array length - 1).
    arr[arr.length - 1] = temp; // this changes the last index (array length - 1) to the variable called temp.
    //(which is equal to the original array index 0)
    //the three lines of code above swap index 0 with the last index of any array length.
    //no if, no analysis, just static swap.
}

// everything below is non functional code- broken 
//--fix it with this example above

// Work this out on the whiteboard! <<<<<<<
var arr2 = [5, 3, 4, 1, 20, 34, 7, 11];
function swap(arr)
{
    for (var x = 0; x < arr.length; x++) 
    {
        for (var y = arr.length - 1; y >= x; y--) 
        {
            if (arr[x] > arr[y]) 
            {
                var temp = arr[y];
                arr[y] = arr[x];
                arr[x] = temp;
            }
        }
    }
}
console.log(swap(arr2));


var arr = [5,3,4,1];

for(var x = 0; x < arr.length; x++)
{
    for(var y = arr.length -1; y >= x; y--)
    {
        if(arr[x] > arr[y])
        {
            var temp = arr[y];
            arr[y] = arr[x];
            arr[x] = temp;
        }
    }
}

console.log(arr);


