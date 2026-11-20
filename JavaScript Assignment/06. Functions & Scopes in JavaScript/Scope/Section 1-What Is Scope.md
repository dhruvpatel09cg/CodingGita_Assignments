# Section 1: What Is Scope?

Q1) Consider the following code:

```js
var city = "Surat";
function display() {
    var country = "India";
    console.log(city);
    console.log(country);
}
display();
```

Answer the following:

- Which variable is declared in the global scope?

    Answer: `city` variable is declared in global scope.
- Which variable is declared inside the function?

    Answer: `country` variable is declared in function.
- Can both variables be accessed inside `"display()"`?

    Answer: Yes both the variables can be accessed inside `display()`

Q2) Predict the output:

```js
var price = 500;
function calculate() {
    var tax = 50;
    console.log(price + tax);
}
calculate(); // 550
console.log(price); // 500
```

Q3) Identify the scope of each variable:

```js
var college = "ABC College";
function student() {
    var name = "Rahul";
    var age = 20;
}
function teacher() {
    var subject = "JavaScript";
}
```

Classify `"college"`, `"name"`, `"age"`, and `"subject"` as global or function-scoped variables.

Answer: Global scoped variables: `college`

function-scoped variables: `name`, `age`, `subject`

Q4) What will happen when you execute this code? Explain why.

```js
function first() {
    var number = 100;
}
function second() {
    console.log(number);
}
first();
second();
```

Answer: Calling the function `fist()` will not give any output as we just declared a variable inside that function. But calling the function `second()` will give `ReferenceError: number is not defined` as variable number was declared in `first()` so it was not accessible outside that function.

Q5) Write a JavaScript program that:

- Declares one variable in the global scope.
- Declares another variable inside a function.
- Prints both variables inside the function.
- Prints the global variable outside the function.

```js
var x = 45
function myFunc(){
    var y = 35
    console.log(x)
    console.log(y)
}
myFunc()
console.log(x)
```
