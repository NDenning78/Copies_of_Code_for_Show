function sum_odd_5000()
{
    var arrOdd = [];
    var arrEven = [];
    var sumOdd = 0;
    var sumEven = 0;

    for (var n = 0; n <= 5000; n++){
        if (n % 2 == 1){
            arrOdd.push(n);
        }
        if (n % 2 === 0){
            arrEven.push(n);
        }
    }
    for (var r = 0; r < arrOdd.length; r++){
        sumOdd += arrOdd[r];
    }
    for (var d = 0; d < arrEven.length; d++){
        sumEven += arrEven[d];
    }
    sumDojo = sumEven + sumOdd;
    return sumOdd;
}
sumOdd()