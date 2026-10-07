# Multiplication

Q1) One notebook costs ₹45. Calculate the cost of buying 8 notebooks.

```js
let priceOfNotebook = 45
let quantityOfNotebook = 8
let totalCost = priceOfNotebook * quantityOfNotebook
console.log("Total cost:",totalCost)
```

Q2) A machine produces 120 bottles per hour. Calculate its production in 6 hours.

```js
let productionPerHour = 120
let productionHours = 6
let totalProduction = productionPerHour * productionHours
console.log("Total production:",totalProduction)
```

Q3) A garden has 7 rows with 15 plants in each row. Find the total number of plants.

```js
let totalRows = 7
let plantsPerRow = 15
let totalPlants = totalRows * plantsPerRow
console.log("Total plants:",totalPlants)
```

Q4) Predict the output:

```js
let a = "5";
let b = 4;
let result = a * b;
console.log(result);
// Output: 20
```

Q5) Predict the output:

```js
let x = "10";
let y = "2";
let result = x * y;
console.log(result);
// Output: 20
```

Q6) What is the output of `12 * 8`?

Output: 96

Q7) One pizza costs ₹299. What is the total cost of 4 pizzas?

```js
let priceOfPizza = 299
let quantityOfPizza = 4
let totalCost = priceOfPizza * quantityOfPizza
console.log("Total cost:",totalCost)
```

Q8) What is the result of `"7" * 6` and `"7" * "6"`?

Result: 42 => Same of both.

Q9) A factory produces 45 units per hour. How many units does it produce in 8 hours? Write the expression and calculate.

```js
let unitsPerHour = 45
let productionHours = 8
let totalProduction = unitsPerHour * productionHours
console.log("Total units produced:",totalProduction)
```

Q10) Predict and explain the outputs:

```js
console.log("5" * 3 * "2"); // Output: 30 => JS convert string datatype to number while executing multiplication operator
console.log("abc" * 4); // Output: NaN => As abc cannot be converted to number datatype and 4 is number so JS give output of datatype number but value Not a Number
console.log(10 * "2.5"); // Output: 25 => JS convert string datatype to number while executing multiplication operator
console.log("10" * "2.5" * "0"); // Output: 0 => JS convert string datatype to number while executing multiplication operator
```
