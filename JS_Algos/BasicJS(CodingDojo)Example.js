
// this code is coding dojo's example of Basic JavaScript.


var x = 15;
var y = "CodingDojo";
var x_array = [1,5,10,15];
var y_array = ["Coding", "Dojo", "is", "awesome!"];
document.write('hello');  //writes 'hello' on the document
document.write('hello ', y);  //writes 'hello CodingDojo' on the documents
console.log(x);  //logs 15 on the console
console.log(y);  //logs "CodingDojo" on the console
console.log(y_array[3]);  //logs the value in y_array index 3 which is 'awesome!';
//this prints 0 to 99
for(var i=0; i<100; i++){
  console.log(i);
}
//loops through 1 to 100 and prints whether the number is odd or even
for(var j=1; j<=100; j++){
    if(j%2 == 0) {
        console.log(j, ' is an Even number');
    }
    else {
        console.log(j, 'is an Odd number');
    }
}
function sum(x,y){
    console.log('Got the following two parameters', x, y);
    return x+y;
}
console.log(sum(5,3));  //logs 8
console.log(sum(10,15) + sum(3,5));  //logs 33
