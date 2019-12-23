function sum_even_numbers()
{
    var arr1odd = [];
    var arr2even = [];
    var sumOdd = 0;
    var sumEven = 0;

   
    // create even and odd arrays with 1 for loop containing 2 if statements .
    for(var n =1; n <= 1000; n++)
    {
        if (n % 2 === 0) // === means equal to        
        {
            arr2even.push(n);
        }
        // modulus 2 pushes numbers counting by 2. 
        // remainder 0 means we increment up to next number with remainder 0.
        //Modulus Number indicates how much to count by.
        //mod 2 remainder 0 would count by 2 starting at 1 (var n=1) ex: 2, 4, 6, 8, etc..
        //mod 5 remainder 0 would count by 5 starting at 1 (var n=1) ex: 5, 10, 15, 20 etc..
        //mod 5 remainder 1 would count by 5 starting at 1 (var n=1) ex: 1, 6, 11, 16, etc..
        //we start counting from var n which is 1, but we identify our first mod with the correct remainder
        //then we count by mod integer. 
        if (n % 2 !== 0) // !== is not equal to. so this mod 2, 
        // meaning that we are counting by 2 with a remainder not equal to 0.
        // starting at 1(var n=1)       
        {
            arr1odd.push(n);
        }
        //if(n % 3 === 2)
        //modulus 2 pushes numbers counting by 2.
        // remainder 1 means we count by modulus number starting at 1.
        //Modulus Number indicates how much to count by.
        //modulus 3 remainder 1 would count by 3 starting at 1. ex: 1, 4, 7, 10, 13 etc..
        //modulus 3 remainder 2 would count by 3 starting at 2. ex: 2, 5, 8, 11, 14 etc..
    }


    for(var d = 1; d <= 1000; d++) // to understand better try a smaller value like 100 or 10. 
    {
        if (d % 2 === 0)
        {
            sumEven += d; // sumEven = sumEven + d;
        }
    }



    for(var r = 0; r < arr1odd.length; r++) // this for loops condition is based on the array length instead
    //of a preset range. 
    {
        sumOdd += arr1odd[r]; // 
    }
}


// coding dojo example

function get_even_numbers()
{
    var sum = 0;
    for(var i = 0; i < 1001; i++)
    {
        if(i % 2 === 0)
        {
            sum += i;
        }
    }
    return sum;
}

// new example below

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
console.log(result);