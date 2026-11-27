# indexOf()

Q1) Create an array of 6 fruits. Find the index of a fruit that exists and one that does not exist using `indexOf()`.

```js
const fruits = ["Mango", "Banana", "Grapes", "Berry", "Pineapple", "Apple"]
console.log(fruits.indexOf("Berry"))
console.log(fruits.indexOf("Strawberry"))
```

Q2) Create an array `["A", "B", "C", "B", "D"]`. Print the index of `"B"` using `indexOf()`.

```js
const alphabets = ["A", "B", "C", "B", "D"];
console.log(alphabets.indexOf("B"))
```

Q3) Create an array of 4 student names. Check the index of your name (or any name) and print the result.

```js
const students = ["Ishant", "David", "Om", "Ellis"];
console.log(students.indexOf("Dhruv"))
```

Q4) What does `indexOf()` return if the element is not found?

=> `indexOf()` returns -1 if the element is not found in array.

Q5) What will `indexOf()` return if the element appears more than once in the array?

=> Element is present more than once in the array `indexOf()` returns the index of the first appearance of element in an array.
