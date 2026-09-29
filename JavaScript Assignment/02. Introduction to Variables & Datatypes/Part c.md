9. Predict and Explain Without running the code, predict the output of each console.log() and identify which lines cause errors. Explain your answer using the rules of scope, re-assignment, and variable declaration.

var x = 10;

if (true) {
    var x = 20;
    let y = 30;
    const z = 40;
}

console.log(x);
console.log(y);
console.log(z);

```js
// console.log(x); ==> Run successfully as var is functional scope
// console.log(y); ==> Error as let is block scope so running variable assigned inside if block will run
                       only inside that block
// console.log(z);  ==> Error as const is block scope so running variable assigned inside if block will run
                       only inside that block
```
10. Fix the Program The following program contains multiple errors. Fix the code so that it runs correctly. Make sure your solution follows the rules for initialization, re-declaration, re-assignment, and scope.
```js
let name; // const without declaration value will give error

var age = 20;
var age = 25; // let doesn't allow redeclaration so we changed to var

if (true) {
    var city = "Delhi";
    var country = "India"; // let only give output inside block so we changed it to var
}

console.log(country); // let only give output inside block so we changed it to var

let score = 50;
score = 80; // const creates constant variable which doesn't allow to reassign value so we changed to let
```
