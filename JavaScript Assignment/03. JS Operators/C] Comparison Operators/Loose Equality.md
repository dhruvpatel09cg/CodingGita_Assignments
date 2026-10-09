# Loose Equality

Q1) Check whether the string `"25"` is loosely equal to the number `25`.

```js
console.log("25" == 25)
// Output: true
```

Q2) Check if `0 == false` returns true or false.

```js
console.log(0 == false)
// Output: true
```

Q3) Predict the output:

```js
console.log(10 == "10"); // Output: true
console.log(null == undefined); // Output: true (JS edge case, 0 == NaN)
```

Q4) Predict the output:

```js
console.log("" == 0); // Output: true
console.log([] == false); // Output: true
```

Q5) Why does `NaN == NaN` return `false`?

Answer: In JS NaN represents a not defined number whose value doesn't matches to any other input including itself.
