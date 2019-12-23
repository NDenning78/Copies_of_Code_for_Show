var a = 2;-4
while (a < 16) 
{   
    console.log(a);
    a = a * 2;
}
output= 2,4,8,16


var b = 2;
while (b < 30) 
{   
    if (b > 10) 
    {
        b = b + 6;
    }
    b += 3;
}
console.log(b);

output= 


var c = 50;
while (c > 0) 
{   
    if (c > 47) 
    {
        c--;
    }
    else {
        c -= 20;
    }
}
console.log(c);

output= -13


for (var d = 1; d < 8; d += 2) 
{   
    console.log(d);
}

output= 1,3,5,7


for (var e = 10; e < 1000; e *= 10) 
{   
    console.log(e);
}

output= 10, 100


for(var f = 0; f < 5; f++) 
{
    f = f + 1;  
    console.log(f);
}

output= 1,3,5


for (var g = 200; g >= 0; g -= 10) 
{   
    if (g == 200) 
    {
        g = g / 20;
    }
}
console.log(g);

output= 0