
// this funtion will sum all the odd values within 5000.
// the 5000 value is specific to this lesson. 

function sum_odd_5000()
{
    var sumDojo = 0;
    var arrOdd = [];
    var arrEven = [];
    var sumOdd = 0;
    var sumEven = 0;

    for(var n = 0; n <= 5000; n++) // use a smaller value for practice.
    {
        if(n % 2 !== 0) // this is the not equal to.
        // this can look two ways.
        //(n % 2 === 1) this is equal to remainder 1.
        //which in this case means odd numbers. 
        {
            arrOdd.push(n);
        }

        if(n % 2 === 0)
        {
            arrEven.push(n);
        }
    }

    for(var r = 0; r < arrOdd.length; r++)
    {
        sumOdd += arrOdd[r];
    }

    for(var d = 0; d < arrEven.length; d++)
    {
        sumEven += arrEven[d];
    }
    sumDojo = sumEven + sumOdd;

    return sumOdd;
}

// coding dojo example below

function sum_odd_5000()
{
    var sum = 0;
    for(var i = 0; i <= 5000; i++)
    {
        if(i % 2 == 1)
        {
            sum = sum + i;
        }
    }
    return sum;
}

// my new example below

function sumOdd_5000(){
    var sum = 0;
    for (var n = 1; n <= 5000; n++){
        if(n % 2 !== 0){
            sum += n;
        }
    }
    return sum;
}
var result = sumOdd_5000();
console.log(result);