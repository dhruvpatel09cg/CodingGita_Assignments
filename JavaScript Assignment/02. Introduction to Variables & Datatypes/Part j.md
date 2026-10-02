**8. Predict the Output**  
Without running the code, predict what each `console.log` will print. Explain your reasoning (especially for `typeof`).

```javascript
let person = { name: "Amit", age: 22 };
let colors = ["red", "green", "blue"];
function sayHi() {
  return "Hi!";
}
let empty = null;

console.log(typeof person); // print: object , It is an object variable
console.log(typeof colors); // print: object , It is array still it print object due to quirk of JS
console.log(typeof sayHi); // print: function , It is a function
console.log(typeof empty); // print: object , It is a null variable which is left empty intentionally but
 prints object due to quirk of JS
console.log(person.name); // print: Amit , this command asks for name variable inside person object
console.log(colors[1]); // print: green , this asks for the color present at index 1 in array colors
console.log(sayHi()); // print: Hi! , we've called function sayHi() which returns Hi!
```

**9. Fix the Program**  
The following code has multiple errors related to objects, arrays, functions, naming rules, and best practices. Fix it so that it runs correctly.

```javascript
let student1 = { name: "Neha", Age: 19 } // variable name should not start with a number
let scores = [90, 85, 88] // Values of array to be covered in []
function greet(name) {
  return "Hello " + name
} // function declaration should contain (), also function ask for argument name
let maxScore = 100
maxScore = 95 // const doesn't allow reassignment
console.log(student1.name)
console.log(scores[0])
console.log(greet("Iva")) //we have to give name
```

**10. Concept Questions**  
Answer the following in your own words with examples:

a) What is the main difference between an **Object** and an **Array**?  

```md
    Object: It is a collection of a key-value pairs, generally used to store different datatypes in
    a single variable
```

```js
// example:
let obj = {
    name: "Dhruv",
    age : 17
}
```

```md
    Array: It is an ordered list of values, generally stores same datatype values, can be accessed 
    by index
```

```js
// example:
let arr = [12, 34, 56, 78]
```

b) Why does `typeof null` return `"object"`? Is `null` really an object? 

```md
    null is not really an object it is a totally different datatype but typeof null returns object
    due to quirk of JS
```

```js
let x = null
```

c) Why is it recommended to keep arrays with a single data type?  

```md
    arrays are recommended to keep with a single data type to keep code easier to understand and 
    less error-prone.
```

```js
let students = ["Dhruv", "Om", "Kashyap"]
```

d) When should you use `const` and when should you use `let`?

```md
    const: When you are assigning a value to a variable which should be kept constant throughout code and 
    you are not going to change its value you should use const
```

```js
const PI = 3.14
```

```md
    let: When we are declaring a variable whose value we are going to change later in code we should
 prefer let
```

```js
let marks = 78;
marks = 98
```
