


    var userObj = {"firstName": "Dwight", "lastName": "Schrute", "email": "beetsbears@battlestar.com"};
    console.log(userObj["firstName"]);    // reading the value -- OUTPUT: Dwight
    userObj["lastName"] = "Martin";    // updating the value
    userObj["favoritePrank"] = "jello";    // adding a new key-value pair
    console.log(userObj);    // {"firstName": "Dwight", "lastName": "Martin", "email": "beetsbears@battlestar.com", "favoritePrank": "jello"}


    function printVal(obj, keyName) {
        console.log(obj[keyName]);
    }
    var wand1 = {"wood": "cherry", "core": "phoenix feather", "length": 11.5};
    printVal(wand1, "core");
    var wand2 = {"wood": "chestnut", "core": "dragon heartstring", "length": 10};
    printVal(wand2, "length");




    function updateVal(obj, keyName, val) {
        obj[keyName] = val;
        return obj;
    }
    var dish = {"desc": "fries", "price": 2.99, "size": "L"};
    dish = updateVal(dish, "desc", "waffle fries");
    dish = updateVal(dish, "price", 2.59);
    console.log(dish);



    
    function zip(arr1, arr2) {
        var newObj = {};
        for (var i = 0; i < arr1.length; i++) {
            var key = arr1[i];
            var val = arr2[i];
            newObj[key] = val;
        }
        return newObj;
    }
    var p = zip(["founder", "name", "year"], ["Brandon Eich", "JavaScript", 1995]);
    console.log(p); 