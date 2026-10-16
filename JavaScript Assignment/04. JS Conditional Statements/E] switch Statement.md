# E] switch Statement

Q1) Write a program that takes a month number (1–12) and prints the number of days in that month using switch
(Hint: Consider 28/29 for February as 28 for simplicity).

```js
let monthNumber = 5;
switch (monthNumber){
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
        console.log("31 Days")
        break
    case 2:
        console.log("28 Days")
        break
    case 4:
    case 6:
    case 9:
    case 11:
        console.log("30 Days")
        break
    default:
        console.log("Invalid")
}
```

Q2) Write a program that checks a character and prints whether it is a vowel or consonant using switch.

```js
let chr = "t";
switch (chr){
    case "a":
    case "e":
    case "i":
    case "o":
    case "u":
        console.log("Vowel")
        break
    default:
        console.log("Consonant")
}
```

Q3) Create a program that takes a number from 1 to 4 and prints the season using multiple cases together:
1 or 2 → Winter
3 or 4 → Summer

```js
let seasonNumber = 2;
switch (true){
    case seasonNumber == 1 || seasonNumber == 2:
        console.log("Winter")
        break
    case seasonNumber == 3 || seasonNumber == 4:
        console.log("Summer")
        break
    default:
        console.log("Invalid")
}
```

Q4) Write a program using switch (true) to assign class based on marks:
≥ 75 → Distinction
≥ 60 → 1st class
≥ 50 → 2nd class
≥ 35 → 3rd class
below 35 → Failed

```js
let marks = 86;
switch (true){
    case marks>=75&&marks<=100:
        console.log("Distinction")
        break
    case marks>=60:
        console.log("1st Class")
        break
    case marks>=50:
        console.log("2nd Class")
        break
    case marks>=35:
        console.log("3rd Class")
        break
    case marks<=35&&marks>=0:
        console.log("Failed")
        break
    default:
        console.log("Invalid Marks")
}
```

Q5) Create a nested switch program:
First take a role (“admin” or “user”).
If role is “admin”, then take an action (“create”, “edit”, “delete”) and print the corresponding message.
If role is “user”, print “Limited Access”.

```js
let role = "admin";
let action = "edit";
switch (role){
    case "admin":
        switch (action){
            case "create":
                console.log("Start creating")
                break
            case "edit":
                console.log("Start editing")
                break
            case "delete":
                console.log("Are you sure?")
                break
            default:
                console.log("Invalid Action")
        }
        break
    case "user":
        console.log("Limited Access")
        break
    default:
        console.log("Invalid Role")
}
```

Q6) Predict and explain the output of the following code. Then correct it so that only one message is printed:

```js
let fruit = "mango";

switch (fruit) {
  case "apple":
    console.log("Apple is red");
  case "mango":
    console.log("Mango is yellow");
  case "banana":
    console.log("Banana is yellow");
  default:
    console.log("Unknown fruit");
}
// Output: Mango is yellow  Banana is Yellow   Unknown fruit
// Explanation: This happens because we haven't given break in any case
```

Corrected Code

```js
let fruit = "mango";

switch (fruit) {
  case "apple":
    console.log("Apple is red");
    break
  case "mango":
    console.log("Mango is yellow");
    break
  case "banana":
    console.log("Banana is yellow");
    break
  default:
    console.log("Unknown fruit");
}
```

Q7) Write a program that takes a value which can be either a number or a string (0, "0", false, null, undefined) and uses switch to correctly identify each one. Explain why some values may not match as expected.

```js
let val = "0";
switch (true){
    case typeof(val) == "string":
        console.log("String type")
        break
    case typeof(val) == "number":
        console.log("Number type")
        break
    default:
        console.log("Invalid type")
}
```

Explanation: As we only took case of string and number data types so null and undefined are giving Invalid type as type of null is object and undefined for undefined

Q8) Create a tricky calculator using switch that supports these operations:
+, -, *, /, %, and also ** (exponentiation).
Handle division by zero properly inside the corresponding case.

```js
let num1 = 6;
let num2 = 5;
let operator = "%";
switch (operator){
    case "+":
        console.log(num1 + num2)
        break
    case "-":
        console.log(num1 - num2)
        break
    case "*":
        console.log(num1 * num2)
        break
    case "/":
        if (num2==0){
            console.log("Division by 0 is invalid")
        }else{
            console.log(num1 / num2)
        }
        break
    case "%":
        if (num2==0){
            console.log("Modulo with zero is invalid")
        }else{
            console.log(num1 % num2)
        }
        break
    case "**":
        console.log(num1 ** num2)
        break
    default:
        console.log("Invalid Operator")
}
```

Q9) Write a program using switch that takes a date (day number of the month) and prints:
“Beginning of the month” (1–10)
“Middle of the month” (11–20)
“End of the month” (21–31)
Use switch (true) technique for range checking.

```js
let date = 23;
switch (true){
    case date<=10&&date>=1:
        console.log("Beginning of the month")
        break
    case date<=20:
        console.log("Middle of the month")
        break
    case date<=31:
        console.log("End of the month")
        break
    default:
        console.log("Invalid date")
}
```

Q10) Create a multi-level nested switch program for an online food ordering system:
First select Category: "veg" or "non-veg".
Then select Item based on category.
Finally select Size: "half" or "full" and print the final order summary with price.

```js
let category = "veg";
let dish = "Shahi Paneer"
let size = "full"
switch (category){
    case "veg":
        switch (dish){
            case "Chole":
                switch (size){
                    case "half":
                        console.log("You ordered Half-Plate Chole at ₹150")
                        break
                    case "full":
                        console.log("You ordered Full-Plate Chole at ₹300")
                        break
                    default:
                        console.log("Invalid size")
                }
                break
            case "Shahi Paneer":
                switch (size){
                    case "half":
                        console.log("You ordered Half-Plate Shahi Paneer at ₹200")
                        break
                    case "full":
                        console.log("You ordered Half-Plate Shahi Paneer at ₹400")
                        break
                    default:
                        console.log("Invalid size")
                }
                break
            default:
                console.log("Dish Not Available")
        }
        break
    case "non-veg":
        switch (dish){
            case "Fish":
                switch (size){
                    case "half":
                        console.log("You ordered Half-Plate Fish at ₹150")
                        break
                    case "full":
                        console.log("You ordered Full-Plate Fish at ₹300")
                        break
                    default:
                        console.log("Invalid size")
                }
                break
            case "Chicken":
                switch (size){
                    case "half":
                        console.log("You ordered Half-Plate Chicken at ₹180")
                        break
                    case "full":
                        console.log("You ordered Full-Plate Chicken at ₹360")
                        break
                    default:
                        console.log("Invalid size")
                }
                break
            default:
                console.log("Dish Not Available")
        }
        break
    default:
        console.log("Not a Category")
}
```
