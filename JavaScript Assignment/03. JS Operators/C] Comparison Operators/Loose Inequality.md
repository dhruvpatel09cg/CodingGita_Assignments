# Loose Inequality

Q1) Check whether `"18" != 18` returns true or false.

```js
console.log("18"!=18)
// Output: false
```

Q2) A password is stored as `"1234"`. User enters `1234` (number). Will `!=` return true?

Answer: No, `!=` will give false as loose inequality doesn't checks datatypes, it only checks values.

Q3) Predict the output:

```js
console.log(5 != "5"); // Output: false
console.log(0 != false); // Output: false
```

Q4) Predict the output:

```js
console.log(null != undefined); // Output: false
console.log("" != 0); // Output: false
```

Q5) What does `NaN != NaN` return? Explain.

Answer: It will return true as NaN in JS is a value which is unmatchable with even itself.
