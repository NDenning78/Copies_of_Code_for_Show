function a()    
    {
    console.log('hello');
    }
console.log('Dojo');
Dojo

function b() 
    {
    console.log('hello');
    return 15;
    }
var x = b();
console.log('x is', x);
hello, x is , 15


var z = 15;
console.log(z);
function a(z)
    {
   console.log(z);   
   return z;
    }
var b = a(10);
console.log(b);
console.log(z);

15,10,10,15


var c = 15;
console.log(c);
function d(c)
    {
   console.log(c);   
   return c*2;
    }
var e = d(10);
console.log(e);
console.log(c);
15,10,20,15


function a(n) 
    {
    console.log('n is', n);
    y = n*2;
    return y;
    }
var x = a(3) + a(5);
console.log('x is', x);
n is 3, n is 5, x is 16


function x(num1, num2) 
    {  
    return num1+num2;
    }
console.log(x(2,3));
console.log(x(3,5));
5,8


function y(num1, num2) 
    {
    console.log(num1);   
    return num1+num2;
    }
console.log(y(2,3));
console.log(y(3,5));
2,5,3,8


function z(a,b) 
    {
    var c = a + b;
    console.log('c is', c);
    return c;
    }
var x = z(2,3) + z(3,5);
console.log('x is', x);
c is 5, c is 8, x is 13


function d(a,b) 
    {
    var c = a + b;
    console.log('c is', c);
    return c;
    }
var x = d(2,3) + d(3,d(2,1)) + d(d(2,1),d(2,3));
console.log('x is', x);
c is 5, c is 6, c is 8, x is 19

neil denning

