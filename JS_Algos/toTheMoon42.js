function toTheMoon(num){
    var a = 1;
    var b = 0;
    var sum = 2;
    for (var n = 0; n < (num-1); n++){
        b = a + a;
        a = b;
        // console.log(b)
        sum += b;
    }
    return sum;
}
results = toTheMoon(42)
console.log("Results: " + results);





// This function above runs clean. 
// The results are correct and the "num" parameter
// can be used to tell different stories of the same math.
//  30 days of rice..42 paper folds to the moon..etc.
// For every iteration and increment we double the value.
// Starting with "1", iterating until we reach "num".
// 42 paper folds at 0.05mm equals 136,640 miles!!!!



















// function multiply(a,b)
// {
//     return a * b;
// }
// multiply(5,7)

// function square (n)
// {
// return n * n;
// }
// square(4)

// function cube(x)
// {
// return x * x * x;
// }
// cube(3)


// function to_the_moon(num) {
//     var arr = [];
//     var x = 0;
//     // var total = 0;

//     for (var n = 1; n < num + 1; n++) {
//         arr.push(n);
//     }

//     for (var r = 0; r <= arr.length; r++) {
//         x += arr[r];
//         // total += x;
//         console.log(x);
//     }    
// }
// to_the_moon(42)



// function toTheMoon(num){
//     var arrtemp =[];
//     var arrMoon = [];
//     var moon = 0;
//     for (var n = 1; n <= num; n++){
//         arrtemp.push(n);
//     }
//     console.log(arrtemp);

//     for (var i = 0; i < arrtemp.length; i++){
//         moon = arr[i] + arr[i];
//         arrMoon.push(moon);
//     }
//     return arrMoon;
// }
// toTheMoon(42);


// function toTheMoon(num){
//     var x = 1;
//     while (x <= num){
//         x *= x;
//     }
//     console.log(x);
// }
// toTheMoon(42)


