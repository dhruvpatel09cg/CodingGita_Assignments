**1. Create an Object**  
Create an object named `student` with the following properties:

- `name` → `"Riya"`
- `age` → `18`
- `isEnrolled` → `true`  

Print the entire object and then print each property individually.

```js
let student = {
    name : "Riya",
    age : 18,
    isEnrolled : true
}

console.log(student)
console.log(student.name)
console.log(student.age)
console.log(student.isEnrolled)
```

**2. Work with Arrays**  
Create two arrays:

- `scores` containing only numbers: `85, 92, 78, 90`
- `mixedData` containing different types: a number, a string, a boolean, and `null`  

Print both arrays. Also print the first and last element of the `scores` array using index.

```js
let scores = [85, 92, 78, 90]
let mixedData = [854, "Wicket", false, null]

console.log(scores)
console.log(mixedData)
console.log(scores[0])
console.log(scores[scores.length-1])
```

**3. Declare and Call a Function**  
Write a function named `calculateArea` that takes two parameters (`length` and `width`) and returns the area of a rectangle.  
Call the function twice with different values and print the results.

```js
function calculateArea(length, width) {
    let area = length * width
    return area
}

console.log(calculateArea(10, 20))
console.log(calculateArea(34, 85))
```

**4. Check Types with `typeof`**  
Create variables of the following types and print both the value and its type using `typeof`:

- A number  
- A string  
- A boolean  
- `null`  
- An object  
- An array  
- A function  

Observe and note any surprising results (especially with `null` and arrays).

```js
let num = 347
console.log(num)
console.log(typeof(num))

let string = "Hello"
console.log(string)
console.log(typeof(string))

let isStudent = false
console.log(isStudent)
console.log(typeof(isStudent))

let x = null
console.log(x)
console.log(typeof(x)) // typeof of null is giving output 'object' due to js quirk

let obj = {
    user : true,
    plan : "Gold Membership"
}
console.log(obj)
console.log(typeof(obj))

let arr = [347, 8934, 2, 34]
console.log(arr)
console.log(typeof(arr)) // typeof of array is giving output 'object' due to js quirk

function total(s1, s2, s3) {
    let total = s1 + s2 + s3
    console.log(`Total =`,total)
}
total(90, 95, 85)
console.log(typeof(total))
```