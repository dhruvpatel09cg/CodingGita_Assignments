# Exponentiation

Q1) Find the volume of a cube with a side length of 6 cm using `side ** 3`.

```js
let sideOfCube = 6
let volOfCube = sideOfCube ** 3
console.log(volOfCube)
```

Q2) Calculate the total number of cells in a square arrangement with 9 cells on each side using `side ** 2`.

```js
let cellsEachSide = 9
let totalSquares = cellsEachSide ** 2
console.log(totalSquares)
```

Q3) Find the value of \( 5^4 \) (5 raised to the power 4) using the exponentiation operator.

```js
console.log(5 ** 4)
```

Q4) A digital image has 1,024 pixels on each side (square image). Find the total number of pixels using `pixels ** 2`.

```js
let pixelPerSide = 1024
let totalPixels = pixelPerSide ** 2
console.log(totalPixels)
```

Q5) Predict the output:

```js
let base = 2;
let power = -1;
let result = base ** power;
console.log(result);
// Output: 0.5
```

Q6) What is the output of `3 ** 4`?

Output: 81

Q7) Calculate the area of a square whose side is 9 units using the exponentiation operator.

```js
let side = 9
let areaOfSquare = side ** 2
console.log(areaOfSquare)
```

Q8) What is the result of `2 ** 5` and `5 ** 2`? Are they the same?

Output: `2 ** 5 = 32`
Output: `5 ** 2 = 25`
They both are not same, first one is 2 raised to power 5 and the second is 5 raised to power 2.

Q9) Predict and explain the outputs (and any errors):

```js
console.log(2 ** 3 ** 2); // Output: 512 => its 3 ** 2 = 9(Powers) and then 2 raised to 9  // right-associative
console.log((2 ** 3) ** 2); // Output: 64 => First 2 raised to 3 = 8 then 8 ** 2
console.log(2 ** -3); // Output: 0.125 => 2 raised to power -3 = 1/2**3
// console.log(-2 ** 2); // It will give syntax error we should cover -2 in ()  // Remember: Syntax error
console.log((-2) ** 2); // Output: 4 => This is the correct way for above situation
console.log(4 ** 0.5); // Output: 2 => Halves the 4
```

Q10) Predict the output:

```js
let a = 10;
let b = 0;
let result = a ** b;
console.log(result);
// Output: 1
```
