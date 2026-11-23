# 13. Common Mistakes

Q1) What does the following code output?  

```javascript
const arr = [10, 20, 30];
console.log(arr[3]); // undefined
```

Q2) Why is this code considered wrong?  

```javascript
arr[arr.length] = 10;
```

=> This code does the thing correctly but considered wrong as JS specifically provide a method `.push()` at the end of array.

Q3) Correct the above code so that 40 is properly added at the end of the array on the place of 30:  

```javascript
let arr = [10, 20, 30];
arr[arr.length-1] = 40;
```

Q4) What is a “sparse array”? Give one example of how it can be created accidentally.

=> A sparse array is an array that has one or more empty slots(missing elements) between its indexes.

Q5) True or False: Accessing an invalid index throws an error in JavaScript.

=> False

Q6) What is the difference between an array and an object in JavaScript?

=> Array: Stores data as ordered list

Object: Stores dta in key-value pair
