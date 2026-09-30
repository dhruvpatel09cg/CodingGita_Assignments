**11. Predict the Hoisting Behavior**  
Without running the code, predict the output of each `console.log()` and identify which lines cause errors. Explain your answer using the rules of hoisting for `var`, `let`, and `const`.

```javascript
console.log(a); // Will run but give undefined => engine knows that it is defined later in code.
console.log(b); // Error Cannot access 'b' before initialization => as engine has idea that it is defined in code but as it runs line-by-line it found b non-initialized.
console.log(c); // Error Cannot access 'c' before initialization => as engine has idea that it is defined in code but as it runs line-by-line it found b non-initialized.

var a = 10;
let b = 20;
const c = 30;
```


**12. Fix the Hoisting Errors**  
The following program contains errors related to hoisting. Fix the code so that it runs correctly without any errors. Make sure your solution follows the rules of hoisting for `var`, `let`, and `const` (you may reorder declarations/assignments or change keywords only where necessary to make it work properly).

```javascript
console.log(x);
console.log(y);
console.log(z);

var x = "Hello";
var y = "World";
var z = "!";
// let and const will show error so we changed them to var.

console.log(x + " " + y + z);
```