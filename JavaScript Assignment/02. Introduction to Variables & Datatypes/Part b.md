5. Choose the Correct Keyword Create the following variables using the most appropriate keyword:

- studentName — the value will not change
- marks — the value may change
- schoolName — the value will not change
  
Assign values to all three variables. Change marks and print all variables.
```javascript
const studentName = "Vraj Patel"
var marks = 98
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
