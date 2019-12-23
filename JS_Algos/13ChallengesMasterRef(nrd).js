// 13 Challenge Master Reference
// Neil Denning


//---------------------------------------------------------------//
// #1 Get an array to print 1 -> 255.
function get_array(){
    var arr = []; 
    for(var n = 1; n <= 255; n++){
        arr.push(n);
    }
    return arr;
}
var result = get_array()
console.log(result);


//---------------------------------------------------------------//
// #2 Get the Sum of all the even numbers from 1 -> 1000.
function getEvenNum(){
    var sumEven = 0;
    for (var n =1; n <= 1000; n++){
        if(n % 2 === 0){
            sumEven += n;
        }
    }
    return sumEven;
}
var result = getEvenNum();
console.log(result); // 
//---------------------------------------------------------------//
// #3 Sum all the odd numbers from 1 -> 5000.
function sumOdd_5000(){
    var sum = 0;
    for (var n = 1; n <= 5000; n++){
        if(n % 2 !== 0){
            sum += n;}}
    return sum;
}
var result = sumOdd_5000();
console.log(result);

//---------------------------------------------------------------//
// #4  Iterate an Array. Return the sum of all the values of an array.
function sumAllArr(arr)
{
    var sum = 0;
    for(var n = 0; n < arr.length; n++)
    {
        sum += arr[n]
    }
    return sum;
}
console.log(sumAllArr([5,10,15,20]));  // = 50

//---------------------------------------------------------------//
// #5 Write a function that returns the maximum number in the array.
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
console.log(findMax([1,5,8,12]));

//---------------------------------------------------------------//
// #6 Write a function that returns the average of the values in the array.
function findAvg(arr)
{
    var sum = 0;    
    for(var n = 0; n < arr.length; n++)
    {
        sum += arr[n];
    }
    return sum / arr.length;
}
console.log(findAvg([1,5,9,11,14]))  
//---------------------------------------------------------------//
// #7
function oddNumbers() 
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
console.log(oddNumbers());

//---------------------------------------------------------------//
// #8
function greaterY(arr, Y)
{
    var countY = 0;
    for(var n = 0; n < arr.length; n++)
    {
        if(arr[n] > Y)
        {
            countY++;
        }
    }
    return countY;
}
console.log(greaterY([1,2,5,7,20], 9)); 

//---------------------------------------------------------------//
// #9
function squareVal1(arr)
{
    for(var n =0; n < arr.length; n++)
    {
        arr[n] *= arr[n];
    }
    return arr;
}
console.log(squareVal1([2,4,5,8]));

//---------------------------------------------------------------//
// #10
function noNeg(arr)
{
    for(var n = 0; n < arr.length; n++)
    {
        if(arr[n] < 0)
        {
            arr[n] = 0;
        }
    }
    return arr;
}
consolle.log(noNeg([1,-5,10,-2,3,13,-1,9,-47]));

//---------------------------------------------------------------//
// #11
function maxMinAvg(arr)
{
    var arrNew = [];
    var sum = 0;
    var max = arr[0];
    var min = arr[0];
    var avg = arr[0];

    for(var n = 0; n < arr.length; n++){
        if(max < arr[n]){
            max = arr[n];}}
    arrNew.push(max);

    for(var r = 0; r < arr.length; r++){
        if(min > arr[r]){
            min = arr[r];}}
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

// This is what I've been writing out on the algorithm app- after reading the book I see how I can avoid 
// repeating my for loops. One for loop with 3 conditions/actions inside instead of three for loops with one condition/action inside.
// Below is my updated maxMinAvg function.
// Still # 11



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
// #12
function swapVal(arr)
{
    var temp = arr[0];
    arr[0] = arr[arr.length - 1];
    arr[arr.length - 1] = temp;
    return arr;
}
console.log(swapVal([1,2,3,4,5,6,7,8,9,10]));

//---------------------------------------------------------------//
// #13
var arrTest = [2,8,-3,0,7,-2,13,1,-1];

function  numToStr(arr){
    for(var n = 0; n < arr.length; n++)
    {
        if(arr[n] < 0){
            arr[n] = 'JS is Fun!';
        }
    }
    return arr;
}
console.log(numToStr(arrTest));



