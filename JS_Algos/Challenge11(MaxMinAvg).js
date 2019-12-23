// Find MAX 
// Neil Denning

function findMaxMinAvg(arr){
    var max = 0;
    var min = 0;
    var avg = 0;
    var sum = 0;
    var arrNew = [];

    for (var n = 0; n < arr.length; n++){
        if (max < arr[n]){
            max = arr[n];
        }
        if (min > arr[n]){
            min = arr[n];
        }
        sum += arr[n];
    }
    avg = sum / arr.length;
    arrNew.push(max, min, avg);
    return arrNew;
}
var result = findMaxMinAvg([1,5,10,-2, 15, -20]);
console.log(result)



//---------------------------------------------------------------//


var arr2 = [1,5,10,-2, 15, -20];

function maxMinAvg(arr)
{
    var arrNew = [];
    var sum = 0;
    var max = arr[0];
    var min = arr[0];
    var avg = arr[0];

    for(var n = 0; n < arr.length; n++)
    {
        if(max < arr[n])
        {
            max = arr[n];
        }
    }
    arrNew.push(max);

    for(var r = 0; r < arr.length; r++)
    {
        if(min > arr[r])
        {
            min = arr[r];
        }
    }
    arrNew.push(min);

    for(var d = 0; d < arr.length; d++)
    {
        sum += arr[d];
    }
    avg = sum / arr.length;

    arrNew.push(avg);  // this should result in avg of array values.
    

    return arrNew;
}
console.log(minMaxAvg(arr2));

//--------------------------------------------------------------------------------//


// var arr2 = [1,5,10,-2, 15, -20];

function maxMinAvg(arr)
{
    var arrNew = [];
    var sum = 0;
    var max = arr[0];
    var min = arr[0];
    var avg = arr[0];

    for(var n = 0; n < arr.length; n++)
    {
        if(max < arr[n])
        {
            max = arr[n];
        }
    }
    arrNew.push(max);

    for(var r = 0; r < arr.length; r++)
    {
        if(min > arr[r])
        {
            min = arr[r];
        }
    }
    arrNew.push(min);

    for(var d = 0; d < arr.length; d++)
    {
        sum += arr[d];
    }
    avg = sum / arr.length;

    arrNew.push(avg);  // this should result in avg of array values.
    

    return arrNew;
}
console.log(minMaxAvg([1,5,10,-2, 15, -20]));