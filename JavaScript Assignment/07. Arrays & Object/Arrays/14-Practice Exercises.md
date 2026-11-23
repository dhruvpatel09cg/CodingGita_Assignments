# 14. Practice Exercises

Q1) Given the array:
    `const numbers = [12, 7, 18, 25, 4, 9, 30];`  
    Print only the **even numbers** using a loop.

```js
const numbers = [12, 7, 18, 25, 4, 9, 30];
for (const number of numbers){
    if (number%2===0){
        console.log(number)
    }
}
```

Q2) Given the array:  
   `const cities = ["Ahmedabad", "Surat", "Rajkot", "Vadodara", "Bhavnagar"];`  
   Print all city names in **reverse order** (last to first) using a loop.

```js
const cities = ["Ahmedabad", "Surat", "Rajkot", "Vadodara", "Bhavnagar"];
let i = cities.length-1
while (i>=0){
    console.log(cities[i])
    i--
}
```

Q3) Given the array:  
   `const scores = [12, 45, 7, 89, 23];`  
   Find and print the **second largest** number.

```js
const scores = [12, 45, 7, 89, 23];
let largest = -Infinity
let secondLarge = -Infinity;
for (const score of scores){
    if (score>largest){
        secondLarge = largest
        largest = score
    }
}
console.log(secondLarge)
```

Q4) Given the array:  
   `const colors = ["Red", "Blue", "Green", "Yellow"];`  
   Use `push()` to add `"Purple"` at the end and `unshift()` to add `"Black"` at the beginning. Then print the final array.

```js
const colors = ["Red", "Blue", "Green", "Yellow"];
colors.push("Purple")
colors.unshift("Black")
console.log(colors)
```

Q5) Given the matrix:  

   ```javascript
   const matrix = [
       [10, 20, 30],
       [40, 50, 60]
   ];
   ```  

   Calculate and print the **sum of all elements**.

```js
let sum = 0;
const matrix = [
    [10, 20, 30],
    [40, 50, 60]
];
for (let i=0; i<matrix.length; i++){
    for (let j=0; j<matrix[i].length; j++){
        sum+=matrix[i][j]
    }
}
console.log(sum)
```

Q6) Given the array:  
   `const marks = [45, 67, 89, 32, 76, 91, 54];`  
   Count how many numbers are **greater than 50** and print the count.

```js
let count=0
const marks = [45, 67, 89, 32, 76, 91, 54];
for (const mark of marks){
    if (mark>50){
        count++
    }
}
console.log(count)
```

Q7) Given the matrix:  

   ```javascript
   const matrix = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
   ];
   ```  

Print only the **main diagonal elements** (1, 5, 9).

```js
const matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];
for (let i=0; i<matrix.length; i++){
    for (let j=0; j<matrix[i].length; j++){
        if (i==j){
            console.log(matrix[i][j])
        }
    }
}
```
