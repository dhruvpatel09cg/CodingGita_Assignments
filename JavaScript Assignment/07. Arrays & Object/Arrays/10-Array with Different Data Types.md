# 10. Array with Different Data Types

Q1)  Can a JavaScript array store values of different data types (e.g., number, string, boolean, null) in the same array?

=> Yes, a JS array stores values of different datatypes.

Q2) Write the syntax to create an array named `data` that contains a number, a string, a boolean, and `null`.

```js
const data = [84, "abc", true, null];
```

Q3) How can you check the data type of each element in such an array?

```js
const data = [84, "abc", true, null];
for (const ele of data){
    console.log(typeof(ele))
}
```

Q4)  Given `const data = [100, "Hello", true, null];`, what does `typeof data[0]` return?

=> number

Q5) What does `typeof data[2]` return for the same array?

=> boolean
