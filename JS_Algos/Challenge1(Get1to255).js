// this challenge is to write a function that returns the numbers from 1 to 255.

function get_array()
{
    var arr = 0; 
    for(var n = 1; n <= 255; n++)
    {
        arr.push(n);
    }
    return arr;
}
get_array()





function get_array()
{
    var arrX5 = [];
    var sumX5 = 0;
    var arrY3 = [];
    var sumY3 = 0;
    var arrNRD = [];

    for(var n = 1; n <= 255; n++)   // this for loop builds the arrays
    {
        arrNRD.push(n);

        if (n % 3 === 0)    //could be "while" statement
        {
            arrY3.push(n);
        }
        
        if (n % 5 === 0)    //could be "while" statement
        {
            arrX5.push(n);
        }
    }
     
    for(var r = 0; r < arrY3.length; r++)
    {
        sumY3 += r;     // same as sumY3 = sumY3 + r;
    }
    for(var d = 0; d < arrX5.length; d++)
    {
        sumX5 += d;     // same as sumX5 = sumX5 + d;
    }
//return any variable here 
}