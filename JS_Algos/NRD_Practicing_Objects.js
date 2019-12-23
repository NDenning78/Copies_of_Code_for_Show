
function printVal(obj, keyName) 
    {
    console.log(obj[keyName]);
    }
var wand1 = {"wood": "cherry", "core": "phoenix feather", "length": 11.5};
printVal(wand1, "core");
var wand2 = {"wood": "chestnut", "core": "dragon heartstring", "length": 10};
printVal(wand2, "length");