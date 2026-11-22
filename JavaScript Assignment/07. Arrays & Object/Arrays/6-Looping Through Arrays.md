# 6. Looping Through Arrays

Q1) What are the two types of loops demonstrated in the notes for iterating through an array?

=> for and while loop

Q2) In a standard `for` loop, what condition is typically used to ensure the loop stops before going out of bounds? (`i < ...`)

=> `arr.length`

Q3) In the `while` loop example, where is the increment step (`i++`) placed relative to the array access statement?

=> The increment step should be placed after the array access statement, at the end of loop body.

Q4) Write a `for` loop structure that prints every element of an array named `students`.

```js
const students = ["Kishan", "Chesa", "Gaurav", "Joy"]
for (let i=0; i<students.length; i++){
    console.log(students[i])
}
```

Q5) What happens if your loop condition incorrectly uses `<=` instead of `<` alongside `students.length` when accessing elements?

=> JS prints last index as undefined as it will not be in array.

Q6) Write a `for...of` loop that prints every element of an array named `subject`.

```js
const subjects = ["Physics", "Maths", "Economics", "Gujarati"]
for (const subject of subjects){
    console.log(subject)
}
```

Q7) What is the main advantage of using a `for...of` loop over a traditional `for` loop when you only need the values (and not the indices)?

=> It gives you all elements of array without need of increment condition, array length or stoping condition.

Q8) Given `const colors = ["Red", "Blue", "Green"];`, what will the following code output?

   ```javascript
   for (const color of colors) {
       console.log(color, indexOf(color));
   }
   ```

=> This will give error as we haven't defined `indexOf`

`ReferenceError: indexOf is not defined`
