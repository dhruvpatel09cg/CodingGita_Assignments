# Strict Equality

Q1) Check whether `"25" === 25` returns true or false. Explain why.

```js
console.log("25"===25)
// Output: false
```

Q2) Check if `0 === false` and `null === undefined`.

```js
console.log(0===false) // Output: false
console.log(null===undefined) // Output: false
```

Q3) Predict the output:

```js
console.log(10 === "10"); // Output: false
console.log(true === 1); // Output: false
```

Q4) Predict the output:

```js
console.log("" === 0); // Output: false
console.log([] === false); // Output: false
```

Q5) Why is `===` preferred over `==` in most real-world code?

Answer: `===` is preferred over `==` as it compares the datatype as well along with values.
