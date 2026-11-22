# 7. Adding Elements to Arrays

Q1) Which method is used to add an element at the **end** of an array?

=> `push()`

Q2) Which method is used to add an element at the **beginning** of an array?

=> `unshift()`

Q3) Given `let nums = [1, 2, 3];`, write the code to add `4` at the end using the appropriate method. What will `console.log(nums);` show after that?

```js
let nums = [1, 2, 3];
nums.push(4);
console.log(nums)
```

=> Output: `[ 1, 2, 3, 4 ]`

Q4) Continuing from the previous question, write the code to add `0` at the beginning. What will the final array look like?

```js
let nums = [1, 2, 3];
nums.unshift(0);
console.log(nums)
```

=> Output: `[ 0, 1, 2, 3 ]`

Q5) True or False: `push()` and `unshift()` both modify the original array (they are mutating methods).

=> True
