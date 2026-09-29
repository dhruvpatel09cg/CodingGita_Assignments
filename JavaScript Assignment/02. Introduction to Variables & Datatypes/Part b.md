5. Choose the Correct Keyword Create the following variables using the most appropriate keyword:

- studentName — the value will not change
- marks — the value may change
- schoolName — the value will not change
  
Assign values to all three variables. Change marks and print all variables.
```javascript
const studentName = "Vraj Patel"
let marks = 98
const schoolName = "ABC School"

marks = "99"

console.log(studentName)
console.log(marks)
console.log(schoolName)
```
6. Understand Scope Write a program where var, let, and const variables are declared inside an if block. Try to access all three variables outside the block. Observe and identify which variables can be accessed.
```js
let x = 5
if (x == 5){
  var name1 = "Maan"
  let name2 = "Manan"
  const name3 = "Manav"
}

console.log(name1) // Successfully runs
console.log(name2) // error name2 not defined
console.log(name3) // error name3 not defined
```
7. Test Re-declaration Declare a variable named user using var and declare it again with a different value. Then perform the same experiment using let. Observe what happens and identify which declaration allows re-declaration.
```js
var user = "Found"
var user = "Not Found"

console.log(user) // Runs Successfully

let result = "Pass"
let result = "Fail"

console.log(result) // Error Identifier 'result' has already been declared
```
8. Test Re-assignment Create three variables using var, let, and const. Assign an initial value to each. Try to change the value of all three variables. Observe which variables allow re-assignment and which one produces an error.
```js
var name1 = "Harry"
let name2 = "Hitesh"
const name3 = "Hiren"

name1 = "Sahil"
name2 = "Sam"
name3 = "Sujeet"

console.log(name1) // Runs Successfully
console.log(name2) // Runs Successfully
console.log(name3) // Error Assignment to constant variable.
```
