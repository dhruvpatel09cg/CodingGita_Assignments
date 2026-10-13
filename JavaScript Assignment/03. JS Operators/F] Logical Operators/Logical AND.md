# Logical AND

Q1) Stored username is `"admin"` and password is `1234`. Check if both are valid using `&&` and print the result.

```js
let username = "admin"
let password = 1234
let enteredUsername = "admin"
let enteredPassword = 1212
let validation = username==enteredUsername && password==enteredPassword
console.log("Is user valid?",validation)
```

Q2) A user is logged in (`isLoggedIn = true`) and has permission (`hasPermission = true`). Check if they can access a page using `&&`.

```js
let isLoggedIn = true;
let hasPermission = true
let accessToPage = isLoggedIn && hasPermission
console.log("Can access a page?",accessToPage);
```

Q3) A product is in stock (`inStock = true`) and its price is less than ₹1000 (`price = 800`). Check if it can be bought using `&&`.

```js
let inStock = true;
let price = 800;
let canBought = inStock && price<1000
console.log("Product can be bought?",canBought);
```

Q4) A student has marks `75` and attendance `80`. Passing requires marks greater than `65` **and** attendance greater than `70`. Check using `&&`.

```js
let marks = 75;
let attendance = 80
let isPass = marks>65 && attendance>70;
console.log("Is the student pass?",isPass)
```

Q5) Two conditions: `isWeekend = true` and `isHoliday = false`. A party happens only if both are true. Check using `&&`.

```js
let isWeekend = true;
let isHoliday = false;
let party = isWeekend && isHoliday;
console.log("Is party happening?",party)
```

## Additional Questions

Q6) Predict the output:

```js
let a = 0;
let b = 10;
let result = a && b;
console.log(result);
// Output: 0
```

Q7) Predict the output:

```js
let x = 5;
let y = 10;
let result = (x > 3 && y) || 0;
console.log(result);
// Output: 10
```

Q8) Predict the output:

```js
let p = "Hello";
let q = "";
let r = "World";
let result = p && q && r;
console.log(result);
// Output: ""
```

Q9) Predict the output:

```js
let val = 5;
let condition = val && (val = 0);
console.log(condition);
console.log(val);
// Output: 0
// Output: 0
```

Q10) Predict the output:

```js
let x = 10;
let y = 20;
let result = (x && y) && (x > y);
console.log(result);
// Output: false
```
