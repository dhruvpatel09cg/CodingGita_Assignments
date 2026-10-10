# Less Than

Q1) A box can hold maximum 50 kg. Current weight is 42 kg. Check if more items can still be added.

```js
let maxWeight = 50;
let currentWeight = 42
console.log("Can more items be added in box:", currentWeight < maxWeight)
```

Q2) Age of a person is 16. Minimum age required is 18. Check if the person is underage.

```js
let age = 16;
let requiredAge = 18;
console.log("Is person underage:", age < requiredAge)
```

Q3) Predict the output:

```js
console.log(8 < 12); // Output: true
console.log(20 < 10); // Output: false
console.log(7 < 7); // Output: false
```

Q4) Predict the output:

```js
console.log("8" < 10); // Output: true
console.log("20" < "3"); // Output: true
console.log("hello" < 5); // Output: false
```

Q5) 5. What is the result of `null < 0` and `undefined < 0`? Explain.

Output: false => As JS converts null to number which is 0 so it become 0<0.
Output: false => As JS converts undefined to number so NaN compared to anything give false

Q6) A tank capacity is 500 litres. Current water level is 375 litres. Write a condition using `<` to check if it is not full.

```js
let tankCapacity = 500
let currentLevel = 375
console.log("Is tank full:",  tankCapacity < currentLevel)
```

Q7) Predict and explain:

```js
console.log(false < true); // Output: true => JS will convert both operands to number so 0<1
console.log("5" < "15"); // Output: false => Only the first characters of strings will be compared so 5<1
console.log(NaN < 10); // Output: false => Comparing anything with NaN will give false
```
