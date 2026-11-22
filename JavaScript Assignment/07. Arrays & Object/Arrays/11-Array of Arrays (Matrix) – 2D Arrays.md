# 11. Array of Arrays (Matrix) – 2D Arrays

Q1) Create a 4×2 matrix and print **all elements of the second column**.

```js
const matrix = [[1,2], [3,4], [5,6], [7,8]];
for (let i=0; i<matrix.length; i++){
    console.log(matrix[i][1])
}
```

Q2) Given this matrix of student marks, print only the marks of the **third student**:  

   ```javascript
   const marks = [
       [85, 90, 78],
       [70, 75, 80],
       [88, 82, 95],
       [60, 65, 70]
   ];

   for (const ele of marks[2]){
        console.log(ele)
   }
   ```

`console.log(marks[2]);`

Q3) Write code to find and print the **total number of elements** present in a 3×4 matrix.

```js
const nums = [[11, 22, 33, 44], [55, 66, 77, 88], [99, 00, 111, 222]];
let count = 0
// for (let i=0; i<nums.length; i++){
//     for (let j=0; j<nums[i].length; j++){
//         count++
//     }
// }
// console.log(count)

for (let i = 0; i < matrix.length; i++) {
    total = total + matrix[i].length;
}
console.log(total)
```

Q4) Create a 3×3 matrix filled with numbers 1 to 9. Then update the **center element** (index `[1][1]`) to `0` and print the matrix.

```js
const nums = [[1,2,3], [4,5,6], [7,8,9]];
nums[1][1] = 0
console.log(nums)
```

Q5) Access and print the element that is present at the **first row and last column** of any 3×3 matrix you create.

```js
const nums = [[1,2,3], [4,5,6], [7,8,9]];
console.log(nums[0][2])
```
